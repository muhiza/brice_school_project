from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, IntegerField, TextAreaField, FileField, DateTimeField, SelectField, SubmitField, FloatField, ValidationError
from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional

#from ..models import Department, Role, Employee, Product
from ..models import *


from flask_wtf.file import FileField, FileAllowed, FileRequired
from .. import images






class intekoRusangeForm(FlaskForm):
    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])
    ibyizweho = SelectField(
        'Status',
        choices=[('Not Started', 'Not Started'), ('In Progress', 'In progress'), ('Decided', 'Decided')])
    decision1 =  StringField("Decision", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    owner1 = StringField("Ibyemezo", validators=[DataRequired()])
    stakeholders1 = StringField("Abitabiriye Inama", validators=[DataRequired()])
    due_date1    =  DateField("Talika",format='%Y-%m-%d', validators=[DataRequired()])
    background1  =  StringField("Ubusobanuro burambuye", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])

    submit      =  SubmitField('Emeza')




class inamaUbuyoboziForm(FlaskForm):
    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])
    status = SelectField(
        'Status',
        choices=[('Not Started', 'Not Started'), ('In Progress', 'In progress'), ('Decided', 'Decided')])
    decision =  StringField("Decision", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    owner = decision =  StringField("Decision", validators=[DataRequired()])
    stakeholders = StringField("Stakeholders", validators=[DataRequired()])
    due_date    =  DateField("Due date",format='%Y-%m-%d', validators=[DataRequired()])
    background  =  StringField("Background", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])

    submit      =  SubmitField('Emeza')





class ubugenzuziForm(FlaskForm):
    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])
    status = SelectField(
        'Status',
        choices=[('Not Started', 'Not Started'), ('In Progress', 'In progress'), ('Decided', 'Decided')])
    decision =  StringField("Decision", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    owner = StringField("Decision", validators=[DataRequired()])
    stakeholders = StringField("Stakeholders", validators=[DataRequired()])
    due_date    =  DateField("Due date",format='%Y-%m-%d', validators=[DataRequired()])
    background  =  StringField("Background", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])

    submit      =  SubmitField('Emeza')






"""
class isandukuForm(FlaskForm):
    
    no =  StringField("Nimero y'igikorwa", validators=[DataRequired()])
    done_date = DateField("Tariki byakoreweho",format='%Y-%m-%d', validators=[DataRequired()])
    action    =  StringField("Igikorwa", validators=[DataRequired()])
    income  =  StringField("Amafaranga yinjiye", validators=[DataRequired()])
    expense  =  StringField("Amafaranga Asohotse", validators=[DataRequired()])
    remain  =  StringField("Amafaranga Asigaye", validators=[DataRequired()])
    done_by  =  StringField("Umukono / Uyatanze ", validators=[DataRequired()])
    done_to  =  StringField("Umukono / Uyakiriye", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])
    submit      =  SubmitField('Emeza')

"""



