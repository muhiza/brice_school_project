from flask import render_template, abort, flash, redirect, url_for, request
from . import aicos_stock_managment
from flask_login import current_user, login_required
from ..models import * 
from .forms import UmusaruroForm, InyongeraMusaruroForm, IbyakoreshejweForm, KonteZaBankForm, UmusarurobForm, IbihanoForm, IbindiForm, UmusanzuForm, IbiraraneForm

import flask_excel
from flask import Markup
import flask_excel as excel


from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from decimal import Decimal


import nexmo

import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

client = nexmo.Client(key='e7096025', secret='ab848459dae27b51')


def check_admin():
    if not current_user.is_admin:
        abort(403)

def check_overall():
    if not current_user.is_overall:
        abort(403)


def check_accountant():
    if not current_user.is_accountant:
        abort(403)


def check_coop_admin():
    if not current_user.is_coop_admin:
        abort(403)



session = sessionmaker()()





@aicos_stock_managment.route('/')
@login_required
def dashboard():
    #check_admin()
    #check_coop_admin()
    #if current_user.is_manager:

    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    #all_member_idd = Umusaruro.member_id
    memberss = Member.query.filter_by(department_id=current_user.email).all()
    umusaruro_resi = Umusarurob.query.filter_by(department_id=current_user.email).all()
    inyongera = InyongeraMusaruro.query.filter_by(department_id=current_user.email).all()
    #ibyakoze = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
    member_all = Employee.query.filter_by(department_id=current_user.email).all()
    ibirarane = Ibirarane.query.filter_by(department_id=current_user.email).all()
    imisanzu = Umusanzu.query.filter_by(department_id=current_user.email).all()
    umusaruro = Umusarurob.query.filter_by(department_id=current_user.email).all()
    inyongeramusaruro = InyongeraMusaruro.query.filter_by(department_id=current_user.email).all()


    return render_template('stock_dashboard.html', 
                                                ibirarane=ibirarane, 
                                                imisanzu=imisanzu, 
                                                umusaruro=umusaruro, 
                                                inyongeramusaruro=inyongeramusaruro,
                                                umusaruro_resi=umusaruro_resi, 
                                                member_all=member_all,
                                                inyongera=inyongera,
                                                memberss=memberss
                                                )





















@aicos_stock_managment.route('/stock')
@login_required
def stock():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    all_member_idd = Umusaruro.member_id
    memberss = Member.query.all()
    umusaruro_resi = Umusaruro.query.filter_by(department_id=current_user.email).all()
    inyongera = InyongeraMusaruro.query.filter_by(department_id=current_user.email).all()
    #ibyakoze = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
    ibindi = Ibindi.query.all()
    ibihano = Ibihano.query.all()
    member_all = Employee.query.filter_by(department_id=current_user.email).all()
    ibirarane = Ibirarane.query.filter_by(department_id=current_user.email).all()
    imisanzu = Umusanzu.query.filter_by(department_id=current_user.email).all()
    umusaruro = Umusarurob.query.all()
    inyongeramusaruro = InyongeraMusaruro.query.all()


    return render_template('stock_manage.html',ibihano=ibihano,
                                               imisanzu = imisanzu,
                                               ibirarane = ibirarane,
                                               ibindi=ibindi,
                                               umusaruro_resi=umusaruro_resi, 
                                               member_all=member_all, 
                                               employees=employees,
                                               umusaruro = umusaruro, 
                                               inyongera=inyongera,
                                               memberss=memberss,
                                               employee=employee,
                                               )


@aicos_stock_managment.route('/umusaruro', methods=['GET', 'POST'])
@login_required
def umusaruro():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    all_member_idd = Umusarurob.member_id
    umusaruro_resi = Umusarurob.query.all()
    member_all = Employee.query.filter_by(department_id=current_user.email).all()

    return render_template('umusaruro.html', umusaruro_resi=umusaruro_resi, member_all=member_all, employees=employees)
    
