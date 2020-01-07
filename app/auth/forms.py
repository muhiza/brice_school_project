"""
This is the form for define the fields that are to be used
for users registration, login and forgot password
"""

# Third-party imports
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import PasswordField, StringField, SubmitField, SelectField,  ValidationError, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

# Internal imports
from ..models import Employee

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email Address', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    #first_name = StringField('', validators=[DataRequired()], render_kw={"placeholder": "AMAZINA YOSE"})
    #last_name = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Izina rikurikira"})
    phone_number = StringField('Phone number', validators=[DataRequired()])
    is_union         = BooleanField('is_union')
    is_ferwacotamo   = BooleanField('is_ferwacotamo')
    is_confederation = BooleanField('is_confederation')
    is_rca           = BooleanField('is_rca')
    is_manager       = BooleanField('is_manager')
    is_coop_admin    = BooleanField('is_coop_admin')
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm password')
    #recaptcha = RecaptchaField()
    submit = SubmitField('Register')
    """
    def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')
    """
    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    #recaptcha = RecaptchaField()
    submit = SubmitField('Login', render_kw={"onclick": "loading()"})


class ForgetPasswordForm(FlaskForm):
    """
    Form for user to change password
    """
    email = StringField('', validators=[DataRequired(), Email()], render_kw={"placeholder": "Kode yo kwinjira"})
    submit = SubmitField('Ohereza')