class MemberForm(FlaskForm):
    firstName =  StringField("Izina ribanza", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Izina ribanza"})
    secondName =  StringField("Izina rikurikira", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Izina rikurikira"})
    others =  StringField("Ayandi (Singombwa)", render_kw={"placeholder": "Ayandi (Singombwa)"})
    District =  StringField("Akarere", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Akarere"})
    Sector =  StringField("Umurenge", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umurenge"})
    Cell =  StringField("Akagari", validators=[DataRequired()], render_kw={"placeholder": "Injizamo akagari"})
    nId =  StringField("Nimero ndangamuntu", validators=[DataRequired()], render_kw={"placeholder": "Injiza Nimero y'indangamuntu"})
    entryDate =  DateField("Tariki yinjiriyemo",format='%Y-%m-%d', validators=[DataRequired()])
    share =  StringField("Umugabane", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umugabane"})
    exitDate =  DateField("Tariki yasohokeyemo",format='%Y-%m-%d', validators=[DataRequired()])
    umuzungura =  StringField("Umuzungura", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umuzungura"})
    umukono =  StringField("Umukono", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umukono"})
    gender = SelectField(
        'Igitsina',
        choices=[('Igitsina', 'Igitsina'), ('Gabo', 'Gabo'), ('Gole', 'Gole'), ('Ibindi', 'Ibindi')])
    dob     =  DateField("Tariki y'amavuko", format='%Y-%m-%d', validators=[DataRequired()])  
    phone = StringField("Nimero ya telephone", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo numero ya telephone"})
    
    
    """
    Current Comment
    ==========================
    #owner    =  StringField("Owner", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    """
    submit      =  SubmitField('Injiza Umunyamuryango')




class umusaruroForm(FlaskForm):
    
    Amazina =  StringField("Amazina y'umusaruro winjiye", validators=[DataRequired()])
    Taliki = DateField("Tariki winjiriyeho",format='%Y-%m-%d', validators=[DataRequired()])
    Uwagemuye    =  StringField("Amazina y'uwagemuye umusaruro", validators=[DataRequired()])
    Ibiro  =  StringField("Ingano y'ibiro byagemuwe", validators=[DataRequired()])
    Igiciro  =  StringField("Igiciro byagemuweho", validators=[DataRequired()])
    IkiguziCyose  =  StringField("Ikiguzi cyose cyatanzwe", validators=[DataRequired()])
    amafarangaYishyuweKuKiro  =  StringField("Amafaranga yatanzwe ku kiro ", validators=[DataRequired()])
    done_by  =  StringField("Umukono / Uyakiriye", validators=[DataRequired()])
    done_to  =  StringField("Umukono / Uwagemuye", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])
    submit      =  SubmitField('Emeza')


class ibitaboBankForm(FlaskForm):
    No =  StringField("Amazina y'umusaruro winjiye", validators=[DataRequired()])
    Date = DateField("Tariki winjiriyeho",format='%Y-%m-%d', validators=[DataRequired()])
    Igikorwa    =  StringField("Amazina y'uwagemuye umusaruro", validators=[DataRequired()])
    Debit  =  StringField("Ingano y'ibiro byagemuwe", validators=[DataRequired()])
    Credit  =  StringField("Igiciro byagemuweho", validators=[DataRequired()])
    Solde  =  StringField("Ikiguzi cyose cyatanzwe", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])
    submit      =  SubmitField('Emeza')


class amatsindaForm(FlaskForm):
    name = StringField("Injiza izina ry'itsinda", validators=[DataRequired()])
    description = StringField("Tanga ubusobanuro bw'itsinda", validators=[DataRequired()])
    purpose = StringField("Impamvu")
    submit = SubmitField('Kora itsinda')


class IsandukuForm(FlaskForm):
    itariki = DateField("Tariki byakoreweho",format='%Y-%m-%d', validators=[DataRequired()])
    impamvu = StringField("Impamvu", validators=[DataRequired()], render_kw={"placeholder": "Ubusobanuro"})
    piyesi = IntegerField("Piyesi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Piyesi"})
    ayinjiye = IntegerField("Ayinjiye", validators=[DataRequired()], render_kw={"placeholder": "ayinjiye"})
    ayasohotse = IntegerField("Ayasohotse", validators=[DataRequired()], render_kw={"placeholder": "ayasohotse"})
    asigaye = IntegerField("Ayasigaye", validators=[Optional()], render_kw={"placeholder": "asigaye"})
    submit = SubmitField('Bika')

class BankForm(FlaskForm):
    itariki = DateField("Tariki byakoreweho",format='%Y-%m-%d', validators=[DataRequired()])
    impamvu = StringField("Impamvu", validators=[DataRequired()], render_kw={"placeholder": "Ubusobanuro"})
    piyesi = StringField("Piyesi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Piyesi"})
    ayinjiye = IntegerField("Ayo Binjije", validators=[DataRequired()], render_kw={"placeholder": "Injiza ayinjiye"})
    ayasohotse = IntegerField("Ayo Basohoye", validators=[DataRequired()], render_kw={"placeholder": "Injiza ayasohotse"})
    submit = SubmitField('Bika')

class InguzanyoZatanzweForm(FlaskForm):
    """docstring for InguzanyoZatanzwe"""
    itariki = DateField("Tariki byakoreweho",format='%Y-%m-%d', validators=[DataRequired()])
    impamvu = StringField("Impamvu", validators=[DataRequired()], render_kw={"placeholder": "Ubusobanuro"})
    piyesi = StringField("Piyesi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Piyesi"})
    ayinjiye = IntegerField("Ayo Binjije", validators=[DataRequired()])
    ayasohotse = IntegerField("Ayo Basohoye", validators=[DataRequired()])
    submit = SubmitField('Bika')

class IbirambaForm(FlaskForm):
    """docstring for IbirambaForm"""
    itariki = DateField("Tariki byakoreweho",format='%Y-%m-%d', validators=[DataRequired()])
    impamvu = StringField("Impamvu", validators=[DataRequired()], render_kw={"placeholder": "Ubusobanuro"})
    piyesi = StringField("Piyesi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Piyesi"})
    ayinjiye = IntegerField("Ayo Binjije", validators=[DataRequired()])
    ayasohotse = IntegerField("Ayo Basohoye", validators=[DataRequired()])
    submit = SubmitField('Bika')

class UbubikoForm(FlaskForm):
    """docstring for UbubikoForm"""
    itariki = DateField("Tariki byakoreweho",format='%Y-%m-%d', validators=[DataRequired()])
    impamvu = StringField("Impamvu", validators=[DataRequired()], render_kw={"placeholder": "Ubusobanuro"})
    piyesi = StringField("Piyesi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Piyesi"})
    ayinjiye = IntegerField("Ayo Binjije", validators=[DataRequired()])
    ayasohotse = IntegerField("Ayo Basohoye", validators=[DataRequired()])
    submit = SubmitField('Bika')

class UmugabaneShingiroForm(FlaskForm):
    itariki = DateField("Tariki byakoreweho",format='%Y-%m-%d', validators=[DataRequired()])
    impamvu = StringField("Impamvu", validators=[DataRequired()], render_kw={"placeholder": "Ubusobanuro"})
    piyesi = StringField("Piyesi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Piyesi"})
    ayinjiye = IntegerField("Ayo Binjije", validators=[DataRequired()])
    ayasohotse = IntegerField("Ayo Basohoye", validators=[DataRequired()])
    submit = SubmitField('Bika')

