from flask import render_template, abort, flash, redirect, url_for, request
from . import aicos_req
from flask_login import current_user, login_required
from sqlalchemy import func
from ..models import * 
from .forms import *

from datetime import datetime,date,time
import calendar

import flask_excel
import flask_excel as excel

import nexmo

import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)





client = nexmo.Client(key='e7096025', secret='ab848459dae27b51')



def check_admin():
    #form = LoginForm()
    # departments = Employee.query.filter_by(email=form.email.data).first()
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        #if not current_user.
        abort(403)


def check_overall():
    if not current_user.is_overall:
        abort(403)




def check_coop_admin():
    if not current_user.is_coop_admin:
        abort(403)

@aicos_req.route('/')
def dashboardqw():
    return render_template('homereq.html')


@aicos_req.route('/governanceBooks')
def governanceBooks():
    return render_template('governanceBooks/governanceBook.html')





@aicos_req.route('/accountingBooks')
def accountingBooks():
    return render_template('accountingBooks/accountingBook.html')




@aicos_req.route('/legalBooks')
def legalBooks():
    return render_template('legalBooks/legalBook.html')


@aicos_req.route('/planningBooks')
def planningBooks():
    return render_template('planningBooks/planningBook.html')




@aicos_req.route('/specialReports')
def specialReports():
    return render_template('specialReports/specialReport.html')


@aicos_req.route('/Production')
def Production():
    return render_template('accountingBooks/production.html')





# Listing all from governanceBooks block.
@aicos_req.route('/cooperative/intekoRusangeList')
def intekoRusangeList():
    intekoRusangeList = intekoRusange.query.all()
    return render_template("governanceBooks/intekoRusangeList.html", intekoRusangeList=intekoRusangeList, title="List y'ibyemezo by'inteko rusange")

@aicos_req.route('/cooperative/inamaUbuyoboziList')
def inamaUbuyoboziList():
    inamaUbuyoboziList = inamaUbuyobozi.query.all()
    return render_template("governanceBooks/inamaUbuyoboziList.html", inamaUbuyoboziList=inamaUbuyoboziList, title="List y'ibyemezo by'inama y'ubuyobozi")

@aicos_req.route('/cooperative/inamaUbugenzuziList')
def ubugenzuziList():
    ubugenzuzi = Ubugenzuzi.query.all()
    return render_template("governanceBooks/ubugenzuziList.html", ubugenzuzi=ubugenzuzi, 
                            title="List y'ibyemezo by'inama y'ubugenzuzi")

# Processing forms on the Governance Block.
# This is the views for adding new inteko rusange meeting notes
@aicos_req.route('/cooperative/ibyemezo_byinama', methods=['GET', 'POST'])
@login_required
def intekoRusangeAdd():
    #check_admin()
    form = intekoRusangeForm()
    if form.validate_on_submit():
        inteko = intekoRusange(
                        status1=form.ibyizweho.data,
                        decision1=form.decision1.data,
                        owner1   = form.owner1.data,
                        stakeholders1=form.stakeholders1.data,
                        due_date1=form.due_date1.data,
                        background1 = form.background1.data,
                        department_id = current_user.email
                        )

        try:
            db.session.add(inteko)
            #db.session.add(notif)
            db.session.commit()
            flash("Umaze kubika neza ibyemezo by'inama")
        except:
            flash("Habayeho ikibazo mu makuru watanze!")
        return redirect(url_for('aicos_req.intekoRusangeList'))
    return render_template("governanceBooks/intekoRusange.html", form=form, title="Create")


