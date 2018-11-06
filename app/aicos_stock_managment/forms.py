from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, IntegerField, TextAreaField, FileField, DateTimeField, SelectField, SubmitField, FloatField, ValidationError
from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional
from ..models import *


from flask_wtf.file import FileField, FileAllowed, FileRequired


class UmusaruroForm(FlaskForm):
	umwakaWisarura = SelectField("Umwaka W'isarura", choices=[('2018A','2018A')], validators=[Optional()])
	amazina = StringField("amazina", validators=[Optional(), Length(4, 64)])
	resi = IntegerField("Resi", validators=[Optional()], render_kw={"placeholder":"Injiza numero ya resi y'umunyamuryango"})
	zone = StringField("Zone", validators=[Optional()], render_kw={"placeholder":"Injiza Zone"})
	umusaruro = IntegerField("Umusaruro", validators=[Optional()], render_kw={"placeholder":"Injiza Umusaruro Wabonetse wose"})
	umuceriWoKurya = IntegerField("Umuceri Wo Kurya", validators=[Optional()], render_kw={"placeholder":"Injiza Umuceri wo kurya (kg)"})
	igiciroCyaKimwe = SelectField("Igiciro Cya Kimwe(Frw/kg)", choices=[('290','290'),('280','280')], validators=[Optional()])
	umusanzu = SelectField("Umusanzu Ku kiro (Frw/kg)", choices=[('15','15')], validators=[Optional()])
	amafrwYoGutonoza = SelectField("Amafaranga yo gutonoza (Frw/kg)", choices=[('50','50')], validators=[Optional()])
	submit = SubmitField("Injiza Umusaruro")

	"""
	def validate_resi(self, field):
        if Umusaruro.query.filter_by(resi=field.data).first():
        	raise ValidationError('Resi yawe yarakoreshejwe')
    """       
    

class InyongeramusaruroForm(FlaskForm):
	umwakaWisarura = SelectField("Umwaka W'isarura", choices=[('2018A','2018A')], validators=[DataRequired()])
	resi = IntegerField("Resi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Resi y'uwahawe Inyongeramusaruro"})
	briquetteKg = FloatField("Briquette", validators=[DataRequired()], render_kw={"placeholder":"Injiza briquette (kg)"})
	briquettePU = SelectField("Briquette kuri kiro (Frw)", choices=[('390','390')], validators=[DataRequired()])
	DAPandNPKkg = FloatField("DAP & NPK", validators=[DataRequired()], render_kw={"placeholder":"Injiza DAP and NPK (kg)"})
	DAPandNPKpu = SelectField("Igiciro kuri DAP & NPK", choices=[('430','430')], validators=[DataRequired()])
	KCLkg = FloatField("KCL", validators=[DataRequired()], render_kw={"placeholder":"Injiza KCL (kg)"})
	KCLpu = SelectField("Igiciro kuri KCL", choices=[('395','395')], validators=[Optional()])
	ImbutoKg = FloatField("Imbuto", validators=[DataRequired()], render_kw={"placeholder":"Injiza Imbuto (kg)"})
	ImbutoPU = SelectField("Igiciro ku Mbuto", choices=[('400','400')], validators=[DataRequired()])
	ImifukaKg = IntegerField("Imifuka", validators=[NumberRange(min=0, max=500, message="Only from zero to 500")], render_kw={"placeholder":"Injiza Imifuka uko ingana"})
	ImifukaPU = SelectField("Igiciro ku mufuka", choices=[('400','400')], validators=[DataRequired()])
	redevenceUbuso = FloatField("Redevence", validators=[DataRequired()], render_kw={"placeholder":"Injiza redevence ubuso"})
	redevencePU = SelectField("Redevence kuri inite", choices=[('250','250')], validators=[DataRequired()])
	submit = SubmitField("Injiza Inyongeramusaruro")

	def validate_resi(self, field):
		if Inyongeramusaruro.query.filter_by(umusaruro_resi=field.data).first():
			raise ValidationError('Resi yawe yarakoreshejwe')

