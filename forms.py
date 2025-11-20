from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Regexp
from models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=4, max=20, message='Username must be between 4 and 20 characters long'),
        Regexp(r'^[\w.]+$', message='Username can only contain letters, numbers, dots and underscores')
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message='Please enter a valid email address'),
        Length(max=120, message='Email must be less than 120 characters')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message='Password must be at least 8 characters long'),
        Regexp(r'.*[A-Z].*', message='Password must contain at least one uppercase letter'),
        Regexp(r'.*[a-z].*', message='Password must contain at least one lowercase letter'),
        Regexp(r'.*\d.*', message='Password must contain at least one number'),
        Regexp(r'.*[!@#$%^&*(),.?":{}|<>].*', message='Password must contain at least one special character')
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')

    def validate_username(self, username):
        # Check for case-insensitive username match
        user = User.query.filter(User.username.ilike(username.data)).first()
        if user:
            raise ValidationError('Username already taken. Please choose a different one.')

    def validate_email(self, email):
        # Check for case-insensitive email match
        user = User.query.filter(User.email.ilike(email.data)).first()
        if user:
            raise ValidationError('Email already registered. Please use a different one.')

    def validate_password(self, field):
        try:
            # Create a temporary user to validate password using the model's logic
            temp_user = User()
            temp_user._is_valid_password(field.data) # Use the internal validation method
        except ValueError as e:
            raise ValidationError(str(e))

class QuizForm(FlaskForm):
    title = StringField('Quiz Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    is_advanced = BooleanField('Mark as Advanced Quiz')
    time_limit = IntegerField('Time Limit (minutes, 0 for no limit)', default=0)
    submit = SubmitField('Create Quiz')

class QuestionForm(FlaskForm):
    quiz_id = SelectField('Quiz', coerce=int, validators=[DataRequired()])
    question_text = TextAreaField('Question', validators=[DataRequired()])
    option_a = StringField('Option A', validators=[DataRequired()])
    option_b = StringField('Option B', validators=[DataRequired()])
    option_c = StringField('Option C', validators=[DataRequired()])
    option_d = StringField('Option D', validators=[DataRequired()])
    correct_answer = SelectField('Correct Answer', 
                               choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')],
                               validators=[DataRequired()])
    points = IntegerField('Points', validators=[DataRequired()], default=1)
    submit = SubmitField('Add Question') 