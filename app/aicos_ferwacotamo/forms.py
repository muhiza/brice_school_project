from flask_wtf import FlaskForm

from flask_login import login_required, current_user
from wtforms import StringField, TextAreaField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import *
from .. import *

from markupsafe import Markup

Kigali_City=['','Nyarugenge', 'Gasabo', 'Kicukiro']
East=['','Kayonza', 'Kirehe', 'Ngoma', 'Bugesera', 'Nyagatare', 'Gatsibo']
South=['','Kamonyi', 'Ruhango', 'Muhanga', 'Nyanza', 'Huye', 'Nyaruguru', 'Nyamagabe', 'Gisagara']
North=['','Rulindo', 'Burera', 'Burera', 'Gakenke', 'Gicumbi', 'Musanze']
West=['','Karongi','Ngororero','Nyabihu', 'Nyamasheke', 'Rubavu', 'Rusizi', 'Rutsiro']

Provinces={
    'Kigali_City':Kigali_City,
    'East':East,
    'South':South,
    'North':North,
    'West':West
}
class FederationForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    Code = StringField(u'Code ya Federation', validators=[DataRequired()], render_kw={"placeholder": "Injiza Code ya Federation"})
    Name = StringField(u'Izina rya Federation', validators=[DataRequired()], render_kw={"placeholder": "Injiza izina rya Federation"})
    RegDate = StringField(u'Igihe Federation yandikiwe', validators=[DataRequired()], render_kw={"placeholder": "Injiza italiki yandikiweho"})
    Certificate = StringField(u'Certificate ya Federation', validators=[DataRequired()], render_kw={"placeholder": "Shyiramo certificate ya Federation"})
    Province = SelectField(
        'Intara Federation ibarizwamo',
        choices=[('', ''),('Kigali_City', 'Kigali_City'), 
        ('East', 'East'), ('West', 'West'),
        ('North', 'North'), ('South', 'South')],id='Province')

    District = SelectField(
        'Akarere Federation ibarizwamo',
        choices=[],id='District'
        )
    Sector = StringField('Injiza umurenge Federation ibarizwamo', validators=[DataRequired()], render_kw={"placeholder": "Injiza umurenge Federation ibarizwamo"})
    Cell = StringField('Injiza akagari Federation ibarizwamo', validators=[DataRequired()], render_kw={"placeholder": "Injiza akagari Federation ibarizwamo"})
    startingShare = StringField('Umugabane Shingiro', validators=[DataRequired()], render_kw={"placeholder": "Umugabane Shingiro wo Kwinjira muri Cooperative"})
    Field = SelectField(
        'Hitamo umurimo Federation ikora',
        choices=[('Umurimo Federation ikora', 'Umurimo Federation ikora'),('Ubuhinzi bw\'Icyayi', 'Ubuhinzi bw\'Icyayi'), 
        ('Ubucukuzi', 'Ubucukuzi'), ('Ubworozi', 'Ubworozi'),
        ('Ubuhinzi bwa Kawa', 'Ubuhinzi bwa Kawa'), ('Ubuhinzi bw\'Imyumbati', 'Ubuhinzi bw\'Imyumbati'),
        ('Ubuhinzi bw\'Ibirayi', 'Ubuhinzi bw\'Ibirayi'), ('Gutwara moto', 'Gutwara Moto'),
        ('Ubuvumvu', 'Ubuvumvu'), ('Ubuhinzi bw\'Ibireti', 'Ubuhinzi bw\'Ibireti'),
        ('Ubuhinzi bw\'Umuceri', 'Ubuhinzi bw\'Umuceri'), ('Gutwara imodoka', 'Gutwara imodoka'),
        ('Ubuhinzi bw\'Ibigori', 'Ubuhinzi bw\'Ibigori'), ('Uburobyi', 'Uburobyi'),
        ('Ubuhinzi bw\'Indabo', 'Ubuhinzi bw\'Indabo'), ('Kuboha', 'Kuboha')])

    Confederation = SelectField(
        'Hitamo Komfederasiyo ya Federation',
        choices=[])

    # Federation = SelectField(
    #     'Hitamo Federation Federation ibarizwamo',
    #     choices=[('Hitamo Federation Federation ibarizwamo', 'Hitamo Federation Federation ibarizwamo'),('UCTHEN', 'UCTHEN'), 
    #     ('UCTCCN', 'UCTCCN'), ('UCOTHENYU', 'UCOTHENYU'),
    #     ('UCOTHEI', 'UCOTHEI'), ('UCOTHESN', 'UCOTHESN')])
    Description = TextAreaField('Ubundi busobanuro bwa Federation (Si ngombwa)', render_kw={"placeholder": "Ubundi busobanuro bwa Federation (Si ngombwa)"})
    submit = SubmitField('Injiza muri sisiteme')


class newFederationForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    Name = StringField(Markup('<b>Izina rya Federation</b>'), validators=[DataRequired()], render_kw={"placeholder": "Injiza izina rya Federation"})
    Province = SelectField(
        Markup('<b>Intara Federation ibarizwamo</b>'),
        choices=[('', ''),('Kigali_City', 'Kigali_City'), 
        ('East', 'East'), ('West', 'West'),
        ('North', 'North'), ('South', 'South')],id='Province')

    District = SelectField(
        Markup('<b>Akarere Federation ibarizwamo</b>'),
        choices=[],id='District')
    Sector = StringField(Markup('<b>Injiza umurenge Federation ibarizwamo</b>'), validators=[DataRequired()], render_kw={"placeholder": "Injiza umurenge Federation ibarizwamo"})
    Cell = StringField(Markup('<b>Injiza akagari Federation ibarizwamo</b>'), validators=[DataRequired()], render_kw={"placeholder": "Injiza akagari Federation ibarizwamo"})
    startingSharex = StringField(Markup('<b>Umugabane Shingiro</b>'), validators=[DataRequired()], render_kw={"placeholder": "Umugabane Shingiro wa Cooperative"})
    sharePerPerson = StringField(Markup('<b>Umugabane Kuri buri munyamuryango</b>'), validators=[DataRequired()], render_kw={"placeholder": "Umugabane Shingiro wo Kwinjira muri Cooperative"})
    maleMembers = StringField(Markup('<b>Abanyamuryango b\'abagabo</b>'), validators=[DataRequired()], render_kw={"placeholder": "Umubare w\'Abanyamuryango b\'abagabo"})
    femaleMembers = StringField(Markup('<b>Abanyamuryango b\'abagore</b>'), validators=[DataRequired()], render_kw={"placeholder": "Umubare w\'Abanyamuryango b\'abagore"})

    Activity = SelectField(
        Markup('<b>Icyo Federation Ikora</b>'),
        choices=[('Tea', 'Tea'),('Coffee', 'Coffee'), 
        ('Rice', 'Rice')])

    Confederation = SelectField(
        'Hitamo Komfederasiyo ya Federation',
        choices=[])

    
    submit = SubmitField('Injiza muri sisiteme')
