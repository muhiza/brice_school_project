from flask import render_template, abort, flash, redirect, url_for, request
from . import aicos_stock_managment
from flask_login import current_user, login_required
from ..models import *
from .forms import UmusaruroForm, InyongeraMusaruroForm, IbyakoreshejweForm, KonteZaBankForm, UmusarurobForm, IbihanoForm, IbindiForm, UmusanzuForm, IbiraraneForm

import flask_excel
from flask import Markup
import flask_excel as excel
import requests

from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from decimal import Decimal


import nexmo

import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

client = nexmo.Client(key='e7096025', secret='ab848459dae27b51')

from time import gmtime, strftime
get_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())



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
    # check_admin()
    # check_coop_admin()
    # if current_user.is_manager:

    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    #all_member_idd = Umusaruro.member_id
    memberss = Member.query.filter_by(department_id=current_user.email).all()
    umusaruro_resi = Umusarurob.query.filter_by(
        department_id=current_user.email).all()
    inyongera = InyongeraMusaruro.query.filter_by(
        department_id=current_user.email).all()
    #ibyakoze = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
    member_all = Employee.query.filter_by(
        department_id=current_user.email).all()
    ibirarane = Ibirarane.query.filter_by(
        department_id=current_user.email).all()
    imisanzu = Umusanzu.query.filter_by(department_id=current_user.email).all()
    umusaruro = Umusarurob.query.filter_by(
        department_id=current_user.email).all()
    inyongeramusaruro = InyongeraMusaruro.query.filter_by(
        department_id=current_user.email).all()

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
    umusaruro_resi = Umusaruro.query.filter_by(
        department_id=current_user.email).all()
    inyongera = InyongeraMusaruro.query.filter_by(
        department_id=current_user.email).all()
    #ibyakoze = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
    ibindi = Ibindi.query.all()
    ibihano = Ibihano.query.all()
    member_all = Employee.query.filter_by(
        department_id=current_user.email).all()
    ibirarane = Ibirarane.query.filter_by(
        department_id=current_user.email).all()
    imisanzu = Umusanzu.query.filter_by(department_id=current_user.email).all()
    umusaruro = Umusarurob.query.all()
    inyongeramusaruro = InyongeraMusaruro.query.all()

    return render_template('stock_manage.html', ibihano=ibihano,
                           imisanzu=imisanzu,
                           ibirarane=ibirarane,
                           ibindi=ibindi,
                           umusaruro_resi=umusaruro_resi,
                           member_all=member_all,
                           employees=employees,
                           umusaruro=umusaruro,
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
    member_all = Employee.query.filter_by(
        department_id=current_user.email).all()
    
    coop_activity = Department.query.filter_by(email=current_user.email).first()
    act = coop_activity.Activity


    stock_season1 = Arc_stock.query.filter_by(department_id=current_user.email).filter_by(season='2018_19_season_a')
    stock_season2 = Arc_stock.query.filter_by(department_id=current_user.email).filter_by(season='2019_season_b')
    stock_season3 = Arc_stock.query.filter_by(department_id=current_user.email).filter_by(season='2019_season_c')
    stock_season4 = Arc_stock.query.filter_by(department_id=current_user.email).filter_by(season='2019_2020_season_a')


    

    #stock_season = stock_season_all.season.filter_by(season='2019_2020_season_a')
    #season_1 = stock_season.season

    return render_template('umusaruro.html', act=act, umusaruro_resi=umusaruro_resi, member_all=member_all, employees=employees, 
                                             stock_season1=stock_season1, stock_season2=stock_season2, stock_season3=stock_season3,
                                             stock_season4=stock_season4)


@aicos_stock_managment.route('/umusaruro/member/<int:id>')
@login_required
def ibindiUmusaruro(id):
    memberId = Member.query.get_or_404(id)
    umusaruro = Umusarurob.query.filter_by(member_id=memberId.id).all()

    musa = 10000
    avance = 5000

    carnet = 500
    rpf = 100
    ejo_heza = 1500
    inguzanyo = 0
    ejo_heza_2 = 1250

    retenue = musa+carnet+avance+inguzanyo+ejo_heza+rpf

    umusaruro_all = db.session.query(func.sum(Umusarurob.UwoKugurisha)).filter_by(
        member_id=memberId.id).scalar()
    amafaranga_all = db.session.query(func.sum(Umusarurob.RiceAmount)).filter_by(
        member_id=memberId.id).scalar()
    amafaranga_asigaye = Decimal(db.session.query(
        func.sum(Umusarurob.Asigaye)).filter_by(member_id=memberId.id).scalar())

    price = amafaranga_all / umusaruro_all

    amafaranga_asigaye = Decimal(db.session.query(
        func.sum(Umusarurob.Asigaye)).filter_by(member_id=memberId.id).scalar())
    
    ibyabuze_amanota = Umusarurob.query.filter_by(member_id=memberId.id).filter_by(UmusaruroGrade='bad').count()
    
    ibiro_ibyabuze_amanota = db.session.query(func.sum(Umusarurob.UwoKugurisha)).filter_by(member_id=memberId.id).filter_by(UmusaruroGrade='bad').scalar()
    
    coop_activity = Department.query.filter_by(email=current_user.email).first()
    act = coop_activity.Activity



    igiciro_uruganda = 10 * 191 / 100

    if ibiro_ibyabuze_amanota is None:
        amafaranga_ibyabuze_amanota = 0
    else:
        amafaranga_ibyabuze_amanota = Decimal(igiciro_uruganda) * Decimal(ibiro_ibyabuze_amanota - (10 * ibiro_ibyabuze_amanota / 100))



    return render_template('ibindiUmusaruro.html', act=act, retenue = retenue, inguzanyo=inguzanyo, ejo_heza=ejo_heza, rpf=rpf, carnet=carnet, avance=avance, musa=musa, ibiro_ibyabuze_amanota=ibiro_ibyabuze_amanota, amafaranga_ibyabuze_amanota=amafaranga_ibyabuze_amanota, ibyabuze_amanota=ibyabuze_amanota, memberId=memberId, price=price, umusaruro=umusaruro, umusaruro_all=umusaruro_all, amafaranga_asigaye=amafaranga_asigaye, amafaranga_all=amafaranga_all)


@aicos_stock_managment.route('/umusaruro/member/ishyura/<int:id>')
@login_required
def umunyamuryangoIshyura(id):
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members

    memberId = Member.query.get_or_404(id)
    umusaruro = Umusarurob.query.filter_by(member_id=memberId.id).all()
    umusaruro_all = db.session.query(func.sum(Umusarurob.UwoKugurisha)).filter_by(
        member_id=memberId.id).scalar()
    amafaranga_all = db.session.query(func.sum(Umusarurob.RiceAmount)).filter_by(
        member_id=memberId.id).scalar()
    price = amafaranga_all / umusaruro_all

    return render_template('ishyuraByose.html', memberId=memberId, price=price, umusaruro=umusaruro, umusaruro_all=umusaruro_all, amafaranga_all=amafaranga_all, employees=employees)


@aicos_stock_managment.route('/umusaruro/member/ishyura/<int:id>', methods=['GET'])
@login_required
def umusaruroIshyura(id):
    umusaruroId = Umusarurob.query.get_or_404(id)
    member = Member.query.filter_by(member_id=umusaruroId.member_id)

    ayishyurwa = Abishyuwe(
        amount_payed=50000,
        member_id=member.id,
        member_name=member.izina_ribanza + " " + member.izina_rikurikira,
        ibiro=umusaruroId.UwoKugurisha,
        umusaruro_id=umusaruroId.id,
        department_id=current_user.email
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
    inyongera = InyongeraMusaruro.query.filter_by(
        department_id=current_user.email).all()
    return render_template('inyongeramusaruro.html', inyongera=inyongera, employees=employees)


@aicos_stock_managment.route('/ibyakoreshejwe')
@login_required
def ibyakoreshejwe():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    ibyakoreshejwe = Ibyakoreshejwe.query.filter_by(
        department_id=current_user.email).all()
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
    ibirarane = Ibirarane.query.filter_by(
        department_id=current_user.email).all()
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


@aicos_stock_managment.route('/injiza/umusaruro/<int:id>', methods=["GET", "POST"])
@login_required
def injizaUmusaruro(id):
    check_admin()
    memberid = Member.query.get_or_404(id)
    member_name = Member.query.filter_by(id=memberid.id).first()
    activity = Department.query.filter_by(email=current_user.email).first()
    coop_activity = Department.query.filter_by(email=current_user.email).first()
    act = coop_activity.Activity

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
                #RiceType=form.RiceType.data,
                RicePrice=form.RiceAmount.data,
                RiceAmount=int(form.RiceAmount.data) * form.Quantity.data,
                UmusaruroGrade=form.UmusaruroGrade.data,
                UwoAsigaranye=form.UwoAsigaranye.data,

                Musa=form.Musa.data,
                Carnet=form.Carnet.data,
                Avance=form.Avance.data,

                UwoKugurisha=(form.Quantity.data) - (form.UwoAsigaranye.data),
                GutonozaAmount=int(form.Gutonoza.data) *
                int(form.UwoAsigaranye.data),
                AmafarangaUmusaruro1=(int(form.RiceAmount.data) * (int(form.Quantity.data) -
                                                                   int(form.UwoAsigaranye.data)) - (int(form.Gutonoza.data) *
                                                                                                    int(form.UwoAsigaranye.data))) + 10 * form.RiceAmount.data * form.Quantity.data / 100,
                Asigaye=10 * form.Quantity.data / 100,
                done_date=form.done_date.data,
                member_id=memberid.id,
                department_id=current_user.email
            )




        elif form.UmusaruroGrade.data == 'normal':
            umusaruro = Umusarurob(
            #RiceType=form.RiceType.data,
            RicePrice=form.RiceAmount.data,
            RiceAmount=int(form.RiceAmount.data) * form.Quantity.data,
            UmusaruroGrade=form.UmusaruroGrade.data,
            UwoAsigaranye=form.UwoAsigaranye.data,

            Musa=form.Musa.data,
            Carnet=form.Carnet.data,
            Avance=form.Avance.data,

            UwoKugurisha=(form.Quantity.data) - (form.UwoAsigaranye.data),
            GutonozaAmount=int(form.Gutonoza.data) *
            int(form.UwoAsigaranye.data),
            AmafarangaUmusaruro1=(int(form.RiceAmount.data) * (int(form.Quantity.data) -
                                                                int(form.UwoAsigaranye.data)) - (int(form.Gutonoza.data) *
                                                                                            int(form.UwoAsigaranye.data))) + 10 * form.RiceAmount.data * form.Quantity.data / 100,
            
            Asigaye=10 * form.Quantity.data / 100,
            done_date=form.done_date.data,
            member_id=memberid.id,
            department_id=current_user.email
        )



        elif form.UmusaruroGrade.data == 'normal' and act == 'Potato':
            umusaruro = Umusarurob(
            #RiceType=form.RiceType.data,
            RicePrice=form.RiceAmount.data,
            RiceAmount=int(form.RiceAmount.data) * form.Quantity.data,
            UmusaruroGrade=form.UmusaruroGrade.data,
            UwoAsigaranye=form.UwoAsigaranye.data,

            Musa=form.Musa.data,
            Carnet=form.Carnet.data,
            Avance=form.Avance.data,

            UwoKugurisha=(form.Quantity.data) - (form.UwoAsigaranye.data),
            GutonozaAmount=int(form.Gutonoza.data) *
            int(form.UwoAsigaranye.data),

            AmafarangaUmusaruro1=((form.RiceAmount.data) * (form.Quantity.data)),            
            
            Asigaye= (5 * form.Quantity.data),
            done_date=form.done_date.data,
            member_id=memberid.id,
            department_id=current_user.email
        )


        else:
            uruganda_igiciro = 10 * 191 / 100

            Ibikase = uruganda_igiciro * (10 * form.Quantity.data / 100),
            umusaruro = Umusarurob(
                #RiceType=form.RiceType.data,
                RicePrice=form.RiceAmount.data,
                RiceAmount=int(form.RiceAmount.data) * form.Quantity.data,
                UmusaruroGrade=form.UmusaruroGrade.data,
                UwoAsigaranye=form.UwoAsigaranye.data,


                Musa=form.Musa.data,
                Carnet=form.Carnet.data,
                Avance=form.Avance.data,

                UwoKugurisha=(form.Quantity.data) - (form.UwoAsigaranye.data),
                GutonozaAmount=int(form.Gutonoza.data) *
                int(form.UwoAsigaranye.data),
                AmafarangaUmusaruro1=(int(form.RiceAmount.data) * (int(form.Quantity.data) -
                                                                   int(form.UwoAsigaranye.data)) - (int(form.Gutonoza.data) *
                                                                                                    int(form.UwoAsigaranye.data))) - 10 * form.RiceAmount.data * form.Quantity.data / 100,
                
                Asigaye=(10 * form.Quantity.data / 100),
                
                
                Ibisigaye = int(10 * form.Quantity.data / 100) * int(form.RiceAmount.data) - uruganda_igiciro * (10 * form.Quantity.data / 100),
                done_date=form.done_date.data,
                member_id=memberid.id,
                department_id=current_user.email
            )

    



        try:
            db.session.add(umusaruro)
            db.session.commit()
            url = "https://mistasms.com/sms/api"
            files = [
            ]
            headers = {
                'x-api-key': 'SE1tSUp2SUVFRkFtSHJMekdtc3M='
            }

            if form.UmusaruroGrade.data == 'good':
                payload = {
                    'to': member_name.nomero_telephone,
                    'from': 'Coopthevig',

                    'unicode': '0',
                    'sms': 'Muraho,' + str(member_name.izina_ribanza) + '. Umusaruro wose mwagemuye ni: ' + str(form.Quantity.data) + '-kg (havuyemo 10%), kugeza taliki 31-05-2020. igiciro/kg ni 174-Frw. Retenue z\'ukwezi zakuwemo ni: Carnet: ' +  str(form.Carnet.data) + ' Frw, Quality: ' +  str(form.Quality.data) + ' Frw, Inguzanyo: ' +  str(form.Inguzanyo.data) + ' Frw, Avance: ' +  str(form.Avance.data) +  ' Frw, Ejo heza: ' +  str(form.Ejoheza.data) + ' Frw, Ayo guhembwa ni: ' +  str(form.RiceAmount.data) + '-Frw (havuyemo 10%). Mukeneye ubufasha mwahamagara: 0786012383. Murakoze.',
                    'action': 'send-sms'
                }
                response = requests.request(
                    "POST", url, headers=headers, data=payload, files=files)

            else:
                payload = {
                    'to': '+250786012383',
                    'from': 'COOPTHEVIGI',
                    'unicode': '0',
                    'sms': 'Muraho,'+ str(member_name.izina_ribanza) + '. code:,' + str(member_name.sno) + '. umusaruro wose ' + str(form.Quantity.data) + '. ukase ' + str(form.Quantity.data - (10 * form.Quantity.data / 100)) + '. ayakaswe ' + str((form.Quantity.data - (10 * form.Quantity.data / 100)) * 19.1) + ' (Frw) ' + str(form.Quantity.data - (10 * form.Quantity.data / 100)) + ' (Kg).' + '. Ayo guhembwa ' + str((form.RiceAmount.data * (form.Quantity.data - (10 * form.Quantity.data / 100))) - ((form.Quantity.data - (10 * form.Quantity.data / 100)) * 19.1)) + ' Frw ' + str(get_time),
                    'action': 'send-sms'
                }
                response = requests.request(
                    "POST", url, headers=headers, data=payload, files=files)



        

            flash(Markup("Umaze kwandika umusaruro wa " + "<b>" +
                         member_name.izina_ribanza + " " + member_name.izina_rikurikira + "</b>"))

            return redirect(url_for('aicos_stock_managment.injizaUmusaruro'))
        except Exception:
            #flash("Ntago amakuru watanze yashoboye kwakirwa neza!")
            return redirect(url_for('aicos_stock_managment.injizaUmusaruro', activity=activity, form=form, memberid=memberid, member_name=member_name, id=memberid.id))

    return render_template('record_umusaruro.html', form=form, activity=activity, memberid=memberid, member_name=member_name)


@aicos_stock_managment.route('/injiza/inyongeramusaruro/<int:id>', methods=['GET', 'POST'])
@login_required
def injizaInyongeramusaruro(id):
    check_admin()
    memberid = Member.query.get_or_404(id)
    member_name = Member.query.filter_by(id=memberid.id).first()
    inyongera = InyongeraMusaruro.query.filter_by(
        department_id=current_user.email).all()

    if memberid is None:
        flash("Umunyamuryango usabye ntawuhari")
        return redirect(url_for('aicos_stock_managment.inyongeramusaruro'))
    if member_name.izina_ribanza is None:
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
            NPKkg=form.NPKkg.data,
            NPKPerUnity=form.NPKPerUnity.data,
            UREA=form.UREA.data,
            UREAPerUnity=form.UREAPerUnity.data,
            DAP=form.DAP.data,
            DAPPerUnity=form.DAPPerUnity.data,
            KCL=form.KCL.data,
            KCLPerUnity=form.KCLPerUnity.data,
            Briquette=form.Briquette.data,
            BriquettePerUnity=form.BriquettePerUnity.data,
            Cypemetrine=form.Cypemetrine.data,
            Beam=form.Beam.data,
            ImbutoQuantity=form.ImbutoQuantity.data,
            ImbutoAmount=form.ImbutoAmount.data,
            Redevance=form.Redevance.data,
            member_id=memberid.id,
            department_id=current_user.email
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
            InyongeraMusaruroType=form.InyongeraMusaruroType.data,
            Quantity=form.Quantity.data,
            Amount=form.Amount.data,
            Cypemetrine=form.Cypemetrine.data,
            Beam=form.Beam.data,
            ImbutoQuantity=form.ImbutoQuantity.data,
            ImbutoAmount=form.ImbutoAmount.data,
            Redevance=form.Redevance.data,
            member_id=memberid.id,
            department_id=current_user.email
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
    konte = CoopMemberBankAccounts.query.filter_by(
        department_id=current_user.email).all()
    return render_template("/bankiZacu.html", konte=konte)


@aicos_stock_managment.route('/injiza/konte', methods=['GET', 'POST'])
def injizaKonte():
    check_admin()
    form = KonteZaBankForm()

    if form.validate_on_submit():
        coopMemberBankAccounts = CoopMemberBankAccounts(
            memberName=form.izinaryaNyiriKonte.data,
            bankName=form.izanaRyaBank.data,
            bankAccountNumber=form.numeroYaKonte.data,
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
            UmusoroWakarere=form.UmusoroWakarere.data,
            UmusanzuCoop=form.UmusanzuCoop.data,
            Umugabane=form.Umugabane.data,
            Ikigega=form.Ikigega.data,
            KuzibaIcyuho=form.KuzibaIcyuho.data,
            member_id=memberid.id,
            department_id=current_user.email
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
            NPKkg=form.NPKkg.data,
            NPKPerUnity=form.NPKPerUnity.data,
            UREA=form.UREA.data,
            UREAPerUnity=form.UREAPerUnity.data,
            DAP=form.DAP.data,
            DAPPerUnity=form.DAPPerUnity.data,
            KCL=form.KCL.data,
            KCLPerUnity=form.KCLPerUnity.data,
            ImbutoQuantity=form.ImbutoQuantity.data,
            ImbutoAmount=form.ImbutoAmount.data,
            IdeniAmount=form.IdeniAmount.data,
            Briquette=form.Briquette.data,
            BriquettePerUnity=form.BriquettePerUnity.data,
            member_id=memberid.id,
            department_id=current_user.email
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
            AmandeC=form.AmandeC.data,
            AmandeApII=form.AmandeApII.data,
            comment=form.Comment.data,
            member_id=memberid.id,
            department_id=current_user.email
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

        if form.rpf.data is None:
            form.rpf.data = 0
        if form.ejo_heza.data is None:
            form.ejo_heza.data = 0
        if form.mituelle_amount.data is None:
            form.mituelle_amount.data = 0
        if form.carnet.data is None:
            form.carnet.data = 0
        if form.avance.data is None:
            form.avance.data = 0
        if form.loan.data is None:
            form.loan.data = 0


        ibindi = Ibindi(
            rpf=form.rpf.data,
            ejo_heza=form.ejo_heza.data,
            mituelle_amount=form.mituelle_amount.data,
            carnet=form.carnet.data,
            avance=form.avance.data,
            loan=form.loan.data,


            member_id=memberid.id,
            department_id=current_user.email
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




@aicos_stock_managment.route('/umusaruro/member/retenue<int:id>')
@login_required
def retenue_details(id):
    memberId = Member.query.get_or_404(id)
    umusaruro = Ibindi.query.filter_by(member_id=memberId.id).all()

    return render_template("/retenue_details.html", memberId=memberId, umusaruro=umusaruro)



@aicos_stock_managment.route('/imyishyurire', methods=['GET', 'POST'])
@login_required
def Imyishyurire():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    all_member_idd = Umusarurob.member_id
    umusaruro_resi = Umusarurob.query.all()
    member_all = Employee.query.filter_by(
        department_id=current_user.email).all()

    return render_template('imyishyurire.html', umusaruro_resi=umusaruro_resi, member_all=member_all, employees=employees)