@aicos_stock_managment.route('/umusaruro/member/<int:id>')
@login_required
def ibindiUmusaruro(id):
    memberId = Member.query.get_or_404(id)
    umusaruro = Umusarurob.query.filter_by(member_id=memberId.id).all()


    
    umusaruro_all = db.session.query(func.sum(Umusarurob.UwoKugurisha)).filter_by(member_id=memberId.id).scalar()
    amafaranga_all = db.session.query(func.sum(Umusarurob.RiceAmount)).filter_by(member_id=memberId.id).scalar()
    amafaranga_asigaye = Decimal(db.session.query(func.sum(Umusarurob.Asigaye)).filter_by(member_id=memberId.id).scalar())

    price = amafaranga_all / umusaruro_all

    amafaranga_asigaye = Decimal(db.session.query(func.sum(Umusarurob.Asigaye)).filter_by(member_id=memberId.id).scalar())

    return render_template('ibindiUmusaruro.html', memberId=memberId, price=price, umusaruro=umusaruro, umusaruro_all=umusaruro_all, amafaranga_asigaye=amafaranga_asigaye, amafaranga_all=amafaranga_all)




@aicos_stock_managment.route('/umusaruro/member/ishyura/<int:id>')
@login_required
def umunyamuryangoIshyura(id):
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members

    memberId = Member.query.get_or_404(id)
    umusaruro = Umusarurob.query.filter_by(member_id=memberId.id).all()
    umusaruro_all = db.session.query(func.sum(Umusarurob.UwoKugurisha)).filter_by(member_id=memberId.id).scalar()
    amafaranga_all = db.session.query(func.sum(Umusarurob.RiceAmount)).filter_by(member_id=memberId.id).scalar()

    return render_template('ishyuraByose.html', memberId=memberId, umusaruro=umusaruro, umusaruro_all=umusaruro_all, amafaranga_all=amafaranga_all, employees=employees)






@aicos_stock_managment.route('/umusaruro/member/ishyura/<int:id>', methods=['GET'])
@login_required
def umusaruroIshyura(id):
    umusaruroId = Umusarurob.query.get_or_404(id)
    member = Member.query.filter_by(member_id=umusaruroId.member_id)
    
    ayishyurwa = Abishyuwe(
                amount_payed = 50000,
                member_id = member.id,
                member_name = member.izina_ribanza + " " + member.izina_rikurikira,
                ibiro = umusaruroId.UwoKugurisha,
                umusaruro_id = umusaruroId.id,
                department_id = current_user.email
                )
    try:
        db.session.add(ayishyurwa)
        db.session.commit()
        return redirect(url_for('aicos_stock_managment.ibindiUmusaruro', id=umusaruroId.member_id))
    except Exception as e:
        return redirect(url_for('aicos_stock_managment.umusaruro'))



@aicos_stock_managment.route('/inyongeramusaruro')
@login_required
def inyongeramusaruro():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    inyongera = InyongeraMusaruro.query.filter_by(department_id=current_user.email).all()
    return render_template('inyongeramusaruro.html', inyongera=inyongera, employees=employees)


@aicos_stock_managment.route('/ibyakoreshejwe')
@login_required
def ibyakoreshejwe():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    ibyakoreshejwe = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
    return render_template('ibyakoreshejwe.html', ibyakoreshejwe=ibyakoreshejwe, employees=employees)

@aicos_stock_managment.route('/imisanzu')
@login_required
def imisanzu():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    imisanzu = Umusanzu.query.filter_by(department_id=current_user.email).all()
    return render_template('imisanzu.html', employees=employees, imisanzu=imisanzu) 

@aicos_stock_managment.route('/ibirarane')
@login_required
def ibirarane():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    ibirarane = Ibirarane.query.filter_by(department_id=current_user.email).all()
    return render_template('ibirarane.html', employees=employees, ibirarane=ibirarane)

@aicos_stock_managment.route('/ibihano')
@login_required
def ibihano():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    ibihano = Ibihano.query.filter_by(department_id=current_user.email).all()
    return render_template('ibihano.html', employees=employees, ibihano=ibihano)

@aicos_stock_managment.route('/ibindi')
@login_required
def ibindi():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    ibindi = Ibindi.query.filter_by(department_id=current_user.email).all()
    return render_template('ibindi.html', employees=employees, ibindi=ibindi)

