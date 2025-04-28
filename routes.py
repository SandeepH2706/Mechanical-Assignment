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
            error_handled = False

            # Try to get constraint name from PostgreSQL error diagnostics
            constraint_name = ''
            if hasattr(e.orig, 'diag'):
                constraint_name = getattr(e.orig.diag, 'constraint_name', '')

            if constraint_name and constraint_name.startswith('uq_answer'):
                # Extract the answer number from constraint name, e.g. 'uq_answer3' -> '3'
                answer_num = constraint_name[-1]
                field = getattr(form, f'answer{answer_num}', None)
                if field:
                    field.errors.append('This answer already exists. Please provide a unique answer.')
                    error_handled = True

            # Fallback: parse constraint name from error message string (if no diag attribute)
            if not error_handled:
                match = re.search(r'constraint "(uq_answer\d+)"', str(e.orig))
                if match:
                    answer_num = match.group(1)[-1]
                    field = getattr(form, f'answer{answer_num}', None)
                    if field:
                        field.errors.append('This answer already exists. Please provide a unique answer.')
                        error_handled = True

            # If no specific field error found, show generic flash message
            if not error_handled:
                flash('Database error occurred. Please try again.', 'danger')

            # Return the form with field errors displayed
            return render_template('main.html', user=user, form=form)

    # For GET or invalid POST, just render the form
    return render_template('main.html', user=user, form=form)


@routes_bp.route('/congrats/<name>')
def congrats(name):
    return render_template('congrats.html', name=name)
