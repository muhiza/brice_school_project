from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, TextAreaField, FileField, DateTimeField, SelectField, SubmitField, IntegerField
# from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, Optional
from markupsafe import Markup

#from ..models import Department, Role, Employee, Product
from ..models import *


# from flask_wtf.file import FileField, FileAllowed, FileRequired
# from .. import images

def choice_query():
    return Employee.query

class ItemForm(FlaskForm):
    """
    Form for CRM
    """
    tag            = SelectField(
        'Choose the Tag Type',
        choices=[('-- Tag --', '-- Tag --'),('Follow Up', 'Follow Up'), 
        ('Hot', 'Hot'), ('Soon', 'Soon'),('Upsale', 'Upsale')])
    company_name   = StringField('Name', validators=[DataRequired()], 
        render_kw={"placeholder": "Client\'s Name"})
    email     = StringField('Email', validators=[DataRequired(), Email()], 
        render_kw={"placeholder": "Client\'s Email"})
    website   = StringField('Website', validators=[DataRequired()], 
        render_kw={"placeholder": "Client\'s Website"})
    address   = StringField('Address', validators=[DataRequired()], 
        render_kw={"placeholder": "Client\'s Address"})
    contact_type   = SelectField(
        'Choose the Company\'s Contact Type',
        choices=[('-- Contact Type --', '-- Contact Type --'), ('Potential Customer', 'Potential Customer'),
        ('All', 'All'), ('Current Customer', 'Current Customer'), ('Best Teammate', 'Best Teammate')])
    phone_number   = StringField('Phone Number', validators=[DataRequired()], 
        render_kw={"placeholder": "Phone Number"})
    city           = StringField('City', validators=[DataRequired()], 
        render_kw={"placeholder": "City"})
    country        = StringField('', validators=[DataRequired()], 
        render_kw={"placeholder": "Country"})
    employee_id       = QuerySelectField('Assignee',
        query_factory=choice_query, allow_blank=False, get_label= 'username')
    description    = StringField('Description', validators=[DataRequired()], 
        render_kw={"placeholder": "Description"})
    status         = SelectField(
        'Choose the Activity Status',
        choices=[('-- Status --', '-- Status --'), ('Done', 'Done'),
        ('In progress', 'In progress'), ('Unstarted', 'Unstarted')])

    submit = SubmitField('INJIZA')