@aicos_stock_managment.route('/injiza/umusaruro/<int:id>', methods=["GET","POST"])
@login_required
def injizaUmusaruro(id):
    check_admin()
    memberid = Member.query.get_or_404(id)
    member_name = Member.query.filter_by(id=memberid.id).first()


    if member_name is None:
        flash("Umunyamuryango usabye ntawuhari")
        return redirect(url_for('aicos_stock_managment.umusaruro'))
    if member_name.izina_ribanza is None:
        flash("Habaye ikibazo kwizina ry\'umunyamuryango")
        return redirect(url_for('aicos_stock_managment.umusaruro'))
    if member_name.izina_rikurikira is None:
        flash("Habaye ikibazo kwizina ry\'umunyamuryango")
        return redirect(url_for('aicos_stock_managment.umusaruro'))
    
    form = UmusarurobForm()

    
    if form.validate_on_submit():
        
        if form.UwoAsigaranye.data is None:
            form.UwoAsigaranye.data = 0
        if form.Gutonoza.data is None:
            form.Gutonoza.data = 0
        if form.UwoAsigaranye.data is None:
            form.UwoAsigaranye.data = 0
        if form.Quantity.data is None:
            form.Quantity.data = 0
        if form.RiceAmount.data is None:
            form.RiceAmount.data = 0
        if form.UmusaruroGrade.data is None:
            form.UmusaruroGrade.data = 0



        if form.UmusaruroGrade.data == 'good':
            umusaruro = Umusarurob(
                                RiceType = form.RiceType.data,
                                RicePrice = form.RiceAmount.data,
                                RiceAmount = int(form.RiceAmount.data) * form.Quantity.data,
                                UmusaruroGrade = form.UmusaruroGrade.data,
                                UwoAsigaranye = form.UwoAsigaranye.data,
                                UwoKugurisha = (form.Quantity.data) - (form.UwoAsigaranye.data),
                                GutonozaAmount = int(form.Gutonoza.data) * int(form.UwoAsigaranye.data),
                                AmafarangaUmusaruro1 =  (int(form.RiceAmount.data) * (int(form.Quantity.data) - \
                                                        int(form.UwoAsigaranye.data)) - (int(form.Gutonoza.data) * \
                                                        int(form.UwoAsigaranye.data))) + 10 * form.RiceAmount.data * form.Quantity.data / 100,
                                Asigaye     = 10 * form.Quantity.data / 100,
                                member_id = memberid.id,
                                department_id = current_user.email
                             )


        elif form.UmusaruroGrade.data == 'normal':
            umusaruro = Umusarurob(
                                RiceType = form.RiceType.data,
                                RicePrice = form.RiceAmount.data,
                                RiceAmount = int(form.RiceAmount.data) * form.Quantity.data,
                                UmusaruroGrade = form.UmusaruroGrade.data,
                                UwoAsigaranye = form.UwoAsigaranye.data,
                                UwoKugurisha = (form.Quantity.data) - (form.UwoAsigaranye.data),
                                GutonozaAmount = int(form.Gutonoza.data) * int(form.UwoAsigaranye.data),
                                AmafarangaUmusaruro1 =  (int(form.RiceAmount.data) * (int(form.Quantity.data) - \
                                                        int(form.UwoAsigaranye.data)) - (int(form.Gutonoza.data) * \
                                                        int(form.UwoAsigaranye.data))) + 0,
                                Asigaye     = 10 * form.Quantity.data / 100,
                                member_id = memberid.id,
                                department_id = current_user.email
                             )



        else:
            umusaruro = Umusarurob(
                                RiceType = form.RiceType.data,
                                RicePrice = form.RiceAmount.data,
                                RiceAmount = int(form.RiceAmount.data) * form.Quantity.data,
                                UmusaruroGrade = form.UmusaruroGrade.data,
                                UwoAsigaranye = form.UwoAsigaranye.data,
                                UwoKugurisha = (form.Quantity.data) - (form.UwoAsigaranye.data),
                                GutonozaAmount = int(form.Gutonoza.data) * int(form.UwoAsigaranye.data),
                                AmafarangaUmusaruro1 =  (int(form.RiceAmount.data) * (int(form.Quantity.data) - \
                                                        int(form.UwoAsigaranye.data)) - (int(form.Gutonoza.data) * \
                                                        int(form.UwoAsigaranye.data))) - 10 * form.RiceAmount.data * form.Quantity.data / 100,
                                Asigaye     = 10 * form.Quantity.data / 100,
                                member_id = memberid.id,
                                department_id = current_user.email
                             )



        try:
            db.session.add(umusaruro)
            db.session.commit()
            flash(Markup("Umaze kwandika umusaruro wa " + "<b>" + member_name.izina_ribanza + " " + member_name.izina_rikurikira + "</b>"))
            return redirect(url_for('aicos_stock_managment.injizaUmusaruro'))
        except Exception:
            flash("Ntago amakuru watanze yashoboye kwakirwa neza!")
            return redirect(url_for('aicos_stock_managment.injizaUmusaruro', form=form, memberid=memberid, member_name=member_name, id=memberid.id))
    
    return render_template('record_umusaruro.html', form=form, memberid=memberid, member_name=member_name)


