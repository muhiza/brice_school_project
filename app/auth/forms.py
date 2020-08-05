"""
This is the form for define the fields that are to be used
for users registration, login and forgot password
"""

# Third-party imports
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import PasswordField, StringField, SubmitField, SelectField,  ValidationError, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo

# Internal imports
from ..models import Employee

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('E-mail', validators=[DataRequired()])
    username = StringField('Amazina', validators=[DataRequired()])
    #first_name = StringField('', validators=[DataRequired()], render_kw={"placeholder": "AMAZINA YOSE"})
    #last_name = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Izina rikurikira"})
    phone_number = StringField('Nimero ya telephone', validators=[DataRequired()])
    password = PasswordField('Ijambo ry\'Ibanga', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Emeza Ijambo ry\'Ibanga')
    #recaptcha = RecaptchaField()
    submit = SubmitField('Iyandikishe')
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
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Ijambo ry\'Ibanga', validators=[DataRequired()])
    #recaptcha = RecaptchaField()
    submit = SubmitField('Injira', render_kw={"onclick": "loading()"})


class ForgetPasswordForm(FlaskForm):
    """
    Form for user to change password
    """
    email = StringField('', validators=[DataRequired(), Email()], render_kw={"placeholder": "Kode yo kwinjira"})
    submit = SubmitField('Ohereza')



class MemberLoginForm(FlaskForm):
    """
    Form for users to login
    """
    cooperative_code = IntegerField('Cooperative Code', validators=[DataRequired()])
    member_id = IntegerField('Member ID', validators=[DataRequired()])
    #recaptcha = RecaptchaField()
    submit = SubmitField('MemberLogin', render_kw={"onclick": "loading()"})