class InkungaForm(FlaskForm):
    itariki = DateField("Tariki byakoreweho",format='%Y-%m-%d', validators=[DataRequired()])
    impamvu = StringField("Impamvu", validators=[DataRequired()], render_kw={"placeholder": "Ubusobanuro"})
    piyesi = StringField("Piyesi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Piyesi"})
    ayinjiye = IntegerField("Ayo Binjije", validators=[DataRequired()])
    ayasohotse = IntegerField("Ayo Basohoye", validators=[DataRequired()])
    submit = SubmitField('Bika')

class InguzanyoZabandiForm(FlaskForm):
    itariki = DateField("Tariki byakoreweho",format='%Y-%m-%d', validators=[DataRequired()])
    impamvu = StringField("Impamvu", validators=[DataRequired()], render_kw={"placeholder": "Ubusobanuro"})
    piyesi = StringField("Piyesi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Piyesi"})
    ayinjiye = IntegerField("Ayo Binjije", validators=[DataRequired()])
    ayasohotse = IntegerField("Ayo Basohoye", validators=[DataRequired()])
    submit = SubmitField('Bika')

class IbicuruzwaForm(FlaskForm):
    itariki = DateField("Tariki byakoreweho",format='%Y-%m-%d', validators=[DataRequired()])
    impamvu = StringField("Impamvu", validators=[DataRequired()], render_kw={"placeholder": "Ubusobanuro"})
    piyesi = StringField("Piyesi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Piyesi"})
    ayinjiye = IntegerField("Ayo Binjije", validators=[DataRequired()])
    ayasohotse = IntegerField("Ayo Basohoye", validators=[DataRequired()])
    submit = SubmitField('Bika')

class IkoreshwaRyimariForm(FlaskForm):
    itariki = DateField("Tariki byakoreweho",format='%Y-%m-%d', validators=[DataRequired()])
    impamvu = StringField("Impamvu", validators=[DataRequired()], render_kw={"placeholder": "Ubusobanuro"})
    piyesi = StringField("Piyesi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Piyesi"})
    ayinjiye = IntegerField("Ayo Binjije", validators=[DataRequired()])
    ayasohotse = IntegerField("Ayo Basohoye", validators=[DataRequired()])
    submit = SubmitField('Bika')

class IbindiForm(FlaskForm):
    itariki = DateField("Tariki byakoreweho",format='%Y-%m-%d', validators=[DataRequired()])
    impamvu = StringField("Impamvu", validators=[DataRequired()], render_kw={"placeholder": "Ubusobanuro"})
    piyesi = StringField("Piyesi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Piyesi"})
    ayinjiye = IntegerField("Ayo Binjije", validators=[DataRequired()])
    ayasohotse = IntegerField("Ayo Basohoye", validators=[DataRequired()])
    submit = SubmitField('Bika')
        


