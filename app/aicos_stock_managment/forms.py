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
	NPKkg = FloatField("DAP & NPK", validators=[DataRequired()], render_kw={"placeholder":"Injiza DAP and NPK (kg)"})
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
    RiceAmount = SelectField(
        'Igiciro Cy\'umuceri',
        choices=[('295', 295), ('305', 305)])
    UwoAsigaranye =  IntegerField("Umuceri asigaranye", validators=[Optional()], render_kw={"placeholder": "Ibiro by'umuceriri asigaranye"})
    Gutonoza  = SelectField(
        'Igiciro Cyo Gutonoza',
        choices=[('45', 45), ('50', 50)])
    submit      =  SubmitField('Emeza')




class InyongeraMusaruroForm(FlaskForm):
    NPKkg = FloatField("NPK", validators=[Optional()], render_kw={"placeholder":"Injiza ibiro bya NPK"})
    NPKPerUnity = SelectField("Igiciro ku kiro cya NPK", choices=[('490',490)], validators=[Optional()])
    UREA = FloatField("UREA", validators=[Optional()], render_kw={"placeholder":"Injiza ibiro bya UREA"})
    UREAPerUnity = SelectField("Igiciro ku kiro cya UREA", choices=[('340',340)], validators=[Optional()])
    DAP = FloatField("DAP", validators=[Optional()], render_kw={"placeholder":"Injiza ibiro bya DAP"})
    DAPPerUnity = SelectField("Igiciro ku kiro cya DAP", choices=[('430',430)], validators=[Optional()])
    KCL = FloatField("KCL", validators=[Optional()], render_kw={"placeholder":"Injiza ibiro bya KCL"})
    KCLPerUnity = SelectField("Igiciro ku kiro cya KCL", choices=[('395',395)], validators=[Optional()])
    Briquette = FloatField("Briquette", validators=[Optional()], render_kw={"placeholder":"Injiza ibiro bya Briquette"})
    BriquettePerUnity = SelectField("Igiciro ku kiro cya Briquette", choices=[('400',400)], validators=[Optional()])
    Cypemetrine =  IntegerField("Cypemetrine", validators=[Optional()], render_kw={"placeholder": "Cypemetrine"})
    Beam =  IntegerField("Beam", validators=[Optional()], render_kw={"placeholder": "Beam"})
    ImbutoQuantity =  IntegerField("Imbuto", validators=[Optional()], render_kw={"placeholder": "Injiza ingano y'imbuto"})
    ImbutoAmount = SelectField("Igiciro cy'imbuto ku kiro", choices=[('400',400)], validators=[Optional()])
    Redevance      = IntegerField("Redevance", validators=[Optional()], render_kw={"placeholder": "Redevance"})
    umwakaWisarura = SelectField("Umwaka W'isarura", choices=[('2018A','2018A')], validators=[Optional()])
    submit      =  SubmitField('Emeza')




class UmusanzuForm(FlaskForm):
    UmusanzuCoop = IntegerField("Umusanzu Wa koperative", validators=[Optional()], render_kw={"placeholder": "Injiza Umusanzu Wa koperative"})
    UmusoroWakarere = IntegerField("Umusoro W'Akarere", validators=[Optional()], render_kw={"placeholder": "Injiza Umusoro W'akarere"})
    Umugabane = IntegerField("Umugabane", validators=[Optional()], render_kw={"placeholder": "Injiza Umugabane Y'atanze"})
    Ikigega = IntegerField("Ikigega", validators=[Optional()], render_kw={"placeholder": "Injiza Amafaranga Y'ikigega"})
    KuzibaIcyuho = IntegerField("Kuziba Icyuho", validators=[Optional()], render_kw={"placeholder": "Injiza Amafaranga yo Kuziba Icyuho"})
    submit      =  SubmitField('Emeza')



class IbiraraneForm(FlaskForm):
    NPKPerUnity = SelectField("Igiciro ku kiro cya NPK", choices=[('490',490)], validators=[Optional()])
    UREA = FloatField("UREA (Ibirarane)", validators=[Optional()], render_kw={"placeholder":"Injiza ibirarane bya UREA (ibiro)"})
    UREAPerUnity = SelectField("Igiciro ku kiro cya UREA", choices=[('340',340)], validators=[Optional()])
    DAP = FloatField("DAP (Ibirarane)", validators=[Optional()], render_kw={"placeholder":"Injiza ibirarane bya DAP (ibiro)"})
    DAPPerUnity = SelectField("Igiciro ku kiro cya DAP", choices=[('430',430)], validators=[Optional()])
    KCL = FloatField("KCL (Ibirarane)", validators=[Optional()], render_kw={"placeholder":"Injiza ibirarane bya KCL (ibiro)"})
    KCLPerUnity = SelectField("Igiciro ku kiro cya KCL", choices=[('395',395)], validators=[Optional()])
    Briquette = FloatField("Briquette", validators=[Optional()], render_kw={"placeholder":"Injiza ibiro bya Briquette"})
    BriquettePerUnity = SelectField("Igiciro ku kiro cya Briquette", choices=[('400',400)], validators=[Optional()])
    ImbutoQuantity =  IntegerField("Imbuto (Ibirarane)", validators=[Optional()], render_kw={"placeholder": "Injiza ingano y'imbuto"})
    ImbutoAmount = SelectField("Igiciro cy'imbuto ku kiro", choices=[('400',400)], validators=[Optional()])
    IdeniAmount =  IntegerField("Ideni ry'umwaka ushize", validators=[Optional()], render_kw={"placeholder": "Injiza Igiciro cy'ikirarane"})
    NPKkg = FloatField("NPK (Ibirarane)", validators=[Optional()], render_kw={"placeholder":"Injiza ibirarane bya NPK (ibiro)"})
    submit      =  SubmitField('Emeza')



class IbihanoForm(FlaskForm):
    AmandeC =  StringField("Amande C", validators=[Optional()], render_kw={"placeholder": "Injiza izina ry'igihano"})
    AmandeApII =  IntegerField("Amande APII", validators=[Optional()], render_kw={"placeholder": "Injiza Amafaranga"})
    Comment =  TextAreaField("Comment", validators=[Optional()], render_kw={"placeholder": "Comment"})
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