@aicos_stock_managment.route('/injiza/inyongeramusaruro/<int:id>', methods=['GET', 'POST'])
@login_required
def injizaInyongeramusaruro(id):
    check_admin()
    memberid = Member.query.get_or_404(id)
    member_name = Member.query.filter_by(id=memberid.id).first()
    inyongera = InyongeraMusaruro.query.filter_by(department_id=current_user.email).all()


    if memberid is None:
        flash("Umunyamuryango usabye ntawuhari")
        return redirect(url_for('aicos_stock_managment.inyongeramusaruro'))
    if member_name.izina_ribanza is None:
        flash("Habaye ikibazo kwizina ry\'umunyamuryango")
        return redirect(url_for('aicos_stock_managment.inyongeramusaruro'))
    if member_name.izina_rikurikira is None:
        flash("Habaye ikibazo kwizina ry\'umunyamuryango")
        return redirect(url_for('aicos_stock_managment.inyongeramusaruro'))

    form = InyongeraMusaruroForm()

    
    if form.validate_on_submit():

        if form.NPKkg.data is None:
            form.NPKkg.data = 0
        if form.UREA.data is None:
            form.UREA.data = 0
        if form.DAP.data is None:
            form.DAP.data = 0
        if form.KCL.data is None:
            form.KCL.data = 0
        if form.Briquette.data is None:
            form.Briquette.data = 0
        if form.ImbutoQuantity.data is None:
            form.ImbutoQuantity.data = 0
        if form.Cypemetrine.data is None:
            form.Cypemetrine.data = 0
        if form.Beam.data is None:
            form.Beam.data = 0
        if form.ImbutoQuantity.data is None:
            form.ImbutoQuantity.data = 0
        if form.Redevance.data is None:
            form.Redevance.data = 0

        inyongeramusaruro = InyongeraMusaruro(
                                NPKkg = form.NPKkg.data,
                                NPKPerUnity = form.NPKPerUnity.data,
                                UREA = form.UREA.data,
                                UREAPerUnity = form.UREAPerUnity.data,
                                DAP = form.DAP.data,
                                DAPPerUnity = form.DAPPerUnity.data,
                                KCL = form.KCL.data,
                                KCLPerUnity = form.KCLPerUnity.data,
                                Briquette = form.Briquette.data,
                                BriquettePerUnity = form.BriquettePerUnity.data,
                                Cypemetrine = form.Cypemetrine.data,
                                Beam = form.Beam.data,
                                ImbutoQuantity = form.ImbutoQuantity.data,
                                ImbutoAmount = form.ImbutoAmount.data,
                                Redevance = form.Redevance.data,
                                member_id = memberid.id,
                                department_id = current_user.email
                                )

        try:
            db.session.add(inyongeramusaruro)
            db.session.commit()
            flash("Umaze kwinjiza neza inyongeramusaruro!")
            return redirect(url_for('aicos_stock_managment.inyongeramusaruro'))
        except:
            flash("Resi Winjije nta musaruro wayo wabonetse!")
            return redirect(url_for('aicos_stock_managment.injizaInyongeramusaruro', form=form, id=memberid.id, memberid=memberid.id, member_name=member_name))
        
    return render_template('/record_inyongeramusaruro.html', form=form, memberid=memberid, member_name=member_name)