class UbwisazureForm(FlaskForm):
    AssetDescriptionx = StringField("Ubusobanuro bw'umutungo", validators=[DataRequired()], render_kw={"placeholder": "Ubusobanuro bw'umutungo"})
    costx = IntegerField("Igiciro", validators=[DataRequired()], render_kw={"placeholder": "Igiciro"})
    YearOfPurchasex = DateField("Igihe umutungo waguriweho",format='%Y-%m-%d', validators=[DataRequired()])
    SalvageValuex = IntegerField("Ingano y'amafaranga avaho", validators=[DataRequired()], render_kw={"placeholder": "Ingano y'amafaranga avaho"})
    UsefulLifex = StringField("Igihe umutungo uzamara", validators=[DataRequired()], render_kw={"placeholder": "Igihe umutungo uzamara"})
    Methodx = StringField("Uburyo bwo kugabanya", validators=[DataRequired()], render_kw={"placeholder": "Uburyo bwo kugabanya"})
    submit = SubmitField('Bika')




"""
Forms for the accounting models
These models are for improving the
Accounting activities in cooperatives
In Rwanda.
"""

class IncomeCategoryForm(FlaskForm):
    Category = StringField("Category", validators=[DataRequired()], render_kw={"placeholder": "Enter Category"})
    submit = SubmitField('Submit')

class ExpenseCategoryForm(FlaskForm):
    AccountName = StringField("Account Name", validators=[DataRequired()], render_kw={"placeholder": "Enter Account Name"})
    submit = SubmitField('Submit')

class ExpenseForm(FlaskForm):
    Title = StringField("Title", validators=[DataRequired()], render_kw={"placeholder": "Enter Title"})
    Date = DateField("Date",format='%Y-%m-%d', validators=[DataRequired()])
    Category = StringField("Category", validators=[DataRequired()], render_kw={"placeholder": "Enter Category"})
    Account = StringField("Account", validators=[DataRequired()], render_kw={"placeholder": "Enter Account"})
    Amount = IntegerField("Amount", validators=[DataRequired()], render_kw={"placeholder": "Enter Amount"})
    Desciption = StringField("Description", validators=[DataRequired()], render_kw={"placeholder": "Enter Description"})
    submit = SubmitField('Submit')


class IncomeForm(FlaskForm):
    Title = StringField("Title", validators=[DataRequired()], render_kw={"placeholder": "Enter Title"})
    Date = DateField("Date",format='%Y-%m-%d', validators=[DataRequired()])
    Category = StringField("Category", validators=[DataRequired()], render_kw={"placeholder": "Enter Category"})
    Account = StringField("Account", validators=[DataRequired()], render_kw={"placeholder": "Enter Account"})
    Amount = IntegerField("Amount", validators=[DataRequired()], render_kw={"placeholder": "Enter Amount"})
    Desciption = StringField("Description", validators=[DataRequired()], render_kw={"placeholder": "Enter Description"})
    submit = SubmitField('Submit')



class BudgetForm(FlaskForm):
    Category = StringField("Category", validators=[DataRequired()], render_kw={"placeholder": "Enter Category"})
    Date = DateField("Date",format='%Y-%m-%d', validators=[DataRequired()])
    Amount = IntegerField("Amount", validators=[DataRequired()], render_kw={"placeholder": "Enter amount"})
    submit = SubmitField('Submit')

class AssetsForm(FlaskForm):
    Date = DateField("Date",format='%Y-%m-%d', validators=[DataRequired()])
    Category = StringField("Category", validators=[DataRequired()], render_kw={"placeholder": "Enter Category"})
    Account = StringField("Account", validators=[DataRequired()], render_kw={"placeholder": "Enter Account"})
    Amount = IntegerField("Amount", validators=[DataRequired()], render_kw={"placeholder": "Enter Amount"})
    Description = StringField("Description", validators=[DataRequired()], render_kw={"placeholder": "Enter Description"})
    submit = SubmitField('Bika')

class AccountForm(FlaskForm):
    AccountName = StringField("Account Name", validators=[DataRequired()], render_kw={"placeholder": "Enter Account Name"})
    Description = StringField("Description", validators=[DataRequired()], render_kw={"placeholder": "Enter Description"})
    submit = SubmitField('Bika')


    