import email
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from market.model import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(user=username_to_check.data).first()
        if user:
            raise ValidationError('Username already taken!')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email assigned to another account!')

    username= StringField(label='Username', validators=[Length(min=2,max=30),DataRequired()])
    email_address = StringField(label='Email address',validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Password',validators=[Length(min=6),DataRequired()]) 
    password2 = PasswordField(label='Re-enter password',validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Create Account')