@aicos_stock_managment.route('/injiza/ibyakoreshejwe/<int:id>', methods=['GET', 'POST'])
def injizaIbyakoreshejwe(id):
    check_admin()
    check_coop_admin()
    memberid = Member.query.get_or_404(id)
    member_name = Member.query.filter_by(id=memberid.id).first()


    form = IbyakoreshejweForm()



    if form.validate_on_submit():

        amazina = member_name.izina_ribanza + " " + member_name.izina_rikurikira

        ibyakoreshejwe = Ibyakoreshejwe(
                                InyongeraMusaruroType = form.InyongeraMusaruroType.data,
                                Quantity = form.Quantity.data,
                                Amount = form.Amount.data,
                                Cypemetrine = form.Cypemetrine.data,
                                Beam = form.Beam.data,
                                ImbutoQuantity = form.ImbutoQuantity.data,
                                ImbutoAmount = form.ImbutoAmount.data,
                                Redevance = form.Redevance.data,
                                member_id = memberid.id,
                                department_id = current_user.email
                                )

        try:
            db.session.add(ibyakoreshejwe)
            db.session.commit()

            flash("Winjije neza ibyakoreshejwe uyu mwaka!")
            return redirect(url_for('aicos_stock_managment.ibyakoreshejwe'))
        except Exception:
            flash("Ibyo mumaze gukora Ntabwo byakunze neza Ongera ugerageze!")
            return redirect(url_for('aicos_stock_managment.injizaIbyakoreshejwe', memberid=memberid, member_name=member_name))

    return render_template('/record_ibyakoreshejwe.html', form=form, memberid=memberid, member_name=member_name)


@aicos_stock_managment.route('/banki/konte')
def konteZaBanki():
    check_admin
    check_coop_admin()
    konte = CoopMemberBankAccounts.query.filter_by(department_id=current_user.email).all()
    return render_template("/bankiZacu.html", konte=konte)  

@aicos_stock_managment.route('/injiza/konte', methods=['GET', 'POST'])
def injizaKonte():
    check_admin()
    form = KonteZaBankForm()

    
    if form.validate_on_submit():
        coopMemberBankAccounts = CoopMemberBankAccounts(
                                    memberName= form.izinaryaNyiriKonte.data,
                                    bankName= form.izanaRyaBank.data,
                                    bankAccountNumber= form.numeroYaKonte.data,
                                    department_id=current_user.email)

        try:
            db.session.add(coopMemberBankAccounts)
            db.session.commit()
            flash("Winjije neza nimero ya banki")
            return redirect(url_for('aicos_stock_managment.konteZaBanki'))
        except Exception:
            flash("Ibyo wemeje ntabwo bimeze neza Ongera ugerageze!")
            return redirect(url_for('aicos_stock_managment.injizaKonte'))

    return render_template("/record_bankAccount.html", form=form)      


@aicos_stock_managment.route('/injiza/imisanzu/<int:id>', methods=['GET', 'POST'])
def injizaImisanzu(id):
    check_admin()
    check_coop_admin()
    memberid = Member.query.get_or_404(id)
    member_name = Member.query.filter_by(id=memberid.id).first()

    if memberid is None:
        flash("")
        return redirect(url_for('aicos_stock_managment.imisanzu'))
    if member_name.izina_ribanza is None:
        flash("Habaye ikibazo kwizina ry\'umunyamuryango")
        return redirect(url_for('aicos_stock_managment.imisanzu'))
    if member_name.izina_rikurikira is None:
        flash("Habaye ikibazo kwizina ry\'umunyamuryango")
        return redirect(url_for('aicos_stock_managment.imisanzu'))

    form = UmusanzuForm()
    
    if form.validate_on_submit():

        if form.UmusoroWakarere.data is None:
            form.UmusoroWakarere.data = 0
        if form.UmusanzuCoop.data is None:
            form.UmusanzuCoop.data = 0
        if form.Umugabane.data is None:
            form.Umugabane.data = 0
        if form.Ikigega.data is None:
            form.Ikigega.data = 0
        if form.KuzibaIcyuho.data is None:
            form.KuzibaIcyuho.data = 0

        imisanzu = Umusanzu(
                            UmusoroWakarere = form.UmusoroWakarere.data,
                            UmusanzuCoop = form.UmusanzuCoop.data,
                            Umugabane = form.Umugabane.data,
                            Ikigega = form.Ikigega.data,
                            KuzibaIcyuho = form.KuzibaIcyuho.data,
                            member_id = memberid.id,
                            department_id = current_user.email
                    )
        try:
            db.session.add(imisanzu)
            db.session.commit()
            flash('Umaze kwinjiza neza Umusanzu')
            return redirect(url_for('aicos_stock_managment.imisanzu'))
        except Exception:
            flash('Kwinjiza Umusanzu ntibyakunze')
            return redirect(url_for('aicos_stock_managment.injizaImisanzu', id=memberid.id))

    

    return render_template("/record_imisanzu.html", form=form, memberid=memberid, member_name=member_name)


