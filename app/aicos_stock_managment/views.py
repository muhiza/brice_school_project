from flask import render_template, abort, flash, redirect, url_for, request
from . import aicos_stock_managment
from flask_login import current_user, login_required
from ..models import * 
from .forms import UmusaruroForm, InyongeraMusaruroForm, IbyakoreshejweForm, KonteZaBankForm, UmusarurobForm, IbihanoForm, IbindiForm, UmusanzuForm, IbiraraneForm

import flask_excel
import flask_excel as excel

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

def check_coop_admin():
    if not current_user.is_coop_admin:
        abort(403)


@aicos_stock_managment.route('/')
@login_required
def dashboard():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    #all_member_idd = Umusaruro.member_id
    
    umusaruro_resi = Umusarurob.query.filter_by(department_id=current_user.email).all()
    inyongera = InyongeraMusaruro.query.filter_by(department_id=current_user.email).all()
    #ibyakoze = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
    member_all = Employee.query.filter_by(department_id=current_user.email).all()

    return render_template('stock_dashboard.html', umusaruro_resi=umusaruro_resi, member_all=member_all, employees=employees, inyongera=inyongera)



@aicos_stock_managment.route('/stock')
@login_required
def stock():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    all_member_idd = Umusaruro.member_id
    
    umusaruro_resi = Umusaruro.query.filter_by(department_id=current_user.email).all()
    inyongera = InyongeraMusaruro.query.filter_by(department_id=current_user.email).all()
    #ibyakoze = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
    ibindi = Ibindi.query.filter_by(department_id=current_user.email).all()
    ibihano = Ibihano.query.filter_by(department_id=current_user.email).all()
    member_all = Employee.query.filter_by(department_id=current_user.email).all()
    ibirarane = Ibirarane.query.filter_by(department_id=current_user.email).all()
    imisanzu = Umusanzu.query.filter_by(department_id=current_user.email).all()
    umusaruro = Umusarurob.query.filter_by(department_id=current_user.email).all()

    return render_template('stock_manage.html',ibihano=ibihano,
                                               imisanzu = imisanzu,
                                               ibirarane = ibirarane,
                                               ibindi=ibindi,
                                               umusaruro_resi=umusaruro_resi, 
                                               member_all=member_all, 
                                               employees=employees,
                                               umusaruro = umusaruro, 
                                               inyongera=inyongera)


@aicos_stock_managment.route('/umusaruro', methods=['GET', 'POST'])
@login_required
def umusaruro():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    all_member_idd = Umusaruro.member_id
    
    umusaruro_resi = Umusaruro.query.filter_by(department_id=current_user.email).all()
    member_all = Employee.query.filter_by(department_id=current_user.email).all()

    return render_template('umusaruro.html', umusaruro_resi=umusaruro_resi, member_all=member_all, employees=employees)
    

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

@aicos_stock_managment.route('/injiza/umusaruro/<int:id>', methods=["GET","POST"])
@login_required
def injizaUmusaruro(id):
    check_admin()
    memberid = Member.query.get_or_404(id)
    member_name = Member.query.filter_by(id=memberid.id).first()


    if memberid is None:
        return redirect(url_for('aicos_stock_managment.umusaruro'))
    
    form = UmusarurobForm()

    
    if form.validate_on_submit():
        



        umusaruro = Umusarurob(
                            Quantity = form.Quantity.data,
                            RiceType = form.RiceType.data,
                            RiceAmount = form.RiceAmount.data,
                            UwoAsigaranye = form.UwoAsigaranye.data,
                            UwoKugurisha = int(form.Quantity.data) - int(form.UwoAsigaranye.data),
                            GutonozaAmount = form.Gutonoza.data,
                            AmafarangaUmusaruro1 =  (int(form.RiceAmount.data) * int(form.Quantity.data)) - int(form.Gutonoza.data),
                            member_id = memberid.id,
                            department_id = current_user.email
                         )

        try:
            db.session.add(umusaruro)
            db.session.commit()
            flash("Umaze kwandika umusaruro wa" + member_name.izina_ribanza + " " + member_name.izina_rikurikira)
            return redirect(url_for('aicos_stock_managment.stock'))
        except Exception:
            flash("Ntago amakuru watanze yashoboye kwakirwa neza!")
            return redirect(url_for('aicos_stock_managment.injizaUmusaruro', form=form, memberid=memberid, member_name=member_name))
    
    return render_template('record_umusaruro.html', form=form, memberid=memberid, member_name=member_name)