class IbyakoreshejweForm(FlaskForm):
	resi = IntegerField("Resi", validators=[Optional()], render_kw={"placeholder":"Injiza Resi y'uwahawe Ibyakoreshejwe"})
	beamSup = IntegerField("Beam and Sup", validators=[Optional()], render_kw={"placeholder":"Injiza Beam and Sup"})
	ibihanoCoop = IntegerField("Ibihano bya koperative", validators=[Optional()], render_kw={"placeholder":"Injiza Ibihano by cooperative"})
	APIISAMAKIbihano = IntegerField("ibihano bya APIISAMAK", validators=[Optional()], render_kw={"placeholder":"Injiza Ibihano by APIISAMAK"})
	ibiraraneNPKandUREA = IntegerField("ibirarane bya NPK na UREA", validators=[Optional()], render_kw={"placeholder":"Injiza Ibirarane by NPK na UREA"})
	umusoro = IntegerField("Umusoro", validators=[Optional()], render_kw={"placeholder":"Injiza umusoro watanzwe"})
	kwishyuraItsinda = IntegerField("Kwishyura itsinda", validators=[Optional()], render_kw={"placeholder":"Injiza Ubwishyu bw'itsinda"})
	Sheeting = IntegerField("Kwishyura itsinda", validators=[Optional()], render_kw={"placeholder":"Injiza Ubwishyu bw'itsinda"})
	PIS = IntegerField("P/S", validators=[Optional()], render_kw={"placeholder":"Injiza P|S"})
	umuceriYagurijweUmwakaKUshize = IntegerField("Umuceri Yagurijwe ubushize", validators=[Optional()], render_kw={"placeholder":"Injiza Umuceri yagurijwe Umwaka ushize"})
	ibindi = IntegerField("Ibindi", validators=[Optional()], render_kw={"placeholder":"Injiza Ibindi yasabwe"})
	submit = SubmitField("Injiza Ibyakoreshejwe")

	def validate_resi(self, field):
		if Ibyakoreshejwe.query.filter_by(umusaruro_resi=field.data).first():
			raise ValidationError('Resi yawe yarakoreshejwe')


class KonteZaBankForm(FlaskForm):
	resi = IntegerField("Resi", validators=[Optional()], render_kw={"placeholder":"Injiza Resi y'uwahawe Ibyakoreshejwe"})
	izinaryaNyiriKonte = StringField("Amazina ya nyirayo", validators=[Optional()], render_kw={"placeholder":"Injiza izina rya nyiri konte"})
	izanaRyaBank = StringField("Izina Rya Banki", validators=[Optional()], render_kw={"placeholder":"Injiza izina rya banki"})
	numeroYaKonte = StringField("No ya Konte", validators=[Optional()], render_kw={"placeholder":"Injiza nimero ya konte"})
	submit = SubmitField("Injiza Konte")



# These are forms for new Models. from muhiza
class UmusarurobForm(FlaskForm):
    RiceType = SelectField(
        'Ubwoko bw\'umusaruro',
        choices=[('Umusaruro short', 'Umusaruro short'), ('Umusaruro long', 'Umusaruro long')])
    Quantity =  IntegerField("Ingano y\'umusaruro", validators=[DataRequired()], render_kw={"placeholder": "Injiza ingano y'umusaruro"})
    RiceAmount =  IntegerField("Igiciro", validators=[DataRequired()], render_kw={"placeholder": "Injiza Igiciro cy'umusaruro"})
    UwoAsigaranye =  IntegerField("Uwo asigaranye", validators=[DataRequired()], render_kw={"placeholder": "Uwo asigaranye"})
    Gutonoza      = IntegerField("Gutonoza", validators=[DataRequired()], render_kw={"placeholder": "Amafaranga yo gutonoza"})
    submit      =  SubmitField('Emeza')