@aicos_stock_managment.route('/injiza/ibirarane/<int:id>', methods=['GET', 'POST'])
def injizaIbirarane(id):
    check_admin()
    check_coop_admin()
    memberid = Member.query.get_or_404(id)
    member_name = Member.query.filter_by(id=memberid.id).first()

    if memberid is None:
        flash("Umunyamuryango ntabwo abonetse")
        return redirect(url_for('aicos_stock_managment.ibirarane'))
    if member_name.izina_ribanza is None:
        flash("Habaye ikibazo kwizina ry\'umunyamuryango")
        return redirect(url_for('aicos_stock_managment.ibirarane'))
    if member_name.izina_rikurikira is None:
        flash("Habaye ikibazo kwizina ry\'umunyamuryango")
        return redirect(url_for('aicos_stock_managment.ibirarane'))

    form = IbiraraneForm()

    
    if form.validate_on_submit():

        if form.NPKkg.data is None:
            form.NPKkg.data = 0
        if form.UREA.data is None:
            form.UREA.data = 0
        if form.DAP.data is None:
            form.DAP.data = 0
        if form.KCL.data is None:
            form.KCL.data = 0
        if form.ImbutoQuantity.data is None:
            form.ImbutoQuantity.data = 0
        if form.IdeniAmount.data is None:
            form.IdeniAmount.data = 0
        if form.Briquette.data is None:
            form.Briquette.data = 0



        ibirarane = Ibirarane(
                            NPKkg = form.NPKkg.data,
                            NPKPerUnity = form.NPKPerUnity.data,
                            UREA = form.UREA.data,
                            UREAPerUnity = form.UREAPerUnity.data,
                            DAP = form.DAP.data,
                            DAPPerUnity = form.DAPPerUnity.data,
                            KCL = form.KCL.data,
                            KCLPerUnity = form.KCLPerUnity.data,
                            ImbutoQuantity = form.ImbutoQuantity.data,
                            ImbutoAmount = form.ImbutoAmount.data,
                            IdeniAmount = form.IdeniAmount.data,
                            Briquette = form.Briquette.data,
                            BriquettePerUnity = form.BriquettePerUnity.data,
                            member_id = memberid.id,
                            department_id = current_user.email
                        )

        try:
            db.session.add(ibirarane)
            db.session.commit()
            flash('Umaze kwinjiza neza Ikirarane')
            return redirect(url_for('aicos_stock_managment.ibirarane'))
        except Exception:
            flash('Kwandika Ikirarane ntibyakunze')
            return redirect(url_for('aicos_stock_managment.injizaIbirarane', id=memberid.id))

    return render_template("/record_ibirarane.html", form=form, memberid=memberid, member_name=member_name)


