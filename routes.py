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
    error_shown = False  # Track if we found a field-specific error
    
    # PostgreSQL error parsing
    if hasattr(e.orig, 'diag'):
        constraint_name = e.orig.diag.get('constraint_name', '')
        if constraint_name.startswith('uq_answer'):
            error_field = constraint_name[-1]
            if field := getattr(form, f'answer{error_field}', None):
                field.errors.append('This answer already exists. Please provide a unique answer.')
                error_shown = True
    
    # Fallback for non-PostgreSQL or unexpected errors
    if not error_shown:
        constraint_match = re.search(r'constraint "(uq_answer\d+)"', str(e.orig))
        if constraint_match:
            error_field = constraint_match.group(1)[-1]
            if field := getattr(form, f'answer{error_field}', None):
                field.errors.append('This answer already exists. Please provide a unique answer.')
                error_shown = True
    
    if not error_shown:
        flash('Database error occurred. Please try again.', 'danger')
    
    return render_template('main.html', user=user, form=form)

@routes_bp.route('/congrats/<name>')
def congrats(name):
    return render_template('congrats.html', name=name)