# This is the views for adding new inama y'ubuyobozi meeting notes
@aicos_req.route('/cooperative/ibyemezoByinamaUbuyobozi', methods=['GET', 'POST'])
@login_required
def inamaUbuyoboziAdd():
    check_admin()
    form = inamaUbuyoboziForm()
    if form.validate_on_submit():
        inama = inamaUbuyobozi(status=form.status.data,
                        decision=form.decision.data,
                        owner   = form.owner.data,
                        stakeholders=form.stakeholders.data,
                        due_date=form.due_date.data,
                        background = form.background.data,
                        department_id = current_user.email)

        notif = Notification(action="Made decision",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            db.session.add(inama)
            db.session.add(notif)
            db.session.commit()
            flash("Umaze kubika neza ibyemezo by'inama")
        except:
            flash("Habayeho ikibazo mu makuru watanze!")
        return redirect(url_for('aicos_req.inamaUbuyoboziList'))
    return render_template("governanceBooks/inamaUbuyobozi.html", form=form, title="Create")





# This is the views for adding new inama y'ubugenzuzi meeting notes
@aicos_req.route('/cooperative/ibyemezoByinamaUbugenzuzi', methods=['GET', 'POST'])
@login_required
def ubugenzuziAdd(*args, **kwargs):
    check_admin()
    form = ubugenzuziForm()
    if form.validate_on_submit():
        inamaUbugenzuzi = Ubugenzuzi(status=form.status.data,
                        decision=form.decision.data,
                        owner   = form.owner.data,
                        stakeholders=form.stakeholders.data,
                        due_date=form.due_date.data,
                        background = form.background.data,
                        department_id = current_user.email)

        notif = Notification(action="Made decision",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            db.session.add(inamaUbugenzuzi)
            db.session.add(notif)
            db.session.commit()
            flash("Umaze kubika neza ibyemezo by'inama")
        except:
            flash("Habayeho ikibazo mu makuru watanze!")
        return redirect(url_for('aicos_req.ubugenzuziList'))
    return render_template("governanceBooks/ubugenzuzi.html", form=form, title="Create")











# Views which are going to be dealing with Accounting Book.
@aicos_req.route('/abanyamuryangoImigabane', methods=['GET', 'POST'])
def abanyamuryangoImigabane():
    """
    List all employees
    """
    """
    List all employees
    """
    check_admin()
    check_coop_admin()
    #form = LoginForm()
    # if form.validate_on_submit():
        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
    #apps = Department.query.filter_by(email=current_user.email).first()
    #applications = apps.applications
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    employees_count = employee.members.count()

    notes = Notification.query.filter_by(department_id=current_user.email)
    #if employees is not None:
    #employees = Employee.query.filter_by(email=form.email.data)
    return render_template('accountingBooks/imigabane/members_share_capital.html',
                           employees=employees,
                           employee=employee,
                           employees_count=employees_count,
                           notes = notes,
                           title='Employees')


@aicos_req.route('/abanyamuryangoImigabaneDetails/<int:id>', methods=['GET', 'POST'])
@login_required
def abanyamuryangoDetails(id):
    check_admin()
    employee = Member.query.get_or_404(id)
    if employee is not None:
        return render_template("accountingBooks/imigabane/abanyamuryangoImigabaneDetails.html", employee=employee)
    return redirect(url_for('aicos_req.abanyamuryangoImigabane'))













# Kongera umugabane ku munyamuryango.
@aicos_req.route('/cooperative/umugabane/add/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_umugabane(id):
    """
    Edit a role
    """
    check_admin()
    #add_role = False
    member = Member.query.get_or_404(id)
    form = MemberForm(obj=member)
    if form.validate_on_submit():
        member.firstName = form.firstName.data
        member.nId = form.nId.data
        db.session.add(member)
        db.session.commit()
        flash('Umaze kongera umugabane.')
        # redirect to the roles pagess
        return redirect(url_for('aicos_req.abanyamuryangoImigabane'))
    form.firstName.data = member.firstName
    form.nId.data = member.nId
    return render_template('accountingBooks/imigabane/addUmugabane.html', form=form, title="Edit Umugabane")








# Isanguku views are here.
@aicos_req.route('/cooperative/isanduku')
def isandukuList():
    isanduku = Isanduku.query.filter_by().all()
    return render_template("accountingBooks/isanduku/isandukuList.html", isanduku=isanduku, title="List y'ibyemezo by'inteko rusange")



@aicos_req.route('/cooperative/add/Isanduku', methods=['GET', 'POST'])
@login_required
def isandukuAdd():
    check_admin()
    form = isandukuForm()
    if form.validate_on_submit():
        isanduku = Isanduku(

                        no=form.no.data,
                        done_date=form.done_date.data,
                        action=form.action.data,
                        income   = form.income.data,
                        expense   = form.expense.data,
                        remain   = form.remain.data,
                        done_by   = form.done_by.data,
                        done_to   = form.done_to.data,
                        department_id = current_user.email
                        )

        notif = Notification(action="Communication",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            """
            to_number = '+250786012383'
            message = current_user.email + ' Decision has made and you are concerned'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            """

            db.session.add(isanduku)
            db.session.add(notif)
            db.session.commit()
            flash("Wongereye amakuru mu isanduku neza")
        except:
            flash("Error! Invalid information")
        return redirect(url_for('aicos_req.isandukuList'))
    return render_template("accountingBooks/isanduku/isanduku.html", form=form, title="Kongera mu Isanduku.")





# Umusaruro views are here.
@aicos_req.route('/cooperative/Umusaruro')
def umusaruroList():
    umusaruro = Umusaruro.query.all()
    return render_template("accountingBooks/umusaruro/umusaruroList.html", umusaruro=umusaruro, title="List y'umusaruro winjiye")



@aicos_req.route('/cooperative/add/Umusaruro', methods=['GET', 'POST'])
@login_required
def umusaruroAdd():
    check_admin()
    form = umusaruroForm()
    if form.validate_on_submit():
        umusaruro = Umusaruro(
                        Amazina=form.Amazina.data,
                        Taliki=form.Taliki.data,
                        Uwagemuye=form.Uwagemuye.data,
                        Ibiro   = form.Ibiro.data,
                        Igiciro   = form.Igiciro.data,
                        IkiguziCyose   = form.IkiguziCyose.data,
                        amafarangaYishyuweKuKiro   = form.amafarangaYishyuweKuKiro.data,
                        done_by   = form.done_by.data,
                        done_to   = form.done_to.data,
                        department_id = current_user.email
                        )



        notif = Notification(action="Communication",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            """
            to_number = '+250786012383'
            message = current_user.email + ' Decision has made and you are concerned'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            """

            db.session.add(umusaruro)
            db.session.add(notif)
            db.session.commit()
            flash("Winjije neza umusaruro muri Cooperative")
        except:
            flash("Error! Invalid information")
        return redirect(url_for('aicos_req.umusaruroList'))
    return render_template("accountingBooks/umusaruro/umusaruro.html", form=form, title="Kongera umusaruro muri Cooperative.")








# Views for the Wide Cooperative Market.
@aicos_req.route('/cooperatives/wcm')
def wcmIndex():
    umusaruro = Umusaruro.query.all()
    return render_template('accountingBooks/wcm/index.html', umusaruro=umusaruro)




@aicos_req.route('/AccountingBook')
def abishyuye():

    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    employees_count = employee.members.count()


    return render_template('accountingBooks/abishyuye/abishyuyeList.html',
                            employees=employees, title='List yabanyamuryango bishyuye!')









# Views for the Wide Cooperative Market.
@aicos_req.route('/cooperatives/ibitaboBank')
def bankIbitabo():
    bankIbitaboList = ibitaboByaBank.query.all()
    return render_template('accountingBooks/ibitaboBank/ibitaboBankList.html', bankIbitaboList=bankIbitaboList)






# ibitabo bya banks.
@aicos_req.route('/accountingBooks/BankBooks', methods=['GET', 'POST'])
def ibitaboBank():
    form = ibitaboBankForm()
    if form.validate_on_submit():
        ibitabo = ibitaboBank(
                                no = form.No.data,
                                date = form.Date.data,
                                igikorwa = form.Igikorwa.data,
                                debt     = form.Debit.data,
                                credit   = form.Credit.data,
                                solde    = form.Solde.data,
                                department_id = current_user.email)
        try:
            db.session.add(ibitabo)
            db.session.commit()
            flash("Umaze kwinjize igitabo cya bank neza!")
            return redirect(url_for('aicos_req.ibitaboBankList'))
        except:
            flash("Ntabwo igitabo cyabashije kwinjira neza!")
    return render_template('accountingBooks/ibitaboBank/ibitaboBank.html', form=form, title="List y'ibitabo bya banks!")





@aicos_req.route('/cooperatives/accountingBook/BankHistoty')
def bankHistory():
    return render_template('accountingBooks/bankHistory/bankHistory.html')




@aicos_req.route('/cooperatives/accountingBook/signatories')
def signatories():
    return render_template('accountingBooks/bankHistory/signatories.html')

@aicos_req.route('/cooperatives/amatsinda')
def amatsinda():
    amatsinda = Itsinda.query.filter_by(department_id=current_user.email)
    member = ItsindaMember.query.all()
    return render_template('amatsinda/cooperative_groups.html', amatsinda=amatsinda, member=member)


@aicos_req.route('cooperatives/amatsinda/koraitsinda', methods=['GET', 'POST'])
def koraItsinda():

    form = amatsindaForm()

    if form.validate_on_submit():

        itsinda = Itsinda(
                            itsinda_name = form.name.data,
                            description = form.description.data,
                            purpose = form.purpose.data,
                            department_id = current_user.email
                            )

        try:
            db.session.add(itsinda)
            db.session.commit()
            flash("Umaze kwandika neza itsinda")
            return redirect(url_for('aicos_req.amatsinda'))
        except:
            flash("ntabwo itsinda ryanditse neza ongera ugerageze")
            return redirect(url_for('aicos_req.koraItsinda'))

    return render_template('/amatsinda/create_cooperative_group.html', form=form)


@aicos_req.route('/amatsinda/members/<int:id>', methods=['GET', 'POST'])
def amatsindaMembers(id):
    itsinda = Itsinda.query.get_or_404(id)
    itsindaName = Itsinda.query.filter_by(id=itsinda.id).first()
    members = Member.query.all()
    itsindamember = ItsindaMember.query.filter_by(itsinda_id=itsinda.id).all()
    return render_template('/amatsinda/group_members.html', members=members, itsindaName=itsindaName, itsindamember=itsindamember)



@aicos_req.route('/amatsinda/add/members/<int:id>', methods=['GET', 'POST'])
def add_members(id):
    itsinda = Itsinda.query.get_or_404(id)
    itsindaName = Itsinda.query.filter_by(id=itsinda.id).first()
    members = Member.query.all()
    itsindamember = ItsindaMember.query.all()
    return render_template('/amatsinda/add_group_members.html', members=members, itsindaName=itsindaName, itsindamember=itsindamember)

@aicos_req.route('/amatsinda/member/adding/<int:a>/<int:b>', methods=["GET", "POST"])
def ongeramo_member(a, b):
    memberId = Member.query.get_or_404(a)
    itsindaId = Itsinda.query.get_or_404(b)
    itsindaName = Itsinda.query.filter_by(id=itsindaId.id).first()
    member = Member.query.filter_by(id=memberId.id).first()
    members = Member.query.all()
    itsinda = Itsinda.query.filter_by(id=itsindaId.id).first()

    itsindamember = ItsindaMember(
                                member_id=member.id,
                                itsinda_id=itsinda.id,
                                member_firstname=member.izina_ribanza,
                                member_secondname=member.izina_rikurikira,
                                itsinda_name=itsinda.itsinda_name,
                                department_id=current_user.email
                                )
    try:
        db.session.add(itsindamember)
        db.session.commit()
        flash("Umunyamuryango yinjiye neza mwitsinda " + "\"" + itsindaName.itsinda_name + "\"")
        return redirect(url_for('aicos_req.add_members', id=itsinda.id))
    except:
        db.session.rollback()
        flash("Umunyamuryango asanzwe arimo")
        return render_template('/amatsinda/add_itsinda_members.html', members=members, itsindaName=itsindaName)
    return render_template('/amatsinda/add_itsinda_members.html', members=members, itsindaName=itsindaName)
    




@aicos_req.route('/accountingBook/rukomatanyi')
def rukomatanyi():
    rukomatanyo = Rukomatanyo.query.all()
    isanduku = IsandukuNshya.query.filter_by(department_id=current_user.email).all()
    bank = BankModel.query.filter_by(department_id=current_user.email).all()
    inguzanyo_zatanzwe = InguzanyoZatanzwe.query.filter_by(department_id=current_user.email).all()
    ibiramba = Ibiramba.query.filter_by(department_id=current_user.email).all()
    ububiko = Ububiko.query.filter_by(department_id=current_user.email).all()
    umugabane_shingiro = UmugabaneShingiro.query.filter_by(department_id=current_user.email).all()
    inkunga = Inkunga.query.filter_by(department_id=current_user.email).all()
    inguzanyo_abandi = InguzanyoZabandi.query.filter_by(department_id=current_user.email).all()
    ibicuruzwa = Ibicuruzwa.query.filter_by(department_id=current_user.email).all()
    ikoreshwa = IkoreshwaRyimari.query.filter_by(department_id=current_user.email).all()
    isanduku_cr_sum = db.session.query(func.sum(IsandukuNshya.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    isanduku_db_sum = db.session.query(func.sum(IsandukuNshya.asigaye)).filter_by(department_id=current_user.email).scalar()
    bank_cr_sum = db.session.query(func.sum(BankModel.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    bank_db_sum = db.session.query(func.sum(BankModel.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    inguzanyo_db_sum = db.session.query(func.sum(InguzanyoZabandi.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    inguzanyo_cr_sum = db.session.query(func.sum(InguzanyoZabandi.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    ibiramba_cr_sum = db.session.query(func.sum(Ibiramba.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    ibiramba_db_sum = db.session.query(func.sum(Ibiramba.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    ububiko_cr_sum = db.session.query(func.sum(Ububiko.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    ububiko_db_sum = db.session.query(func.sum(Ububiko.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    umugabane_cr_sum = db.session.query(func.sum(UmugabaneShingiro.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    umugabane_db_sum = db.session.query(func.sum(UmugabaneShingiro.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    inkunga_db_sum = db.session.query(func.sum(Inkunga.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    inkunga_cr_sum = db.session.query(func.sum(Inkunga.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    inguzanyo_abandi_cr_sum = db.session.query(func.sum(InguzanyoZabandi.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    inguzanyo_abandi_db_sum = db.session.query(func.sum(InguzanyoZabandi.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    ibindi_cr_sum = db.session.query(func.sum(IbindiRukomatanyi.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    ibindi_db_sum = db.session.query(func.sum(IbindiRukomatanyi.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    return render_template('/accountingBooks/rukomatanyi/index.html', 
                                                                isanduku=isanduku,
                                                                bank=bank,
                                                                isanduku_cr_sum=isanduku_cr_sum,
                                                                isanduku_db_sum=isanduku_db_sum,
                                                                bank_cr_sum = bank_cr_sum,
                                                                bank_db_sum = bank_db_sum,
                                                                inguzanyo_abandi_cr_sum = inguzanyo_abandi_cr_sum,
                                                                inguzanyo_abandi_db_sum = inguzanyo_abandi_db_sum,
                                                                inguzanyo_cr_sum = inguzanyo_cr_sum,
                                                                inguzanyo_db_sum = inguzanyo_db_sum,
                                                                inguzanyo_zatanzwe=inguzanyo_zatanzwe,
                                                                ibiramba_cr_sum = ibiramba_cr_sum,
                                                                ibiramba_db_sum = ibiramba_db_sum,
                                                                ibindi_cr_sum = ibindi_cr_sum,
                                                                ibindi_db_sum = ibindi_db_sum,
                                                                ububiko_db_sum = ububiko_db_sum,
                                                                ububiko_cr_sum = ububiko_cr_sum ,
                                                                inkunga_cr_sum = inkunga_cr_sum,
                                                                inkunga_db_sum = inkunga_db_sum,
                                                                umugabane_cr_sum = umugabane_cr_sum,
                                                                umugabane_db_sum = umugabane_db_sum,
                                                                ibiramba=ibiramba,
                                                                ububiko=ububiko,
                                                                umugabane_shingiro=umugabane_shingiro,
                                                                inkunga=inkunga,
                                                                inguzanyo_abandi=inguzanyo_abandi,
                                                                ibicuruzwa=ibicuruzwa,
                                                                ikoreshwa=ikoreshwa,
                                                                rukomatanyo = rukomatanyo
                                                                )


@aicos_req.route('/accountingBook/rukomatanyi/isanduku')
def isanduku():
    isanduku = IsandukuNshya.query.filter_by(department_id=current_user.email).all()
    rukomatanyo = Rukomatanyo.query.all()
    return render_template('/accountingBooks/rukomatanyi/isanduku.html', isanduku=isanduku, rukomatanyo=rukomatanyo)

@aicos_req.route('/accountingBook/rukomatanyi/isanduku/hindura/<int:id>', methods=["GET", "POST"])
def hinduraIsanduku(id):
    isanduku_id = IsandukuNshya.query.get_or_404(id)
    ibihinduka = IsandukuNshya.query.filter_by(id=isanduku_id.id).first()
    form = IsandukuForm()
    if form.validate_on_submit():
        ibihinduka.ayinjiye = form.ayinjiye.data
        ibihinduka.ayasohotse = form.ayasohotse.data
        try:
            db.session.commit()
            return redirect(url_for('aicos_req.isanduku'))
        except:
            return redirect(url_for('aicos_req.hinduraIsanduku'))
    form.ayinjiye.default = ibihinduka.ayinjiye
    form.ayasohotse.default = ibihinduka.ayasohotse
    form.process()
    return render_template('accountingBooks/rukomatanyi/rukomatanyi_form/hindura_isanduku.html', form=form)


@aicos_req.route('/accountingBook/rukomatanyi/bank')
def bank():
    bank = BankModel.query.filter_by(department_id=current_user.email).all()
    rukomatanyo = Rukomatanyo.query.all()
    return render_template('/accountingBooks/rukomatanyi/bank.html', bank=bank, rukomatanyo=rukomatanyo)

@aicos_req.route('/accountingBook/rukomatanyi/hindura/bank/<int:id>', methods=["GET","POST"])
def hinduraBank(id):
    bankId = BankModel.query.get_or_404(id)
    bank = BankModel.query.filter_by(id=bankId.id).first()
    form = BankForm()
    if form.validate_on_submit():
        bank.ayinjiye = form.ayinjiye.data
        bank.ayasohotse = form.ayasohotse.data
        try:
            db.session.commit()
            return redirect(url_for('aicos_req.bank'))
        except:
            return redirect(url_for('aicos_req.hinduraBank', form=form))
    form.ayinjiye.default = bank.ayinjiye
    form.ayasohotse.default = bank.ayasohotse
    form.process()
    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_bank.html', form=form)


@aicos_req.route('/accountingBook/rukomatanyi/inguzanyo_zatanzwe')
def inguzanyo_zatanzwe():
    inguzanyo_zatanzwe = InguzanyoZatanzwe.query.filter_by(department_id=current_user.email).all()
    rukomatanyo = Rukomatanyo.query.all()
    return render_template('/accountingBooks/rukomatanyi/inguzanyo_zatanzwe.html', inguzanyo_zatanzwe=inguzanyo_zatanzwe, rukomatanyo=rukomatanyo)

@aicos_req.route('/accountingBook/rukomatanyi/hindura/inguzanyo_zatanzwe/<int:id>', methods=["GET", "POST"])
def hinduraInguzanyoZatanzwe(id):
    inguzanyoId = InguzanyoZatanzwe.query.get_or_404(id)
    inguzanyo = InguzanyoZatanzwe.query.filter_by(id=inguzanyoId.id).first()
    form = InguzanyoZatanzweForm()
    if form.validate_on_submit():
        inguzanyo.ayinjiye = form.ayinjiye.data
        inguzanyo.ayasohotse = form.ayasohotse.data
        try:
            db.session.commit()
            return redirect(url_for('aicos_req.inguzanyo_zatanzwe'))
        except:
            return redirect(url_for('aicos_req.hinduraInguzanyoZatanzwe', form=form))
    form.ayinjiye.default = inguzanyo.ayinjiye
    form.ayasohotse.default = inguzanyo.ayasohotse
    form.process()
    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_inguzanyo_zatanzwe.html', form=form)


@aicos_req.route('/accountingBook/rukomatanyi/ibiramba')
def ibiramba():
    ibiramba = Ibiramba.query.filter_by(department_id=current_user.email).all()
    rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    return render_template('/accountingBooks/rukomatanyi/ibiramba.html', ibiramba=ibiramba, rukomatanyo=rukomatanyo)

@aicos_req.route('/accountingBook/rukomatanyi/hindura/ibiramba/<int:id>', methods=["GET", "POST"])
def hinduraIbiramba(id):
    ibirambaId = Ibiramba.query.get_or_404(id)
    ibiramba = Ibiramba.query.filter_by(id=ibirambaId.id).first()
    form = IbirambaForm()
    if form.validate_on_submit():
        ibiramba.ayinjiye = form.ayinjiye.data
        ibiramba.ayasohotse = form.ayasohotse.data
        try:
            db.session.commit()
            return redirect(url_for('aicos_req.ibiramba'))
        except:
            return redirect(url_for('aicos_req.hinduraIbiramba'))
    form.ayinjiye.default = ibiramba.ayinjiye
    form.ayasohotse.default = ibiramba.ayasohotse
    form.process()
    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ibaramba.html', form=form)


@aicos_req.route('/accountingBook/rukomatanyi/ububiko')
def ububiko():
    ububiko = Ububiko.query.filter_by(department_id=current_user.email).all()
    rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    return render_template('/accountingBooks/rukomatanyi/ububiko.html', ububiko=ububiko, rukomatanyo=rukomatanyo)

@aicos_req.route('accountingBook/rukomatanyi/hindura/ububiko/<int:id>', methods=["GET", "POST"])
def hinduraUbubiko(id):
    ububikoId = Ububiko.query.get_or_404(id)
    ububiko = Ububiko.query.filter_by(id=ububikoId.id).first()
    form = UbubikoForm()
    if form.validate_on_submit():
        ububiko.ayinjiye = form.ayinjiye.data
        ububiko.ayasohotse = form.ayasohotse.data
        try:
            db.session.commit()
            return redirect(url_for('aicos_req.ububiko'))
        except:
            return redirect(url_for('aicos_req.hinduraUbubiko', form=form))
    form.ayinjiye.default = ububiko.ayinjiye
    form.ayasohotse.default = ububiko.ayasohotse
    form.process()
    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ububiko.html', form=form)

@aicos_req.route('/accountingBook/rukomatanyi/umugabane_shingiro')
def umugabane_shingiro():
    umugabane_shingiro = UmugabaneShingiro.query.filter_by(department_id=current_user.email).all()
    rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    return render_template('/accountingBooks/rukomatanyi/umugabane_shingiro.html', umugabane_shingiro=umugabane_shingiro, rukomatanyo=rukomatanyo)

@aicos_req.route('/accountingBook/rukomatanyi/hindura/hinduraUmugabaneShingiro/<int:id>', methods=["GET", "POST"])
def hinduraUmugabaneShingiro(id):
    umugabaneId = UmugabaneShingiro.query.get_or_404(id)
    umugabane = UmugabaneShingiro.query.filter_by(id=umugabaneId.id).first()
    form = UmugabaneShingiroForm()
    if form.validate_on_submit():
        umugabane.ayinjiye = form.ayinjiye.data
        umugabane.ayasohotse = form.ayasohotse.data
        try:
            db.session.commit()
            return redirect(url_for('aicos_req.umugabane_shingiro'))
        except:
            return redirect(url_for('aicos_req.hinduraUmugabaneShingiro', form=form))
    form.ayinjiye.default = umugabane.ayinjiye
    form.ayasohotse.default = umugabane.ayasohotse
    form.process()
    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_umugabane_shingiro.html', form=form)

@aicos_req.route('/accountingBook/rukomatanyi/inkunga')
def inkunga():
    inkunga = Inkunga.query.filter_by(department_id=current_user.email).all()
    rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    return render_template('/accountingBooks/rukomatanyi/inkunga.html', inkunga=inkunga, rukomatanyo = rukomatanyo)

@aicos_req.route('/accountingBook/rukomatanyi/hindura/inkunga/<int:id>', methods=["GET", "POST"])
def hindura_inkunga(id):
    inkungaId = Inkunga.query.get_or_404(id)
    inkunga = Inkunga.query.filter_by(id=inkungaId.id).first()
    form = InkungaForm()
    if form.validate_on_submit():
        inkunga.ayinjiye = form.ayinjiye.data
        inkunga.ayasohotse = form.ayasohotse.data
        try:
            db.session.commit()
            return redirect(url_for('aicos_req.inkunga'))
        except:
            return redirect(url_for('aicos_req.hindura_inkunga', form=form))
    form.ayinjiye.default = inkunga.ayinjiye
    form.ayasohotse.default = inkunga.ayasohotse
    form.process()
    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_inkunga.html', form=form)

@aicos_req.route('/accountingBook/rukomatanyi/inguzanyo_abandi')
def inguzanyo_abandi():
    inguzanyo_abandi = InguzanyoZabandi.query.filter_by(department_id=current_user.email).all()
    rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    return render_template('accountingBooks/rukomatanyi/inguzanyo_abandi.html', inguzanyo_abandi=inguzanyo_abandi, rukomatanyo=rukomatanyo)


@aicos_req.route('/accountingBook/rukomatanyi/hindura/hinduraInguzanyoZabandi<int:id>', methods=["GET", "POST"])
def hinduraInguzanyoZabandi(id):
    inguzanyoId = InguzanyoZabandi.query.get_or_404(id)
    inguzanyo = InguzanyoZabandi.query.filter_by(id=inguzanyoId.id).first()
    form = InguzanyoZabandiForm()
    if form.validate_on_submit():
        inguzanyo.ayinjiye = form.ayinjiye.data
        inguzanyo.ayasohotse = form.ayasohotse.data
        try:
            db.session.commit()
            return redirect(url_for('aicos_req.inguzanyo_abandi'))
        except:
            redirect(url_for('aicos_req.hinduraInguzanyoZabandi', form=form))
    form.ayinjiye.default = inguzanyo.ayinjiye
    form.ayasohotse.default = inguzanyo.ayasohotse
    form.process()
    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_inguzanyo_zabandi.html', form=form)



@aicos_req.route('/accountingBook/rukomatanyi/ibicuruzwa')
def ibicuruzwa():
    ibicuruzwa = Ibicuruzwa.query.filter_by(department_id=current_user.email).all()
    rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    return render_template('/accountingBooks/rukomatanyi/ibicuruzwa.html', ibicuruzwa=ibicuruzwa, rukomatanyo=rukomatanyo)

@aicos_req.route('/accountingBook/rukomatanyi/hindura/ibicuruzwa/<int:id>', methods=["GET", "POST"])
def hindura_ibicuruzwa(id):
    ibicuruzwaId = Ibicuruzwa.query.get_or_404(id)
    ibicuruzwa = Ibicuruzwa.query.filter_by(id=ibicuruzwaId.id).first()
    form = IbicuruzwaForm()

    if form.validate_on_submit():
        ibicuruzwa.ayinjiye = form.ayinjiye.data
        ibicuruzwa.ayasohotse = form.ayasohotse.data
        try:
            db.session.commit()
            return redirect(url_for('aicos_req.ibicuruzwa'))
        except:
            return redirect(url_for('aicos_req.hindura_ibicuruzwa', form=form))
    form.ayinjiye.default = ibicuruzwa.ayinjiye
    form.ayasohotse.default = ibicuruzwa.ayasohotse
    form.process()
    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ibicuruzwa.html', form=form)


@aicos_req.route('/accountingBook/rukomatanyi/ikoreshwa_ryimari')
def ikoreshwa_ryimari():
    ikoreshwa = IkoreshwaRyimari.query.filter_by(department_id=current_user.email).all()
    rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    return render_template('/accountingBooks/rukomatanyi/ikoreshwa_ryimari.html', ikoreshwa=ikoreshwa, rukomatanyo=rukomatanyo)

@aicos_req.route('/accountingBook/rukomatanyi/hindura/ikoreshwa_ryimari/<int:id>', methods=["GET", "POST"])
def hinduraIkoreshwaRyimari(id):
    ikoreshwaId = IkoreshwaRyimari.query.get_or_404(id)
    ikoreshwa = IkoreshwaRyimari.query.filter_by(id=ikoreshwaId.id).first()
    form = IkoreshwaRyimariForm()

    if form.validate_on_submit():
        ikoreshwa.ayinjiye = form.ayinjiye.data
        ikoreshwa.ayasohotse = form.ayasohotse.data
        try:
            db.session.commit()
            return redirect(url_for('aicos_req.ikoreshwa_ryimari'))
        except:
            return redirect(url_for('aicos_req.hinduraIkoreshwaRyimari', form=form))
    form.ayinjiye.default = ikoreshwa.ayinjiye
    form.ayasohotse.default = ikoreshwa.ayasohotse
    form.process()
    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ikoreshwa_ryimari.html', form=form)

@aicos_req.route('/accountingBook/rukomatanyi/ibindi_rukomatanyi')
def ibindi_rukomatanyi():
    ibindi = IbindiRukomatanyi.query.filter_by(department_id=current_user.email).all()
    rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()   
    return render_template('/accountingBooks/rukomatanyi/ibindi_rukomatanyi.html', ibindi=ibindi, rukomatanyo=rukomatanyo)

@aicos_req.route('/accountingBook/rukomatanyi/hindura/hindura_ibindi/<int:id>', methods=["GET", "POST"])
def hindura_ibindi(id):
    ibindiId= IbindiRukomatanyi.query.get_or_404(id)
    ibindi = IbindiRukomatanyi.query.filter_by(id=ibindiId.id).first()
    form = IbindiForm()

    if form.validate_on_submit():
        ibindi.ayinjiye = form.ayinjiye.data
        ibindi.ayasohotse = form.ayasohotse.data
        try:
            db.session.commit()
            return redirect(url_for('aicos_req.ibindi_rukomatanyi'))
        except:
            return redirect(url_for('aicos_req.hindura_ibindi', form=form))
    form.ayinjiye.default = ibindi.ayinjiye
    form.ayasohotse.default = ibindi.ayasohotse
    form.process()
    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ibindi.html', form=form)


@aicos_req.route('/accountingBook/rukomatanyi/injiza/isanduku', methods=["GET", "POST"])
def injiza_isanduku():
    form = IsandukuForm()

    if form.validate_on_submit():
        rukomatanyo = Rukomatanyo(
                            tariki_byakozwe = form.itariki.data,
                            description = form.impamvu.data,
                            piyesi = form.piyesi.data
                            )
        try:
            db.session.add(rukomatanyo)
            db.session.commit()
        except:
            flash("Ntabwo byakunze neza")
            return redirect(url_for('aicos_req.injiza_isanduku'))

        rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

        if rukomatanyo_id is None:
            return redirect(url_for('aicos_req.injiza_isanduku'))

        isanduku = IsandukuNshya(
                            ayinjiye = form.ayinjiye.data,
                            ayasohotse = form.ayasohotse.data,
                            asigaye = form.asigaye.data,
                            department_id = current_user.email,
                            rukomatanyo_id = rukomatanyo_id.id
                            )

        try:
            db.session.add(isanduku)
            db.session.commit()
            return redirect(url_for('aicos_req.isanduku'))
        except:
            return redirect(url_for('aicos_req.injiza_isanduku', form=form))
    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_isanduku.html', form=form)


@aicos_req.route('/accountingBook/rukomatanyi/injiza/bank', methods=["GET", "POST"])
def injizaBank():
    form = BankForm()

    if form.validate_on_submit():
        rukomatanyo = Rukomatanyo(
                            tariki_byakozwe = form.itariki.data,
                            description = form.impamvu.data,
                            piyesi = form.piyesi.data
                            )
        try:
            db.session.add(rukomatanyo)
            db.session.commit()
        except:
            flash("Ntabwo byakunze neza")
            return redirect(url_for('aicos_req.injizaBank'))

        rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

        if rukomatanyo_id is None:
            return redirect(url_for('aicos_req.injizaBank'))

        bank = BankModel(
                        ayinjiye = form.ayinjiye.data,
                        ayasohotse = form.ayasohotse.data,
                        department_id = current_user.email,
                        rukomatanyo_id=rukomatanyo_id.id
                        )

        try:
            db.session.add(bank)
            db.session.commit()
            return redirect(url_for('aicos_req.bank'))
        except:
            return redirect(url_for('aicos_req.injizaBank', form=form))
    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_bank.html', form=form)

@aicos_req.route('/accountingBook/rukomatanyi/injiza/inguzanyo_zatanzwe', methods=["GET", "POST"])
def InjizaIzatanzwe():
    form = InguzanyoZatanzweForm()

    if form.validate_on_submit():

        rukomatanyo = Rukomatanyo(
                            tariki_byakozwe = form.itariki.data,
                            description = form.impamvu.data,
                            piyesi = form.piyesi.data,
                            department_id = current_user.email
                            )
        try:
            db.session.add(rukomatanyo)
            db.session.commit()
        except:
            flash("Ntabwo byakunze neza")
            return redirect(url_for('aicos_req.InjizaIzatanzwe'))

        rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

        if rukomatanyo_id is None:
            return redirect(url_for('aicos_req.InjizaIzatanzwe'))

        inguzanyo = InguzanyoZatanzwe(
                                    ayinjiye = form.ayinjiye.data,
                                    ayasohotse = form.ayasohotse.data,
                                    department_id = current_user.email,
                                    rukomatanyo_id = rukomatanyo_id.id
                                    )
        try:
            db.session.add(inguzanyo)
            db.session.commit()
            return redirect(url_for('aicos_req.inguzanyo_zatanzwe'))
        except:
            return redirect(url_for('aicos_req.InjizaIzatanzwe', form=form))
    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/InjizaIzatanzwe.html', form=form)


@aicos_req.route('/accountingBook/rukomatanyi/injiza/ibiramba', methods=["GET", "POST"])
def record_ibiramba():
    form = IbirambaForm()

    if form.validate_on_submit():

        rukomatanyo = Rukomatanyo(
                            tariki_byakozwe = form.itariki.data,
                            description = form.impamvu.data,
                            piyesi = form.piyesi.data,
                            department_id = current_user.email
                            )
        try:
            db.session.add(rukomatanyo)
            db.session.commit()
        except:
            flash("Ntabwo byakunze neza")
            return redirect(url_for('aicos_req.record_ibiramba'))

        rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

        if rukomatanyo_id is None:
            return redirect(url_for('aicos_req.record_ibiramba'))

        iramba = Ibiramba(
                        ayinjiye = form.ayinjiye.data,
                        ayasohotse = form.ayasohotse.data,
                        department_id = current_user.email,
                        rukomatanyo_id = rukomatanyo_id.id
                        )
        try:
            db.session.add(iramba)
            db.session.commit()
            return redirect(url_for('aicos_req.ibiramba'))
        except:
            return redirect(url_for('aicos_req.record_ibiramba', form=form))

    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ibiramba.html', form=form)


@aicos_req.route('/accountingBook/rukomatanyi/injiza/record_ububiko', methods=["GET", "POST"])
def record_ububiko():
    form = UbubikoForm()

    if form.validate_on_submit():

        rukomatanyo = Rukomatanyo(
                            tariki_byakozwe = form.itariki.data,
                            description = form.impamvu.data,
                            piyesi = form.piyesi.data,
                            department_id = current_user.email
                            )
        try:
            db.session.add(rukomatanyo)
            db.session.commit()
        except:
            flash("Ntabwo byakunze neza")
            return redirect(url_for('aicos_req.record_ububiko'))

        rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

        if rukomatanyo_id is None:
            return redirect(url_for('aicos_req.record_ububiko'))

        ububiko = Ububiko(
                        ayinjiye = form.ayinjiye.data,
                        ayasohotse = form.ayasohotse.data,
                        department_id = current_user.email,
                        rukomatanyo_id = rukomatanyo_id.id
                        )

        try:
            db.session.add(ububiko)
            db.session.commit()
            return redirect(url_for('aicos_req.ububiko'))
        except:
            return redirect(url_for('aicos_req.record_ububiko', form=form))

    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ububiko.html', form=form)


@aicos_req.route('/accountingBook/rukomatanyi/injiza/record_umugabane_shingiro', methods=["GET", "POST"])
def record_umugabane_shingiro():
    form = UmugabaneShingiroForm()

    if form.validate_on_submit():

        rukomatanyo = Rukomatanyo(
                            tariki_byakozwe = form.itariki.data,
                            description = form.impamvu.data,
                            piyesi = form.piyesi.data,
                            department_id = current_user.email
                            )
        try:
            db.session.add(rukomatanyo)
            db.session.commit()
        except:
            flash("Ntabwo byakunze neza")
            return redirect(url_for('aicos_req.record_umugabane_shingiro'))

        rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

        if rukomatanyo_id is None:
            return redirect(url_for('aicos_req.record_umugabane_shingiro'))

        umugabane = UmugabaneShingiro(
                                ayinjiye = form.ayinjiye.data,
                                ayasohotse = form.ayasohotse.data,
                                department_id = current_user.email,
                                rukomatanyo_id = rukomatanyo_id.id
                                )
        try:
            db.session.add(umugabane)
            db.session.commit()
            return redirect(url_for('aicos_req.umugabane_shingiro'))
        except:
            return redirect(url_for('aicos_req.record_umugabane_shingiro', form=form))

    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_umugabane_shingiro.html', form=form)


@aicos_req.route('/accountingBook/rukomatanyi/injiza/record_inkunga', methods=["GET", "POST"])
def record_inkunga():
    form = InkungaForm()

    if form.validate_on_submit():

        rukomatanyo = Rukomatanyo(
                            tariki_byakozwe = form.itariki.data,
                            description = form.impamvu.data,
                            piyesi = form.piyesi.data,
                            department_id = current_user.email
                            )
        try:
            db.session.add(rukomatanyo)
            db.session.commit()
        except:
            flash("Ntabwo byakunze neza")
            return redirect(url_for('aicos_req.record_inkunga'))

        rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

        if rukomatanyo_id is None:
            return redirect(url_for('aicos_req.record_inkunga'))

        inkunga = Inkunga(
                        ayinjiye = form.ayinjiye.data,
                        ayasohotse = form.ayasohotse.data,
                        department_id = current_user.email,
                        rukomatanyo_id = rukomatanyo_id.id
                        )
        try:
            db.session.add(inkunga)
            db.session.commit()
            return redirect(url_for('aicos_req.inkunga'))
        except:
            return redirect(url_for('aicos_req.record_inkunga'))

    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_inkunga.html', form=form)


@aicos_req.route('/accountingBook/rukomatanyi/injiza/record_inguzanyo_abandi', methods=["GET", "POST"])
def record_inguzanyo_abandi():
    form = InguzanyoZabandiForm()

    if form.validate_on_submit():

        rukomatanyo = Rukomatanyo(
                            tariki_byakozwe = form.itariki.data,
                            description = form.impamvu.data,
                            piyesi = form.piyesi.data,
                            department_id = current_user.email
                            )
        try:
            db.session.add(rukomatanyo)
            db.session.commit()
        except:
            flash("Ntabwo byakunze neza")
            return redirect(url_for('aicos_req.record_inkunga'))

        rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

        if rukomatanyo_id is None:
            return redirect(url_for('aicos_req.record_inkunga'))

        inguzanyo = InguzanyoZabandi(
                                ayinjiye = form.ayinjiye.data,
                                ayasohotse = form.ayasohotse.data,
                                department_id = current_user.email,
                                rukomatanyo_id = rukomatanyo_id.id 
                                )
        try:
            db.session.add(inguzanyo)
            db.session.commit()
            return redirect(url_for('aicos_req.inguzanyo_abandi'))
        except:
            return redirect(url_for('aicos_req.record_inguzanyo_abandi'))

    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_inguzanyo_abandi.html', form=form)

@aicos_req.route('/accountingBook/rukomatanyi/injiza/record_ibicuruzwa', methods=["GET", "POST"])
def record_ibicuruzwa():
    form = IbicuruzwaForm()

    if form.validate_on_submit():


        
        rukomatanyo = Rukomatanyo(
                            tariki_byakozwe = form.itariki.data,
                            description = form.impamvu.data,
                            piyesi = form.piyesi.data,
                            department_id = current_user.email
                            )
        try:
            db.session.add(rukomatanyo)
            db.session.commit()
        except:
            flash("Ntabwo byakunze neza")
            return redirect(url_for('aicos_req.record_ibicuruzwa'))

        rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

        if rukomatanyo_id is None:
            return redirect(url_for('aicos_req.record_ibicuruzwa'))

        ibicuruzwa = Ibicuruzwa(
                                ayinjiye = form.ayinjiye.data,
                                ayasohotse = form.ayasohotse.data,
                                department_id = current_user.email,
                                rukomatanyo_id = rukomatanyo_id.id
                                )
        try:
            db.session.add(ibicuruzwa)
            db.session.commit()
            return redirect(url_for('aicos_req.ibicuruzwa'))
        except:
            return redirect(url_for('aicos_req.record_ibicuruzwa', form=form))

    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ibicuruzwa.html', form=form)


@aicos_req.route('/accountingBook/rukomatanyi/injiza/record_ikoreshwa_ryimari', methods=["GET", "POST"])
def record_ikoreshwa_ryimari():
    form = IkoreshwaRyimariForm()

    if form.validate_on_submit():


        rukomatanyo = Rukomatanyo(
                            tariki_byakozwe = form.itariki.data,
                            description = form.impamvu.data,
                            piyesi = form.piyesi.data,
                            department_id = current_user.email
                            )
        try:
            db.session.add(rukomatanyo)
            db.session.commit()
        except:
            flash("Ntabwo byakunze neza")
            return redirect(url_for('aicos_req.record_ikoreshwa_ryimari'))

        rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

        if rukomatanyo_id is None:
            return redirect(url_for('aicos_req.record_ikoreshwa_ryimari'))

        ikoreshwa = IkoreshwaRyimari(
                                    ayinjiye = form.ayinjiye.data,
                                    ayasohotse = form.ayasohotse.data,
                                    department_id = current_user.email,
                                    rukomatanyo_id = rukomatanyo_id.id 
                                    )
        try:
            db.session.add(ikoreshwa)
            db.session.commit()
            return redirect(url_for('aicos_req.ikoreshwa_ryimari'))
        except:
            return redirect(url_for('aicos_req.record_ikoreshwa_ryimari'))

    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ikoreshwa_ryimari.html', form=form)
        


@aicos_req.route('/accountingBook/rukomatanyi/injiza/ibindi', methods=["GET", "POST"])
def record_ibindi():
    form = IbindiForm()

    if form.validate_on_submit():


        rukomatanyo = Rukomatanyo(
                            tariki_byakozwe = form.itariki.data,
                            description = form.impamvu.data,
                            piyesi = form.piyesi.data,
                            department_id = current_user.email
                            )
        try:
            db.session.add(rukomatanyo)
            db.session.commit()
        except:
            flash("Ntabwo byakunze neza")
            return redirect(url_for('aicos_req.record_ibindi'))

        rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

        if rukomatanyo_id is None:
            return redirect(url_for('aicos_req.record_ibindi'))

        ibindi = IbindiRukomatanyi(
                                ayinjiye = form.ayinjiye.data,
                                ayasohotse = form.ayasohotse.data,
                                department_id = current_user.email,
                                rukomatanyo_id = rukomatanyo_id.id 
                                )
        try:
            db.session.add(ibindi)
            db.session.commit()
            return redirect(url_for('aicos_req.ibindi_rukomatanyi'))
        except:
            return redirect(url_for('aicos_req.record_ibindi'))

    return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ibindi.html', form=form)






@aicos_req.route('/accountingBooks/UbwisazureList')
def UbwisazureList():
    ubwisazurexx = UbwisazureEnter.query.all()
    return render_template('accountingBooks/ubwisazure/ubwisazure_list.html',
                            ubwisazurexx=ubwisazurexx, title='Ubwisazure ku mutungo wa cooperative!!')






# ibitabo bya banks.
@aicos_req.route('/accountingBooks/Ubwisazure', methods=['GET', 'POST'])
def UbwisazureBwose():
    form = UbwisazureForm()
    if form.validate_on_submit():
        ubwisazurex = UbwisazureEnter(
                                AssetDescription = form.AssetDescriptionx.data,
                                cost = form.costx.data,
                                YearOfPurchase = form.YearOfPurchasex.data,
                                SalvageValue = form.SalvageValuex.data,
                                UsefulLife = form.UsefulLifex.data,
                                Method = form.Methodx.data,
                                department_id = current_user.email
                                )

        try:
            db.session.add(ubwisazurex)
            db.session.commit()
            flash("Umaze kwinjize umutungo neza!")
            return redirect(url_for('aicos_req.UbwisanzureList'))
        except:
            flash("Ntabwo umutungo wabashije kwinjira neza!")
    return render_template('accountingBooks/ubwisazure/ubwisazure_form.html', form=form, title="List y'ubwisazure bw'umutungo!")


@aicos_req.route('/accountingBooks/imyishyurire')
def Imyishyurire():
    return render_template('/accountingBooks/imyishyurire.html')





@aicos_req.route('/accountingBooks/general', methods=['GET', 'POST'])
def general_accounting():

    Ivalues = []
    Bvalues = []
    Evalues = []

    DIvalues = []
    DBvalues = []
    DEvalues = []
    
    Dlabels = []

    today_income = 0
    monthly_income = 0
    quarterly_income = 0
    quarterly1_income = 0
    quarterly2_income = 0
    quarterly3_income = 0
    quarterly4_income = 0
    yearly_income = 0

    today_expense = 0
    monthly_expense = 0
    quarterly_expense = 0
    quarterly1_expense = 0
    quarterly2_expense = 0
    quarterly3_expense = 0
    quarterly4_expense = 0
    yearly_expense = 0

    today_budget = 0
    monthly_budget = 0
    quarterly_budget = 0
    quarterly1_budget = 0
    quarterly2_budget = 0
    quarterly3_budget = 0
    quarterly4_budget = 0
    yearly_budget = 0
    
    monthly_balance = 0
    quarterly_balance = 0
    yearly_balance = 0

    budgets = []
    incomes = []
    expenses = []

    Accounts = Account.query.all()
    Budgets = Budget.query.all()

    Expenses = Expense.query.all()
    Incomes = Income.query.all()

    if len(Accounts)>10:
        accounts = []
        leastA = Accounts[len(Accounts)-10].id
        for account in Accounts:
            if Accounts.index(account)>=len(Accounts)-10:
                accounts.append(account)
    else:
        accounts = Accounts

    if len(Budgets)>10:
        budgets = []
        leastB = Budgets[len(Budgets)-10].id
        for budget in Budgets:
            if Budgets.index(budget)>=len(Budgets)-10:
                budgets.append(budget)
    else:
        budgets = Budgets

    for expense in Expenses:
        if (str((expense.Date)).split('-'))[0] == (str((date.today())).split('-'))[0]:
            yearly_expense+=int(expense.Amount)

            if (str((expense.Date)).split('-'))[1] == '01'or '02'or '03':
                quarterly1_expense+=int(expense.Amount)
                if (str((date.today())).split('-'))[1] == '01'or '02'or '03':
                    quarterly_expense = quarterly1_expense

            if (str((expense.Date)).split('-'))[1] == '04'or '05'or '06':
                quarterly2_expense+=int(expense.Amount)
                if (str((date.today())).split('-'))[1] == '04'or '05'or '06':    
                    quarterly_expense = quarterly2_expense

            if (str((expense.Date)).split('-'))[1] == '07'or '08'or '09':
                quarterly3_expense+=int(expense.Amount)
                if (str((date.today())).split('-'))[1] == '07'or '08'or '09':    
                    quarterly_expense = quarterly3_expense

            if (str((expense.Date)).split('-'))[1] == '10'or '11'or '12':
                quarterly4_expense+=int(expense.Amount)
                if (str((date.today())).split('-'))[1] == '10'or '11'or '12':    
                    quarterly_expense = quarterly4_expense 


            if (str((expense.Date)).split('-'))[1] == (str((date.today())).split('-'))[1]:
                monthly_expense+=int(expense.Amount)
                
                if (str((expense.Date)).split('-'))[2] == (str((date.today())).split('-'))[2]:
                    today_expense+=int(expense.Amount)

        if len(Expenses)>5:
            if Expenses.index(expense)>=len(Expenses)-5:
                expenses.append(expense)
        else:
            expenses = Expenses

    for income in Incomes:
        if (str((income.Date)).split('-'))[0] == (str((date.today())).split('-'))[0]:
            yearly_income+=int(income.Amount)

            if (str((income.Date)).split('-'))[1] == (str((date.today())).split('-'))[1]:
                monthly_income+=int(income.Amount)

                if (str((income.Date)).split('-'))[2] == (str((date.today())).split('-'))[2]:
                    today_income+=int(income.Amount)

        if len(Incomes)>5:
            if Incomes.index(income)>=len(Incomes)-5:
                incomes.append(income)
        else:
            incomes = Incomes

    
    
    for budget in Budgets:
        if (str((budget.Date)).split('-'))[0] == (str((date.today())).split('-'))[0]:
            yearly_budget+=int(budget.Amount) 

            y_days = 0
            months = [1,2,3,4,5,6,7,8,9,10,11,12]
            for m in months:
                y_days += (calendar.monthrange(date.today().year,m)[1])
            
            p_days = 0
            for mon in months:
                if mon == date.today().month:
                    if mon == 1:
                        c_days = date.today().day
                    else:
                        p_days += (calendar.monthrange(date.today().year,mon-1)[1])
                        c_days = p_days + date.today().day
                    y_time_passed = round(((c_days*100)/y_days),2)
            

            if (str((budget.Date)).split('-'))[1] == '01'or '02'or '03':
                quarterly1_budget+=int(budget.Amount)

                if (str((date.today())).split('-'))[1] == '01'or '02'or '03':
                    quarterly_budget = quarterly1_budget

                    q_days = (calendar.monthrange(date.today().year,1)[1])+(calendar.monthrange(date.today().year,2)[1])+(calendar.monthrange(date.today().year,3)[1])

                    if (str((date.today())).split('-'))[1] == '01':
                        q_time_passed = round((date.today().day)*100/q_days,2)

                    if (str((date.today())).split('-'))[1] == '02':
                        q_time_passed = round(((calendar.monthrange(date.today().year,1)[1]) + date.today().day)*100/q_days,2)

                    if (str((date.today())).split('-'))[1] == '03':
                        q_time_passed = round(((calendar.monthrange(date.today().year,2)[1]) + (calendar.monthrange(date.today().year,1)[1]) + date.today().day)*100/q_days,2)

            if (str((budget.Date)).split('-'))[1] == '04'or '05'or '06':
                quarterly2_budget+=int(budget.Amount)

                if (str((date.today())).split('-'))[1] == '04'or '05'or '06':    
                    quarterly_budget = quarterly2_budget

                    q_days = (calendar.monthrange(date.today().year,4)[1])+(calendar.monthrange(date.today().year,5)[1])+(calendar.monthrange(date.today().year,6)[1])

                    if (str((date.today())).split('-'))[1] == '04':
                        q_time_passed = round((date.today().day)*100/q_days,2)

                    if (str((date.today())).split('-'))[1] == '05':
                        q_time_passed = round(((calendar.monthrange(date.today().year,4)[1]) + date.today().day)*100/q_days,2)

                    if (str((date.today())).split('-'))[1] == '06':
                        q_time_passed = round(((calendar.monthrange(date.today().year,5)[1]) + (calendar.monthrange(date.today().year,4)[1]) + date.today().day)*100/q_days,2)

            if (str((budget.Date)).split('-'))[1] == '07'or '08'or '09':
                quarterly3_budget+=int(budget.Amount)

                if (str((date.today())).split('-'))[1] == '07'or '08'or '09':    
                    quarterly_budget = quarterly3_budget

                    q_days = (calendar.monthrange(date.today().year,7)[1])+(calendar.monthrange(date.today().year,8)[1])+(calendar.monthrange(date.today().year,9)[1])

                    if (str((date.today())).split('-'))[1] == '07':
                        q_time_passed = round((date.today().day)*100/q_days,2)

                    if (str((date.today())).split('-'))[1] == '08':
                        q_time_passed = round(((calendar.monthrange(date.today().year,7)[1]) + date.today().day)*100/q_days,2)

                    if (str((date.today())).split('-'))[1] == '09':
                        q_time_passed = round(((calendar.monthrange(date.today().year,9)[1]) + (calendar.monthrange(date.today().year,8)[1]) + date.today().day)*100/q_days,2)

            if (str((budget.Date)).split('-'))[1] == '10'or '11'or '12':
                quarterly4_budget+=int(budget.Amount)

                if (str((date.today())).split('-'))[1] == '10'or '11'or '12':    
                    quarterly_budget = quarterly4_budget

                    q_days = (calendar.monthrange(date.today().year,10)[1])+(calendar.monthrange(date.today().year,11)[1])+(calendar.monthrange(date.today().year,12)[1])

                    if (str((date.today())).split('-'))[1] == '10':
                        q_time_passed = round((date.today().day)*100/q_days,2)

                    if (str((date.today())).split('-'))[1] == '11':
                        q_time_passed = round(((calendar.monthrange(date.today().year,10)[1]) + date.today().day)*100/q_days,2)

                    if (str((date.today())).split('-'))[1] == '12':
                        q_time_passed = round(((calendar.monthrange(date.today().year,12)[1]) + (calendar.monthrange(date.today().year,10)[1]) + date.today().day)*100/q_days,2)

            

            if (str((budget.Date)).split('-'))[1] == (str((date.today())).split('-'))[1] and budget.Period == 'Monthly':
                monthly_budget+=int(budget.Amount)
                
                if (str((budget.Date)).split('-'))[2] == (str((date.today())).split('-'))[2]:
                    today_budget+=int(budget.Amount)
                
    if today_budget!=0:
        d_budget_used = round(((today_expense*100)/today_budget),2)
    else:
        d_budget_used = 0

    if monthly_budget!=0:
        m_budget_used = round(((monthly_expense*100)/monthly_budget),2)
    else:
        m_budget_used = 0

    if quarterly_budget!=0:
        q_budget_used = round(((quarterly_expense*100)/quarterly_budget),2)
    else:
        q_budget_used = 0
    if yearly_budget!=0:
        y_budget_used = round(((yearly_expense*100)/yearly_budget),2)
    else:
        y_budget_used = 0
        
    t = datetime.time(datetime.now()).strftime('%X').split(':')
    
    t1 = []
    for i in t:
        t1.append(int(i))

    t2 = (t1[0]*60*60)+(t1[1]*60)+t1[2]
    ti = (6*60*60)
    tf = (18*60*60)
    tn = (8*60*60)+(55*60)
    # print(t2)

    if (6<t1[0] and t1[1]>0 and t1[0]<18): 
        d_time_passed = round((t2-ti)*100/(tf-ti),2)
    else:
        d_time_passed = 0
    m_time_passed = round((date.today().day)*100/(calendar.monthrange(date.today().year,date.today().month)[1]),2)

    monthly_balance = monthly_income-monthly_expense
    yearly_balance = yearly_income-yearly_expense

    # # print(tn)
    # print(d_budget_used)
    # if t2 == tn:
    #     archives = Archive(
    #         d_budget_used = d_budget_used
    #     )
    #     db.session.add(archives)
    #     db.session.commit()



    
    labels = [
        'Jan', 'Feb', 'Mar', 'Apr',
        'May', 'Jun', 'Jul', 'Aug',
        'Sep', 'Oct', 'Nov', 'Dec'
    ]
    mylabels = [
        '01', '02', '03', '04',
        '05', '06', '07', '08',
        '09', '10', '11', '12'
    ]


    for label in mylabels:

        m_income = 0
        m_budget = 0
        m_expense = 0

        for income in Incomes:
            if (str((income.Date)).split('-'))[0] == (str((date.today())).split('-'))[0]:
                if (str((income.Date)).split('-'))[1] == label:
                    m_income+=int(income.Amount)
        Ivalues.append(m_income) 

        for budget in Budgets:
            if (str((budget.Date)).split('-'))[0] == (str((date.today())).split('-'))[0]:
                if (str((budget.Date)).split('-'))[1] == label and budget.Period == 'Monthly':
                    m_budget+=int(budget.Amount)
        Bvalues.append(m_budget) 

        for expense in Expenses:
            if (str((expense.Date)).split('-'))[0] == (str((date.today())).split('-'))[0]:
                if (str((expense.Date)).split('-'))[1] == label:
                    m_expense+=int(expense.Amount)
        Evalues.append(m_expense)

    


    Dlabels = [calendar.monthcalendar(date.today().year, date.today().month)]

    myDlabels = ['01', '02', '03', '04','05', '06', '07', '08','09']
    myDlabels2 = []

    for sub in Dlabels:
        for l in sub:
            myDlabels += l
            myDlabels2 += l
            

    for i in myDlabels2:
        if i<1:        
            del myDlabels2[myDlabels2.index(i)]

    for label in myDlabels:

        today_inc = 0
        today_bud = 0
        today_exp = 0

        for income in Incomes:
            if (str((income.Date)).split('-'))[0] == (str((date.today())).split('-'))[0]:
                if (str((income.Date)).split('-'))[1] == (str((date.today())).split('-'))[1]:
                    if (str((income.Date)).split('-'))[2] == str(label):
                        today_inc+=int(income.Amount)
        DIvalues.append(today_inc) 

        for budget in Budgets:
            if (str((budget.Date)).split('-'))[0] == (str((date.today())).split('-'))[0]:
                if (str((budget.Date)).split('-'))[1] == (str((date.today())).split('-'))[1]:
                    if (str((budget.Date)).split('-'))[2] == str(label) and (budget.Period == 'Daily'):
                        today_bud+=int(budget.Amount)
        DBvalues.append(today_bud) 

        for expense in Expenses:
            if (str((expense.Date)).split('-'))[0] == (str((date.today())).split('-'))[0]:
                if (str((expense.Date)).split('-'))[1] == (str((date.today())).split('-'))[1]:
                    if (str((expense.Date)).split('-'))[2] == str(label):
                        today_exp+=int(expense.Amount)
        DEvalues.append(today_exp)
    
    values = Ivalues and Evalues and Bvalues
    Dvalues = DIvalues and DEvalues and DBvalues

    



    form = ArchivesForm()
    if form.validate_on_submit():
        archive = Archive(
                    date = str(date.today()),

                    m_income = str(monthly_income),
                    m_expense = str(monthly_expense),

                    y_income = str(yearly_income),
                    y_expense = str(yearly_expense),

                    d_intl_budget = str(today_budget),
                    m_intl_budget = str(monthly_budget),
                    q_intl_budget = str(quarterly_budget),
                    y_intl_budget = str(yearly_budget),

                    d_budget_used = str(d_budget_used),
                    m_budget_used = str(m_budget_used),
                    q_budget_used = str(q_budget_used),
                    y_budget_used = str(y_budget_used),

                    d_time_passed = str(d_time_passed),
                    m_time_passed = str(m_time_passed),
                    q_time_passed = str(q_time_passed),
                    y_time_passed = str(y_time_passed)
                        )

        try:
            db.session.add(archive)
            db.session.commit()
            flash("Umaze kwinjize data neza!")
            # return redirect(url_for('aicos_req.UbwisanzureList'))
        except:
            flash("Ntabwo data zabashije kwinjira neza!")

    today = date.today()

    return render_template('accountingBooks/general/general_accounting.html', form=form, today=today,
        today_budget=today_budget,monthly_budget=monthly_budget,quarterly_budget=quarterly_budget,yearly_budget=yearly_budget,
        d_budget_used=d_budget_used,m_budget_used=m_budget_used,q_budget_used=q_budget_used,y_budget_used=y_budget_used,
        quarterly_expense=quarterly_expense,quarterly_income=quarterly_income,
        yearly_income=yearly_income,yearly_expense=yearly_expense,yearly_balance=yearly_balance,
        monthly_income=monthly_income,monthly_expense=monthly_expense,monthly_balance=monthly_balance,
        budgets=budgets,accounts=accounts,expense=expense,
        incomes=incomes,expenses=expenses, 
        max=max(values), labels=labels, Ivalues=Ivalues, Evalues=Evalues, Bvalues=Bvalues,
        Dmax=max(Dvalues), Dlabels=myDlabels2, DIvalues=DIvalues, DEvalues=DEvalues, DBvalues=DBvalues,
        d_time_passed=d_time_passed, m_time_passed=m_time_passed, q_time_passed=q_time_passed, y_time_passed=y_time_passed)






@aicos_req.route('/accountingBooks/general/budget', methods=["GET", "POST"])
def budget():
    budgets = Budget.query.all()
    m_budgets = Budget.query.filter_by(Period='value').all()
    q_budgets = Budget.query.filter_by(Period='value_two').all()
    y_budgets = Budget.query.filter_by(Period='value_three').all()
    return render_template('/accountingBooks/general/budget.html',
        budgets=budgets,m_budgets=m_budgets,q_budgets=q_budgets,y_budgets=y_budgets)

@aicos_req.route('/accountingBooks/general/monthly_budgets', methods=["GET", "POST"])
def m_budget():
    m_budgets = Budget.query.filter_by(Period='value').all()
    q_budgets = Budget.query.filter_by(Period='value_two').all()
    y_budgets = Budget.query.filter_by(Period='value_three').all()
    return render_template('/accountingBooks/general/m_budget.html',
        m_budgets=m_budgets,q_budgets=q_budgets,y_budgets=y_budgets)

@aicos_req.route('/accountingBooks/general/quarterly_budgets', methods=["GET", "POST"])
def q_budget():
    m_budgets = Budget.query.filter_by(Period='value').all()
    q_budgets = Budget.query.filter_by(Period='value_two').all()
    y_budgets = Budget.query.filter_by(Period='value_three').all()
    return render_template('/accountingBooks/general/q_budget.html',
        m_budgets=m_budgets,q_budgets=q_budgets,y_budgets=y_budgets)

@aicos_req.route('/accountingBooks/general/yearly_budgets', methods=["GET", "POST"])
def y_budget():
    m_budgets = Budget.query.filter_by(Period='value').all()
    q_budgets = Budget.query.filter_by(Period='value_two').all()
    y_budgets = Budget.query.filter_by(Period='value_three').all()
    return render_template('/accountingBooks/general/y_budget.html',
        m_budgets=m_budgets,q_budgets=q_budgets,y_budgets=y_budgets)


@aicos_req.route('/accountingBooks/general/monthly_incomes', methods=["GET", "POST"])
def m_income():
    m_incomes = []
    Incomes = Income.query.all()
    for income in Incomes:
        if (str(income.Date).split('-'))[0] == (str((date.today())).split('-'))[0] and (str(income.Date).split('-'))[1] == (str((date.today())).split('-'))[1]:
            m_incomes.append(income)
    return render_template('/accountingBooks/general/income.html',
        incomes=m_incomes)

@aicos_req.route('/accountingBooks/general/yearly_incomes', methods=["GET", "POST"])
def y_income():
    y_incomes = []
    Incomes = Income.query.all()
    for income in Incomes:
        if (str(income.Date).split('-'))[0] == (str((date.today())).split('-'))[0]:
            y_incomes.append(income)
    return render_template('/accountingBooks/general/income.html',
        incomes=y_incomes)


@aicos_req.route('/accountingBooks/general/monthly_expenses', methods=["GET", "POST"])
def m_expense():
    m_expenses = []
    Expenses = Expense.query.all()
    for expense in Expenses:
        if (str(expense.Date).split('-'))[0] == (str((date.today())).split('-'))[0] and (str(expense.Date).split('-'))[1] == (str((date.today())).split('-'))[1]:
            m_expenses.append(expense)
    return render_template('/accountingBooks/general/expense.html',
        expenses=m_expenses)

@aicos_req.route('/accountingBooks/general/yearly_expenses', methods=["GET", "POST"])
def y_expense():
    y_expenses = []
    Expenses = Expense.query.all()
    for expense in Expenses:
        if (str(expense.Date).split('-'))[0] == (str((date.today())).split('-'))[0]:
            y_expenses.append(expense)
    return render_template('/accountingBooks/general/expense.html',
        expenses=y_expenses)


@aicos_req.route('/accountingBooks/general/delete_category<id>', methods=["GET", "POST"])
def delete_category(id):

    is_accountant = Employee.query.filter_by(is_accountant=True).first()

    category = ExpenseCategory.query.filter_by(id=id).first() 
    
    if category == ExpenseCategory.query.filter_by(id=id).first():
        form = ExpenseForm()
        category_form = ExpenseCategoryForm()
        if current_user == is_accountant:
            try:
                db.session.delete(category)
                db.session.commit()
                flash("Umaze Gusiba Category neza!")
            except:
                flash("Ntabwo Category yabashije Gusibwa neza!")
        else:
            flash("You have no right to delete a category.")
        return render_template('/accountingBooks/general/new_expense.html',form=form,category_form=category_form)

    category = BudgetCategory.query.filter_by(id=id).first()
    
    if category == BudgetCategory.query.filter_by(id=id).first():
        form = BudgetForm()
        category_form = BudgetCategoryForm()
        if current_user == is_accountant:
            try:
                db.session.delete(category)
                db.session.commit()
                flash("Umaze Gusiba Category neza!")
            except:
                flash("Ntabwo Category yabashije Gusibwa neza!")
        else:
            flash("You have no right to delete a category.")
        return render_template('/accountingBooks/general/new_budget.html',form=form,category_form=category_form)

    category = IncomeCategory.query.filter_by(id=id).first()
    
    if category == IncomeCategory.query.filter_by(id=id).first():
        form = IncomeForm() 
        category_form = IncomeCategoryForm() 
        if current_user == is_accountant:
            try:
                db.session.delete(category)
                db.session.commit()
                flash("Umaze Gusiba Category neza!")
            except:
                flash("Ntabwo Category yabashije Gusibwa neza!")
        else:
            flash("You have no right to delete a category.")
        return render_template('/accountingBooks/general/new_income.html',form=form,category_form=category_form)


@aicos_req.route('/accountingBooks/general/new_budget', methods=["GET", "POST"])
def new_budget():
    form = BudgetForm()
    category_form = BudgetCategoryForm()
    is_accountant = Employee.query.filter_by(is_accountant=True).first()

    # if current_user == is_accountant:
    
    if form.validate_on_submit():
        budget = Budget(
            Title = form.Title.data,
            Category = form.Category.data,
            Date = form.Date.data,
            Amount = form.Amount.data,
            Period = form.Period.data,
            cooperative_id = current_user.department
        )
        try:
            db.session.add(budget)
            db.session.commit()
            flash("Umaze kwinjiza Budget neza!")
            return redirect(url_for('aicos_req.budget'))
        except:
            flash("Ntabwo Budget yabashije kwinjira neza!")

    if category_form.validate_on_submit():
        category = BudgetCategory(
            Category = category_form.Category.data,
            cooperative_id = current_user.department
        )
        try:
            db.session.add(category)
            db.session.commit()
            flash("Umaze kwinjize Budget_Category neza!")
            return redirect(url_for('aicos_req.budget'))
        except:
            flash("Ntabwo Budget_Category yabashije kwinjira neza!")

    return render_template('/accountingBooks/general/new_budget.html',form=form,category_form=category_form)


@aicos_req.route('/accountingBooks/general/edit_budget<id>',methods=["GET","POST"])
def edit_budget(id):
    budget = Budget.query.filter_by(id=id).first()
    budget.Date = datetime.strptime(budget.Date,'%Y-%m-%d')
    category_form = BudgetCategoryForm()
    form = BudgetForm(obj=budget)
    is_accountant = Employee.query.filter_by(is_accountant=True).first()

    if current_user == is_accountant:
        form.Title.data = budget.Title
        form.Category.data = budget.AccountName
        form.Date.data = budget.Description
        form.Amount.data = budget.Amount
        form.Period.data = budget.Period

        if form.validate_on_submit():
            budget.Title = form.Title.data
            budget.Category = form.Category.data
            budget.Date = form.Date.data
            budget.Amount = form.Amount.data
            budget.Period = form.Period.data
            budget.cooperative_id = current_user.department
            try:
                db.session.commit()
                flash("Umaze Guhindura Budget neza!")
                return redirect(url_for('aicos_req.budget'))
            except:
                flash("Ntabwo Budget yabashije Guhindurwa neza!")
    return render_template('/accountingBooks/general/new_budget.html',form=form,category_form=category_form)

@aicos_req.route('/assets/delete_budget<id>',methods=["GET","POST"])
def delete_budget(id):
    budget = Budget.query.filter_by(id=id).first()
    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    if current_user == is_accountant:
        try:
            db.session.delete(budget)
            db.session.commit()
            flash("Umaze Gusiba Budget neza!")
            return redirect(url_for('aicos_req.budget'))
        except:
            flash("Ntabwo Budget yabashije Gusibwa neza!")
    else:
        flash("You have no right to delete a budget.")
    budgets = Budget.query.all()
    return render_template('/accountingBooks/general/budget.html',budgets=budgets)





@aicos_req.route('/accountingBooks/general/income', methods=["GET", "POST"])
def income():
    incomes = Income.query.all()
    return render_template('/accountingBooks/general/income.html',incomes=incomes)

@aicos_req.route('/accountingBooks/general/new_income', methods=["GET", "POST"])
def new_income():
    new_income = True
    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    form = IncomeForm()
    category_form = IncomeCategoryForm()

    if current_user == is_accountant:
        if form.validate_on_submit():
            income = Income(
                Title = form.Title.data,
                Amount = form.Amount.data,
                Account = form.Account.data,
                Date = form.Date.data,
                Category = form.Category.data,
                Description = form.Description.data,
                cooperative_id = current_user.department
            )
            try:
                db.session.add(income)
                db.session.commit()
                flash("Umaze kwinjize Income neza!")
                return redirect(url_for('aicos_req.income'))
            except:
                flash("Ntabwo Income yabashije kwinjira neza!")

        if category_form.validate_on_submit():
            category = IncomeCategory(
                Category = category_form.Category.data,
                cooperative_id = current_user.department
            )
            try:
                db.session.add(category)
                db.session.commit()
                flash("Umaze kwinjize Income_Category neza!")
                return redirect(url_for('aicos_req.new_income'))
            except:
                flash("Ntabwo Income_Category yabashije kwinjira neza!")
    return render_template('/accountingBooks/general/new_income.html',form=form,category_form=category_form)

@aicos_req.route('/accountingBooks/general/edit_income<id>',methods=["GET","POST"])
def edit_income(id):
    new_income = False
    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    income = Income.query.filter_by(id=id).first()
    income.Date = datetime.strptime(income.Date,'%Y-%m-%d')
    category_form = IncomeCategoryForm()
    form = IncomeForm(obj=income)

    if current_user == is_accountant:

        form.Title.data = income.Title
        form.Date.data = income.Date
        form.Category.data = income.Category
        form.Account.data = income.Account
        form.Amount.data = income.Amount
        form.Description.data = income.Description

        if form.validate_on_submit():
            income.Title = form.Title.data
            income.Date = form.Date.data
            income.Category = form.Category.data
            income.Account = form.Account.data
            income.Amount = form.Amount.data
            income.Description = form.Description.data
            income.cooperative_id = current_user.department
            try:
                db.session.commit()
                flash("Umaze Guhindura Income neza!")
                return redirect(url_for('aicos_req.income'))
            except:
                flash("Ntabwo Income yabashije Guhindurwa neza!")
    return render_template('/accountingBooks/general/new_income.html',form=form,category_form=category_form)

@aicos_req.route('/accountingBooks/general/delete_income<id>',methods=["GET","POST"])
def delete_income(id):
    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    if current_user == is_accountant:
        income = Income.query.filter_by(id=id).first()
        try:
            db.session.delete(income)
            db.session.commit()
            flash("Umaze Gusiba Income neza!")
            return redirect(url_for('aicos_req.income'))
        except:
            flash("Ntabwo Income yabashije Gusibwa neza!")
    else:
        flash("You have no right to delete an income.")
    incomes = Income.query.all()
    return render_template('/accountingBooks/general/income.html',incomes=incomes)




@aicos_req.route('/accountingBooks/general/expense', methods=["GET", "POST"])
def expense():
    expenses = Expense.query.all()
    return render_template('/accountingBooks/general/expense.html',expenses=expenses)

@aicos_req.route('/accountingBooks/general/new_expense', methods=["GET", "POST"])
def new_expense():
    categories = ExpenseCategory.query.all()

    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    is_admin = Employee.query.filter_by(is_admin=True).first()
    is_coop_admin = Employee.query.filter_by(is_coop_admin=True).first()

    form = ExpenseForm()
    category_form=ExpenseCategoryForm()

    if current_user == is_accountant:
        if form.validate_on_submit():
            expense = Expense(
                Title = form.Title.data,
                Amount = form.Amount.data,
                Budget = form.Budget.data,
                Date = form.Date.data,
                Category = form.Category.data,
                Description = form.Description.data,
                cooperative_id = current_user.department
            )
            try:
                db.session.add(expense)
                db.session.commit()
                flash("Umaze kwinjiza Expense neza!")
                return redirect(url_for('aicos_req.expense'))
            except:
                flash("Ntabwo Expense yabashije kwinjira neza!")

        if category_form.validate_on_submit():
            category = ExpenseCategory(
                Category = category_form.Category.data,
                cooperative_id = current_user.department
            )
            try:
                db.session.add(category)
                db.session.commit()
                flash("Umaze kwinjiza Expense_Category neza!")
                return redirect(url_for('aicos_req.new_expense'))
            except:
                flash("Ntabwo Expense_Category yabashije kwinjira neza!")
    return render_template('/accountingBooks/general/new_expense.html',categories=categories,form=form,category_form=category_form)

@aicos_req.route('/accountingBooks/general/edit_expense<id>',methods=["GET","POST"])
def edit_expense(id):
    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    expense = Expense.query.filter_by(id=id).first()
    expense.Date = datetime.strptime(expense.Date,'%Y-%m-%d')
    category_form = ExpenseCategoryForm()
    form = ExpenseForm(obj=expense)

    if current_user == is_accountant:

        form.Title.data = expense.Title
        form.Date.data = expense.Date
        form.Category.data = expense.Category
        form.Account.data = expense.Account
        form.Amount.data = expense.Amount
        form.Description.data = expense.Description

        if form.validate_on_submit():
            expense.Title = form.Title.data
            expense.Date = form.Date.data
            expense.Category = form.Category.data
            expense.Account = form.Account.data
            expense.Amount = form.Amount.data
            expense.Description = form.Description.data
            expense.cooperative_id = current_user.department
            try:
                db.session.commit()
                flash("Umaze Guhindura Expense neza!")
                return redirect(url_for('aicos_req.expense'))
            except:
                flash("Ntabwo Expense yabashije Guhindurwa neza!")
    return render_template('/accountingBooks/general/new_expense.html',form=form,category_form=category_form)


@aicos_req.route('/accountingBooks/general/delete_expense<id>',methods=["GET","POST"])
def delete_expense(id):
    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    if current_user == is_accountant:
        expense = Expense.query.filter_by(id=id).first()
        try:
            db.session.delete(expense)
            db.session.commit()
            flash("Umaze Gusiba Expense neza!")
            return redirect(url_for('aicos_req.expense'))
        except:
            flash("Ntabwo Expense yabashije Gusibwa neza!")
    else:
        flash("You have no right to delete an expense.")
    expenses = Expense.query.all()
    return render_template('/accountingBooks/general/expense.html',expenses=expenses)





@aicos_req.route('/assets', methods=["GET", "POST"])
def asset():
    assets = Asset.query.all()
    assetsAccountings = assetsAccounting.query.all()
    return render_template('/assets/asset.html',assets=assets,assetsAccountings=assetsAccountings)

@aicos_req.route('/assets/new_asset', methods=["GET", "POST"])
def new_asset():
    form = AssetsForm()
    category_form = AssetCategoryForm()

    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    # if current_user == is_accountant:
    if form.validate_on_submit():
        asset = assetsAccounting(
            Title = form.Title.data,
            Date = form.Date.data,
            Category = form.Category.data,
            # Account = form.Account.data,
            Amount = form.Amount.data,
            Description = form.Description.data,
            cooperative_id = current_user.department
        )
        try:
            db.session.add(asset)
            db.session.commit()
            flash("Umaze kwinjiza Asset neza!")
            return redirect(url_for('aicos_req.asset'))
        except:
            flash("Ntabwo Asset yabashije kwinjira neza!")

    if category_form.validate_on_submit():
        category = AssetCategory(
            Category = category_form.Category.data,
            cooperative_id = current_user.department
        )
        try:
            db.session.add(category)
            db.session.commit()
            flash("Umaze kwinjiza Asset_Category neza!")
            return redirect(url_for('aicos_req.new_asset'))
        except:
            flash("Ntabwo Asset_Category yabashije kwinjira neza!")
    # else:
    #     flash('You are not allowed to add/change/delete anything')
    return render_template('/assets/new_asset.html',form=form,category_form=category_form)


@aicos_req.route('/assets/edit_asset<id>',methods=["GET","POST"])
def edit_asset(id):

    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    asset = assetsAccounting.query.filter_by(id=id).first()
    asset.Date = datetime.strptime(asset.Date,'%Y-%m-%d')
    category_form = AssetCategoryForm()
    form = AssetsForm(obj=asset)

    form.Date.data = asset.Date
    form.Category.data = asset.Category
    # form.Account.data = asset.Account
    form.Amount.data = asset.Amount
    form.Description.data = asset.Description

    if current_user == is_accountant:

        if form.validate_on_submit():
            Title = form.Title.data,
            asset.Date = form.Date.data
            asset.Category = form.Category.data
            # asset.Account = form.Account.data
            asset.Amount = form.Amount.data
            asset.Description = form.Description.data
            asset.cooperative_id = current_user.department
            try:
                db.session.commit()
                flash("Umaze Guhindura Asset neza!")
                return redirect(url_for('aicos_req.asset'))
            except:
                flash("Ntabwo Asset yabashije Guhindurwa neza!")
    return render_template('/assets/new_asset.html',form=form,category_form=category_form)

@aicos_req.route('/assets/delete_asset<id>',methods=["GET","POST"])
def delete_asset(id):
    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    if current_user == is_accountant:
        asset = assetsAccounting.query.filter_by(id=id).first()
        try:
            db.session.delete(asset)
            db.session.commit()
            flash("Umaze Gusiba Asset neza!")
            return redirect(url_for('aicos_req.asset'))
        except:
            flash("Ntabwo Asset yabashije Gusibwa neza!")
    else:
        flash("You have no right to delete an asset.")
    assetsAccountings = assetsAccounting.query.all()
    return render_template('/assets/asset.html',assets=assets,assetsAccountings=assetsAccountings)




@aicos_req.route('/accountingBooks/general/account', methods=["GET", "POST"])
def account():
    accounts = Account.query.all()
    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    form = AccountForm()

    if current_user == is_accountant:
        if form.validate_on_submit():
            account = Account(
                AccountName = form.AccountName.data,
                Description = form.Description.data,
                cooperative_id = current_user.department
            )
            try:
                db.session.add(account)
                db.session.commit()
                flash("Umaze kwinjiza Account neza!")
                return redirect(url_for('aicos_req.account'))
            except:
                flash("Ntabwo Account yabashije kwinjira neza!")
    return render_template('/accountingBooks/general/account.html',accounts=accounts,form=form)


@aicos_req.route('/accountingBooks/general/edit_account<id>',methods=["GET","POST"])
def edit_account(id): 
    account = Account.query.filter_by(id=id).first()
    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    form = AccountForm(obj=account)

    form.AccountName.data = account.AccountName
    form.Amount.data = account.Amount
    form.Description.data = account.Description

    if current_user == is_accountant:

        if form.validate_on_submit():
            account.AccountName = form.AccountName.data
            account.Amount = form.Amount.data
            account.Description = form.Description.data
            account.cooperative_id = current_user.department
            try:
                db.session.commit()
                flash("Umaze Guhindura Account neza!")
                return redirect(url_for('aicos_req.account'))
            except:
                flash("Ntabwo Account yabashije Guhindurwa neza!")
    return render_template('/accountingBooks/general/account.html',form=form)

@aicos_req.route('/assets/delete_account<id>',methods=["GET","POST"])
def delete_account(id):
    form = AccountForm()
    account = Account.query.filter_by(id=id).first()
    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    if current_user == is_accountant:
        try:
            db.session.delete(account)
            db.session.commit()
            flash("Umaze Gusiba Account neza!")
            return redirect(url_for('aicos_req.account'))
        except:
            flash("Ntabwo Account yabashije Gusibwa neza!")
    else:
        flash("You have no right to delete an account.")
    accounts = Account.query.all()
    return render_template('/accountingBooks/general/account.html',accounts=accounts,form=form)





@aicos_req.route('/balance_sheet',methods=["GET","POST"])
def balance_sheet():
    today = date.today()

    # Assets = []

    # for asset in assetsAccounting.query.filter_by().all():
    #     if asset.Category!='Current'or'Investiments'or'Property, Plant and Equipment'or'Intangible'or'Others':
    #         Assets.append(asset)

    Liabilities = assetsAccounting.query.all()

    Current_assets = assetsAccounting.query.filter_by(Category='Current').all()
    Investiments_assets = assetsAccounting.query.filter_by(Category='Investiments').all() 
    Property_Plant_and_Equipment = assetsAccounting.query.filter_by(Category='Property').all()
    Intangible_assets = assetsAccounting.query.filter_by(Category='Intangible').all()
    Other_assets = assetsAccounting.query.filter_by(Category='Other').all()
    acc_depreciations = assetsAccounting.query.filter_by(Category='acc_depr').all()

    Current_liabilities = Liability.query.filter_by(Category='Current').all()
    Long_term_liabilities = Liability.query.filter_by(Category='Long_term').all() 
    Stockholders_equities = Stockholders_equity.query.all()

    assets = []
    liabilities = []
    stockholders_equities = []

    total_acc_dep = 0
    total_assets1 = 0
    total_assets = 0
    total_Assets = 0

    total_Current_assets = 0
    total_Investiments_assets = 0
    total_Property_Plant_and_Equipment = 0
    total_Intangible_assets = 0
    total_Other_assets = 0

    total_Current_liabilities = 0
    total_Long_term_liabilities = 0
    total_liabilities = 0
    total_stockholders_equity = 0

    

    for asset in Current_assets:
        if (str(asset.Date).split('-'))[0] == (str((date.today())).split('-'))[0]:
            assets.append(asset)
            total_Current_assets += int(asset.Amount) 

    for asset in Investiments_assets:
        if (str(asset.Date).split('-'))[0] == (str((date.today())).split('-'))[0]:
            assets.append(asset)
            total_Investiments_assets += int(asset.Amount) 

    for asset in Property_Plant_and_Equipment:
        if (str(asset.Date).split('-'))[0] == (str((date.today())).split('-'))[0]:
            assets.append(asset)
            total_Property_Plant_and_Equipment += int(asset.Amount) 

    for asset in Intangible_assets:
        if (str(asset.Date).split('-'))[0] == (str((date.today())).split('-'))[0]:
            assets.append(asset)
            total_Intangible_assets += int(asset.Amount) 

    for asset in Other_assets:
        if (str(asset.Date).split('-'))[0] == (str((date.today())).split('-'))[0]:
            assets.append(asset)
            total_Other_assets += int(asset.Amount) 

    # for asset in Assets:
    #     if (str(asset.Date).split('-'))[0] == (str((date.today())).split('-'))[0]:
    #         assets.append(asset)
    #         total_Assets += int(asset.Amount) 

    for asset in assets:
        total_assets1 += int(asset.Amount) 

    for acc_dep in acc_depreciations:
        total_acc_dep += int(acc_dep.Amount)

    
    total_assets = total_assets1 - total_acc_dep




    for liability in Current_liabilities:
        if (str(liability.Date).split('-'))[0] == (str((date.today())).split('-'))[0]:
            liabilities.append(liability) 
            total_Current_liabilities += int(liability.Amount)

    for liability in Long_term_liabilities:
        if (str(liability.Date).split('-'))[0] == (str((date.today())).split('-'))[0]:
            liabilities.append(liability) 
            total_Long_term_liabilities += int(liability.Amount)

    for stock in Stockholders_equities:
        if (str(stock.Date).split('-'))[0] == (str((date.today())).split('-'))[0]:
            stockholders_equities.append(stock)
            total_stockholders_equity += int(stock.Amount)

    total_liabilities = total_Current_liabilities + total_Long_term_liabilities
    total_liabilities_and_stockholders_equity = total_liabilities + total_stockholders_equity

    

    return render_template('/accountingBooks/general/balance_sheet.html',today=today,
        Current_assets=Current_assets,Investiments_assets=Investiments_assets,
        Property_Plant_and_Equipment=Property_Plant_and_Equipment,
        Intangible_assets=Intangible_assets,Other_assets=Other_assets,acc_depreciations=acc_depreciations,
        total_Current_assets=total_Current_assets,total_Investiments_assets=total_Investiments_assets,
        total_Property_Plant_and_Equipment=total_Property_Plant_and_Equipment,total_acc_dep=total_acc_dep,
        total_Intangible_assets=total_Intangible_assets,total_Other_assets=total_Other_assets,
        assets=assets,liabilities=liabilities,stockholders_equities=stockholders_equities,
        total_assets=total_assets,total_liabilities=total_liabilities,
        Current_liabilities=Current_liabilities,Long_term_liabilities=Long_term_liabilities,
        total_stockholders_equity=total_stockholders_equity,
        total_Current_liabilities=total_Current_liabilities,total_Long_term_liabilities=total_Long_term_liabilities,
        total_liabilities_and_stockholders_equity=total_liabilities_and_stockholders_equity)





@aicos_req.route('/liabilities', methods=["GET", "POST"])
def liability():
    liabilities = Liability.query.all()
    return render_template('/liabilities/liabilities.html',liabilities=liabilities)

@aicos_req.route('/liabilities/new_liability', methods=["GET", "POST"])
def new_liability():
    form = LiabilityForm()
    category_form = LiabilityCategoryForm()

    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    # if current_user == is_accountant:
    if form.validate_on_submit():
        liability = Liability(
            Date = form.Date.data,
            Category = form.Category.data,
            # Account = form.Account.data,
            Title = form.Title.data,
            Amount = form.Amount.data,
            Description = form.Description.data,
            cooperative_id = current_user.department
        )
        try:
            db.session.add(liability)
            db.session.commit()
            flash("Umaze kwinjiza Liability neza!")
            return redirect(url_for('aicos_req.liability'))
        except:
            flash("Ntabwo Liability yabashije kwinjira neza!")

    if category_form.validate_on_submit():
        category = LiabilityCategory(
            Category = category_form.Category.data,
            cooperative_id = current_user.department
        )
        try:
            db.session.add(category)
            db.session.commit()
            flash("Umaze kwinjiza Liability_Category neza!")
            return redirect(url_for('aicos_req.new_liability'))
        except:
            flash("Ntabwo Liability_Category yabashije kwinjira neza!")

    # else:
    #     flash("You're not allowed to change anything.")
    return render_template('/liabilities/new_liability.html',form=form,category_form=category_form)


@aicos_req.route('/liabilities/edit_liability<id>',methods=["GET","POST"])
def edit_liability(id):

    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    liability = Liability.query.filter_by(id=id).first()
    liability.Date = datetime.strptime(liability.Date,'%Y-%m-%d')
    category_form = LiabilityCategoryForm()
    form = LiabilityForm(obj=liability)

    form.Title.data = liability.Title
    form.Date.data = liability.Date
    form.Category.data = liability.Category
    # form.Account.data = liability.Account
    form.Amount.data = liability.Amount
    form.Description.data = liability.Description

    if current_user == is_accountant:

        if form.validate_on_submit():
            Title = form.Title.data,
            liability.Date = form.Date.data
            liability.Category = form.Category.data
            # liability.Account = form.Account.data
            liability.Amount = form.Amount.data
            liability.Description = form.Description.data
            liability.cooperative_id = current_user.department
            try:
                db.session.commit()
                flash("Umaze Guhindura Liability neza!")
                return redirect(url_for('aicos_req.liability'))
            except:
                flash("Ntabwo Liability yabashije Guhindurwa neza!")
    return render_template('/liabilities/new_liability.html',form=form,category_form=category_form)

@aicos_req.route('/liabilites/delete_liability<id>',methods=["GET","POST"])
def delete_liability(id):
    is_accountant = Employee.query.filter_by(is_accountant=True).first()
    if current_user == is_accountant:
        liability = Liability.query.filter_by(id=id).first()
        try:
            db.session.delete(liability)
            db.session.commit()
            flash("Umaze Gusiba Liability neza!")
            return redirect(url_for('aicos_req.liability'))
        except:
            flash("Ntabwo Asset yabashije Gusibwa neza!")
    else:
        flash("You have no right to delete an asset.")
    liabilities = Liability.query.all()
    return render_template('/liabilities/liabilities.html',liabilities=liabilities)