@aicos_stock_managment.route('/injiza/ibihano/<int:id>', methods=['GET', 'POST'])
def injizaIbihano(id):
    check_admin()
    check_coop_admin()
    memberid = Member.query.get_or_404(id)
    member_name = Member.query.filter_by(id=memberid.id).first()

    if memberid is None:
        flash("Ntabwo Umunyamuryango abonetse")
        return redirect(url_for('aicos_stock_managment.ibihano'))
    if member_name.izina_ribanza is None:
        flash("Habaye ikibazo kwizina ry\'umunyamuryango")
        return redirect(url_for('aicos_stock_managment.ibihano'))
    if member_name.izina_rikurikira is None:
        flash("Habaye ikibazo kwizina ry\'umunyamuryango")
        return redirect(url_for('aicos_stock_managment.ibihano'))

    form = IbihanoForm()
    
    if form.validate_on_submit():

        if form.AmandeC.data is None:
            form.AmandeC.data = 0
        if form.AmandeApII.data is None:
            form.AmandeApII.data = 0

        ibihano = Ibihano(
                        AmandeC = form.AmandeC.data,
                        AmandeApII = form.AmandeApII.data,
                        comment = form.Comment.data,
                        member_id = memberid.id,
                        department_id = current_user.email
                    )

        try:
            db.session.add(ibihano)
            db.session.commit()
            flash('Umaze kwandi igihano neza')
            return redirect(url_for('aicos_stock_managment.ibihano'))
        except Exception:
            flash('Kwandika igihano ntabwo byakunze')
            return redirect(url_for('aicos_stock_managment.injizaIbindi', id=memberid.id))

    
    return render_template("/record_ibihano.html", form=form, memberid=memberid, member_name=member_name)



@aicos_stock_managment.route('/injiza/ibindi/<int:id>', methods=['GET', 'POST'])
def injizaIbindi(id):
    check_admin()
    check_coop_admin()
    memberid = Member.query.get_or_404(id)
    member_name = Member.query.filter_by(id=memberid.id).first()

    if memberid is None:
        flash("Ntabwo Umunyamuryango abonetse")
        return redirect(url_for('aicos_stock_managment.ibindi'))
    if member_name.izina_ribanza is None:
        flash("Habaye ikibazo kwizina ry\'umunyamuryango")
        return redirect(url_for('aicos_stock_managment.ibindi'))
    if member_name.izina_rikurikira is None:
        flash("Habaye ikibazo kwizina ry\'umunyamuryango")
        return redirect(url_for('aicos_stock_managment.ibindi'))

    form = IbindiForm()

    if form.validate_on_submit():

        if form.ImifukaQuantity.data is None:
            form.ImifukaQuantity.data = 0
        if form.ImifukaAmount.data is None:
            form.ImifukaAmount.data = 0
        if form.MituelleAmount.data is None:
            form.MituelleAmount.data = 0
        if form.UmuceriGrade.data is None:
            form.UmuceriGrade.data = 0
        if form.UmuceriQuantity.data is None:
            form.UmuceriQuantity.data = 0
        if form.UmuceriAmountGrade.data is None:
            form.UmuceriAmountGrade.data = 0
        if form.Avence.data is None:
            form.Avence.data = 0

        ibindi = Ibindi(
                    ImifukaQuantity = form.ImifukaQuantity.data,
                    ImifukaAmount = int(form.ImifukaAmount.data) * int(form.ImifukaQuantity.data),
                    MituelleAmount = form.MituelleAmount.data,
                    UmuceriGrade   = form.UmuceriGrade.data,
                    UmuceriQuantity = form.UmuceriQuantity.data,
                    UmuceriAmountGrade = (form.UmuceriAmountGrade.data) * (form.UmuceriQuantity.data),
                    Avence = form.Avence.data,
                    member_id = memberid.id,
                    department_id = current_user.email
                    )

        try:
            db.session.add(ibindi)
            db.session.commit()
            flash("Umaze kwinjiza Ibindi bisabwa neza")
            return redirect(url_for('aicos_stock_managment.ibindi'))
        except Exception:
            flash("kwinjiza Ibindi bisabwa ntibyakunze")
            return redirect(url_for('aicos_stock_managment.injizaIbindi', id=memberid.id))
            session.rollback()

    return render_template("/record_ibindi.html", form=form, memberid=memberid, member_name=member_name)






@aicos_stock_managment.route('/imyishyurire', methods=['GET', 'POST'])
@login_required
def Imyishyurire():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    all_member_idd = Umusarurob.member_id
    umusaruro_resi = Umusarurob.query.all()
    member_all = Employee.query.filter_by(department_id=current_user.email).all()

    return render_template('imyishyurire.html', umusaruro_resi=umusaruro_resi, member_all=member_all, employees=employees)
