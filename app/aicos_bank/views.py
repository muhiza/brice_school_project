from flask import render_template
from flask_login import current_user, login_required

from . import aicos_bank
from ..models import *


@aicos_bank.route('/')
def index():
    return render_template("index_bank.html")









@aicos_bank.route('/bank_kwishyura')
@login_required
def bank_kwishyura():
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


    return render_template('bank_kwishyura.html', 
                                                ibirarane=ibirarane, 
                                                imisanzu=imisanzu, 
                                                umusaruro=umusaruro, 
                                                inyongeramusaruro=inyongeramusaruro,
                                                umusaruro_resi=umusaruro_resi, 
                                                member_all=member_all,
                                                inyongera=inyongera,
                                                memberss=memberss
                                                )