@aicos_stock_managment.route('/injiza/inyongeramusaruro/<int:id>', methods=['GET', 'POST'])
@login_required
def injizaInyongeramusaruro(id):
    check_admin()
    memberid = Member.query.get_or_404(id)
    member_name = Member.query.filter_by(id=memberid.id).first()
    inyongera = InyongeraMusaruro.query.filter_by(department_id=current_user.email).all()


    if memberid is None:
        return redirect(url_for('aicos_stock_managment.umusaruro'))

    form = InyongeraMusaruroForm()

    
    if form.validate_on_submit():

        amazina = member_name.izina_ribanza + " " + member_name.izina_rikurikira

        inyongeramusaruro = InyongeraMusaruro(
                                    InyongeraMusaruroType = form.InyongeraMusaruroType.data,
                                    Quantity = form.Quantity.data,
                                    Amount = form.Amount.data,
                                    Cypemetrine = form.Cypemetrine.data,
                                    Beam = form.Beam.data,
                                    ImbutoQuantity = form.ImbutoQuantity.data,
                                    ImbutoAmount = form.ImbutoAmount.data,
                                    Redevance = form.Redevance.data,
                                    umwakaWisarura = form.umwakaWisarura.data,
                                    member_id = memberid.id,
                                    department_id = current_user.email
                                    )

        try:
            db.session.add(inyongeramusaruro)
            db.session.commit()
            flash("Umaze kwinjiza neza inyongeramusaruro!")
            return redirect(url_for('aicos_stock_managment.stock'))
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

    form = UmusanzuForm()
    
    if form.validate_on_submit():
        imisanzu = Umusanzu(
                            UmusanzuType = form.UmusanzuType.data,
                            Amount = form.Amount.data,
                            Comment = form.Comment.data,
                            member_id = memberid.id,
                            department_id = current_user.email
                    )
        try:
            db.session.add(imisanzu)
            db.session.commit()
            flash('Umaze kwinjiza neza Umusanzu')
            return redirect(url_for('aicos_stock_managment.stock'))
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

    form = IbiraraneForm()

    
    if form.validate_on_submit():

        ibirarane = Ibirarane(
                            IdeniTime = form.IdeniTime.data,
                            IdeniAmount = form.IdeniAmount.data,
                            IdeniType = form.IbiraraneType.data,
                            IdeniQuantity = form.IdeniQuantity.data,
                            member_id = memberid.id,
                            department_id = current_user.email
                        )

        try:
            db.session.add(ibirarane)
            db.session.commit()
            flash('Umaze kwinjiza neza Ikirarane')
            return redirect(url_for('aicos_stock_managment.stock'))
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

    form = IbihanoForm()
    
    if form.validate_on_submit():
        ibihano = Ibihano(
                        Igihano = form.Igihano.data,
                        IgihanoAmount = int(form.IgihanoAmount.data),
                        comment = form.Comment.data,
                        member_id = memberid.id,
                        department_id = current_user.email
                    )

        try:
            db.session.add(ibihano)
            db.session.commit()
            flash('Umaze kwandi igihano neza')
            return redirect(url_for('aicos_stock_managment.stock'))
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

    form = IbindiForm()

    if form.validate_on_submit():
        ibindi = Ibindi(
                    ImifukaQuantity = int(form.ImifukaQuantity.data),
                    ImifukaAmount = int(form.ImifukaAmount.data),
                    MituelleAmount = int(form.MituelleAmount.data),
                    UmuceriGrade   = int(form.UmuceriGrade.data),
                    UmuceriQuantity = int(form.UmuceriQuantity.data),
                    UmuceriAmountGrade = int(form.UmuceriAmountGrade.data),
                    Avence = int(form.Avence.data),
                    member_id = memberid.id,
                    department_id = current_user.email
                    )

        try:
            db.session.add(ibindi)
            db.session.commit()
            flash("Umaze kwinjiza Ibindi bisabwa neza")
            return redirect(url_for('aicos_stock_managment.stock'))
        except Exception:
            flash("kwinjiza Ibindi bisabwa ntibyakunze")
            return redirect(url_for('aicos_stock_managment.injizaIbindi', id=memberid))

    return render_template("/record_ibindi.html", form=form, memberid=memberid, member_name=member_name)






