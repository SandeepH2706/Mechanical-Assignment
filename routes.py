# routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from forms import RegistrationForm, LoginForm, AnswerForm
from models import User, Answer, db
import psycopg2
import re
from sqlalchemy.exc import IntegrityError

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')  # Add this route
def index():
    return render_template('index.html')

@routes_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  # ← Critical initialization
    if form.validate_on_submit():
        # Add registration logic here
        return redirect(url_for('routes.login'))
    return render_template('register.html', form=form)

@routes_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(srn=form.srn.data).first()
        if user and form.password.data == user.password:
            return redirect(url_for('routes.main', srn=user.srn))
        else:
            flash('Login failed. Check SRN and password.', 'danger')
    return render_template('login.html', form=form)

@routes_bp.route('/main/<srn>', methods=['GET', 'POST'])
def main(srn):
    user = User.query.get_or_404(srn)
    form = AnswerForm()

    if form.validate_on_submit():
        try:
            answer = Answer(
                user_srn=srn,
                answer1=form.answer1.data.strip(),
                answer2=form.answer2.data.strip(),
                answer3=form.answer3.data.strip(),
                answer4=form.answer4.data.strip(),
                answer5=form.answer5.data.strip(),
                answer6=form.answer6.data.strip(),
                answer7=form.answer7.data.strip()
            )
            db.session.add(answer)
            db.session.commit()
            flash('Answers submitted successfully!', 'success')
            return redirect(url_for('routes.congrats', name=user.name))

        except IntegrityError as e:
            db.session.rollback()
            error_field = None

            # Handle PostgreSQL error
            orig_error_str = str(e.orig)
            
            # Try to match constraint name
            constraint_match = re.search(r'unique constraint "([^"]+)"', orig_error_str, re.IGNORECASE)
            if constraint_match:
                constraint_name = constraint_match.group(1)
                if constraint_name.startswith('uq_answer'):
                    error_field = constraint_name[-1]  # Last character should be number

            # Try fallback: match field name directly
            if not error_field:
                field_match = re.search(r'\((answer\d)\)=', orig_error_str)
                if field_match:
                    field_name = field_match.group(1)
                    error_field = field_name[-1]  # Last digit

            if error_field:
                field = getattr(form, f'answer{error_field}', None)
                if field:
                    field.errors.append('This answer already exists. Please provide a unique answer.')
            else:
                flash('Database error occurred. Please try again.', 'danger')

            return render_template('main.html', user=user, form=form)

    return render_template('main.html', user=user, form=form)


@routes_bp.route('/congrats/<name>')
def congrats(name):
    return render_template('congrats.html', name=name)
