from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from models import User


class RegistrationForm(FlaskForm):
    srn = StringField('srn', validators=[DataRequired(), Length(min=10, max=20)])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


    def validate_srn(self, srn):
        user = User.query.filter_by(srn=srn.data).first()
        if user:
            raise ValidationError('SRN already exists.')

class LoginForm(FlaskForm):
    srn = StringField('srn', validators=[DataRequired(), Length(min=10, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')



class AnswerForm(FlaskForm):
    answer1 = TextAreaField('Answer 1', validators=[DataRequired()], render_kw={'autofocus': True, 'data-parsley-unique': 'true'})
    answer2 = TextAreaField('Answer 2', validators=[DataRequired()], render_kw={'data-parsley-unique': 'true'})
    answer3 = TextAreaField('Answer 3', validators=[DataRequired()], render_kw={'data-parsley-unique': 'true'})
    answer4 = TextAreaField('Answer 4', validators=[DataRequired()], render_kw={'data-parsley-unique': 'true'})
    answer5 = TextAreaField('Answer 5', validators=[DataRequired()], render_kw={'data-parsley-unique': 'true'})
    answer6 = TextAreaField('Answer 6', validators=[DataRequired()], render_kw={'data-parsley-unique': 'true'})
    answer7 = TextAreaField('Answer 7', validators=[DataRequired()], render_kw={'data-parsley-unique': 'true'})
    submit = SubmitField('Submit Answers')