class InyongeraMusaruroForm(FlaskForm):
    InyongeraMusaruroType = SelectField(
        'Ubwoko bw\'inyongeramusaruro',
        choices=[('DAP', 'DAP'), ('KCL', 'KCL'), ('NPK', 'NPK'), ('UREA', 'UREA')])
    Quantity =  FloatField("Ingano y\'Inyongera musaruro", validators=[Optional()], render_kw={"placeholder": "Injiza ingano y'inyongera musaruro"})    
    Amount =  IntegerField("Igiciro", validators=[Optional()], render_kw={"placeholder": "Injiza Igiciro cy'inyongera musaruro"})
    Cypemetrine =  IntegerField("Cypemetrine", validators=[Optional()], render_kw={"placeholder": "Cypemetrine"})
    Beam =  IntegerField("Beam", validators=[Optional()], render_kw={"placeholder": "Beam"})
    ImbutoQuantity =  IntegerField("Imbuto", validators=[Optional()], render_kw={"placeholder": "Injiza ingano y'imbuto"})
    ImbutoAmount =  IntegerField("Imbuto amount", validators=[Optional()], render_kw={"placeholder": "Injiza igiciro cy'imbuto"})
    Redevance      = IntegerField("Redevance", validators=[Optional()], render_kw={"placeholder": "Redevance"})
    umwakaWisarura = SelectField("Umwaka W'isarura", choices=[('2018A','2018A')], validators=[Optional()])
    submit      =  SubmitField('Emeza')




class UmusanzuForm(FlaskForm):
    UmusanzuType = SelectField(
        'Ubwoko bw\'umusanzu',
        choices=[('Umusanzu Wa Coop', 'Umusanzu Wa Coop'), ('Umusoro Akarere', 'Umusoro Akarere'), ('Umugabane', 'Umugabane'), ('Ikigega', 'Ikigega'), ('Kuziba Icyuho', 'Kuziba Icyuho')])
    Amount =  IntegerField("Igiciro", validators=[Optional()], render_kw={"placeholder": "Injiza Igiciro cy'inyongera musaruro"})
    Comment =  StringField("Comment", validators=[Optional()], render_kw={"placeholder": "Comment"})
    submit      =  SubmitField('Emeza')



class IbiraraneForm(FlaskForm):
    IbiraraneType = SelectField(
        'Ubwoko bw\'ibirarane',
        choices=[('DAP', 'DAP'), ('KCL', 'KCL'), ('NPK', 'NPK'), ('UREA', 'UREA'), ('IMBUTO', 'IMBUTO')])
    IdeniTime =  StringField("Igihe", validators=[Optional()], render_kw={"placeholder": "Injiza Igihe"})
    IdeniAmount =  StringField("Amafaranga", validators=[Optional()], render_kw={"placeholder": "Injiza Igiciro cy'ikirarane"})
    IdeniQuantity =  StringField("Ingano", validators=[Optional()], render_kw={"placeholder": "Injiza Ingano y'ikirarane"})
    
    Comment =  StringField("Comment", validators=[Optional()], render_kw={"placeholder": "Comment"})
    submit      =  SubmitField('Emeza')



class IbihanoForm(FlaskForm):
    Igihano =  StringField("Igihano", validators=[DataRequired()], render_kw={"placeholder": "Injiza izina ry'igihano"})
    IgihanoAmount =  IntegerField("Afaranga", validators=[DataRequired()], render_kw={"placeholder": "Injiza Amafaranga"})
    Comment =  TextAreaField("Comment", validators=[DataRequired()], render_kw={"placeholder": "Comment"})
    submit =  SubmitField('Emeza')




class IbindiForm(FlaskForm):
    ImifukaQuantity =  IntegerField("Imifuka", validators=[Optional()], render_kw={"placeholder": "Injiza umubare w'imifuka"})
    ImifukaAmount =  IntegerField("igiciro", validators=[Optional()], render_kw={"placeholder": "Injiza Amafaranga"})
    MituelleAmount =  IntegerField("Mituelle", validators=[Optional()], render_kw={"placeholder": "Injiza amafaranga ya mituelle"})
    UmuceriGrade =  IntegerField("Umuceri Grade", validators=[Optional()], render_kw={"placeholder": "Injiza Amafaranga"})
    UmuceriQuantity =  IntegerField("Ubwinshi", validators=[Optional()], render_kw={"placeholder": "Injiza Quantity ya Grade"})
    UmuceriAmountGrade =  IntegerField("Amount", validators=[Optional()], render_kw={"placeholder": "Injiza Amafaranga y'umuceri wa Grade"})
    Avence =  IntegerField("Avance", validators=[Optional()], render_kw={"placeholder": "Injiza Amafaranga y avance"})
    submit      =  SubmitField('Emeza')
