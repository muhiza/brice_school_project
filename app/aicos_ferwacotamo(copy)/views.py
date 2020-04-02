from flask import abort,  request, flash, redirect, render_template, url_for, jsonify
from flask_login import current_user, login_required
from .forms import *
#from forms import DepartmentForm, EmployeeAssignForm, RoleForm, SendSMS, 
#ProjectForm, ClientForm, ProductForm, NewEmployee, SubscriptionPlan, ProductForm, OrderForm
from .. auth import *
from .. models import *
from .. import db, api
#from ..models import Department, Employee, Role, Project, Client, Subscription, Post, Category, Product, Decision
from ..models import * 
import nexmo
from flask import Flask, request, jsonify
import flask_excel as excel
from sqlalchemy import func
from . import aicos_ferwacotamo
# Api test related imports
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import make_response
import pdfkit
import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

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




@aicos_ferwacotamo.route('/')
def ferwacotamo_dashboard():
	return redirect(url_for('aicos_ferwacotamo.dashboard_overalls'))

# Views for serving the overall administrator blocks.
@aicos_ferwacotamo.route('/admin/coops/dashboard_overall')
@login_required
def cooperatives_overall():
    #check_admin()
    #check_overall()
    #check_coop_admin()
    employees = Member.query.all()
    departments = Department.query.all()
    all_depts = Department.query.count()
    all_mbs = Employee.query.count()
    all_depts_kigali = Department.query.filter_by(province='Kigali City').count()
    all_depts_west = Department.query.filter_by(province='West').count()
    all_depts_north = Department.query.filter_by(province='North').count()
    all_depts_south = Department.query.filter_by(province='South').count()
    all_depts_east = Department.query.filter_by(province='East').count()
    return render_template("admin/cooperatives.html", employees=employees, 
    						departments=departments, all_mbs=all_mbs, all_depts=all_depts, 
    						all_depts_kigali=all_depts_kigali,
    						all_depts_south = all_depts_south,
    						all_depts_north = all_depts_north,
    						all_depts_east = all_depts_east,
    						all_depts_west = all_depts_west,
    						title="Dashboard Overall")

@aicos_ferwacotamo.route('/admin/members_overall')
@login_required
def members_overall():
    #check_admin()
    #check_overall()
    #check_coop_admin()
    employees = Member.query.all()
    departments = Department.query.all()
    all_depts = Department.query.count()
    all_mbs = Employee.query.count()
    return render_template("members_overall.html", employees=employees, departments=departments, all_mbs=all_mbs, 
                            all_depts=all_depts, title="Dashboard Overall")

@aicos_ferwacotamo.route('/admin/waka/dashboard_overalls')
@login_required
def dashboard_overalls():
    #check_admin()
    #check_overall()
    #check_coop_admin()
    employees = Member.query.all()
    departments = Department.query.all()
    all_depts = Department.query.count()
    all_mbs = Member.query.count()
    notifications = Notification.query.all()
    return render_template("admin/dash_new.html", employees=employees, 
    						notifications=notifications, departments=departments, 
    						all_mbs=all_mbs, all_depts=all_depts,
    						title="Dashboard Overall")

@aicos_ferwacotamo.route('/admin/dashboard_cooperative')
@login_required
def dashboard_coop():
    #check_admin()
    #check_coop_admin()
    employees = Member.query.all()
    departments = Department.query.all()
    all_depts = Department.query.count()
    all_mbs = Member.query.count()
    notes = Department.query.filter_by(email=current_user.email).first()
    notifications = Notification.query.filter_by(department_id='abahuza@gmail.com')
    return render_template("dashboard_coop.html", notifications=notifications, 
                            employees=employees, departments=departments, all_mbs=all_mbs, 
                            all_depts=all_depts, title="Dashboard Coop Admin")


# Views for the full details of a specific employee
@aicos_ferwacotamo.route('/cooperative_details/<string:email>', methods=['GET', 'POST'])
@login_required
def coop_details(email):
    #check_admin()
    #check_overall()
    #check_coop_admin()
    departments = Department.query.get_or_404(email)
    employees = departments.members
    employees_count = departments.members.count()
    employees_male = departments.members.filter_by(Igitsina='Gabo')
    employees_male_count = departments.members.filter_by(Igitsina='Gabo').count()
    employees_female = departments.members.filter_by(Igitsina='Gole')
    employees_female_count = departments.members.filter_by(Igitsina='Gole').count()
    employees_abatarize = departments.members.filter_by(Amashuri='Abatarize')
    employees_abatarize_count = departments.members.filter_by(Amashuri='Abatarize').count()
    employees_abanza = departments.members.filter_by(Amashuri='Abanza')
    employees_abanza_count = departments.members.filter_by(Amashuri='Abanza').count()
    employees_ayisumbuye = departments.members.filter_by(Amashuri='Ayisumbuye')
    employees_ayisumbuye_count = departments.members.filter_by(Amashuri='Ayisumbuye').count()
    employees_kaminuza = departments.members.filter_by(Amashuri='Kaminuza')
    employees_kaminuza_count = departments.members.filter_by(Amashuri='Kaminuza').count()
    employees_imyuga = departments.members.filter_by(Amashuri='Imyuga')
    employees_imyuga_count = departments.members.filter_by(Amashuri='Imyuga').count()
    employees_amaguru = departments.members.filter_by(Ubumuga='Amaguru')
    employees_amaguru_count = departments.members.filter_by(Ubumuga='Amaguru').count()
    employees_amaboko = departments.members.filter_by(Ubumuga='Amaboko')
    employees_amaboko_count = departments.members.filter_by(Ubumuga='Amaboko').count()
    employees_kutabona = departments.members.filter_by(Ubumuga='Kutabona')
    employees_kutabona_count = departments.members.filter_by(Ubumuga='Kutabona').count()
    employees_kutumva = departments.members.filter_by(Ubumuga='Kutumva')
    employees_kutumva_count = departments.members.filter_by(Ubumuga='Kutumva').count()
    employees_mumutwe = departments.members.filter_by(Ubumuga='Mu mutwe')
    employees_mumutwe_count = departments.members.filter_by(Ubumuga='Mu mutwe').count()
    male_members = departments.members.filter_by(Igitsina='Gole').first()
    if departments is not None:
        return render_template("admin/cooperative_details.html", departments=departments, 
        						employees=employees,
	                           employees_count=employees_count,
	                           male_members=male_members,
	                           employees_male=employees_male,
	                           employees_female=employees_female,
	                           employees_male_count=employees_male_count,
	                           employees_female_count=employees_female_count,
	                           employees_abatarize=employees_abatarize,
	                           employees_abatarize_count=employees_abatarize_count,
	                           employees_abanza=employees_abanza,
	                           employees_abanza_count=employees_abanza_count,
	                           employees_ayisumbuye=employees_ayisumbuye,
	                           employees_ayisumbuye_count=employees_ayisumbuye_count,
	                           employees_kaminuza=employees_kaminuza,
	                           employees_kaminuza_count=employees_kaminuza_count,
	                           employees_imyuga=employees_imyuga,
	                           employees_imyuga_count=employees_imyuga_count,
	                           employees_amaguru=employees_amaguru,
	                           employees_amaguru_count=employees_amaguru_count,
	                           employees_amaboko=employees_amaboko,
	                           employees_amaboko_count=employees_amaboko_count,
	                           employees_kutabona=employees_kutabona,
	                           employees_kutabona_count=employees_kutabona_count,
	                           employees_kutumva=employees_kutumva,
	                           employees_kutumva_count=employees_kutumva_count,
	                           employees_mumutwe=employees_mumutwe,
	                           employees_mumutwe_count=employees_mumutwe_count,
        						title="Cooperative's details")
    return redirect(url_for('admin.list_employees'))

@aicos_ferwacotamo.route('/memberDetails/<int:id>', methods=['GET', 'POST'])
@login_required
def memberDetails(id):
    #check_admin()
    employee = Member.query.get_or_404(id)
    if employee is not None:
        return render_template("overall_member_details.html", employee=employee)
    return redirect(url_for('aicos_members.aicos_members_home'))



@aicos_ferwacotamo.route('/members/umusaruro/')
@login_required
def federation_umusaruro():
    employee = Department.query.all()
    return render_template("federation_umusaruro.html", employee=employee)

@aicos_ferwacotamo.route('/cooperative/umusaruro/<string:email>')
@login_required
def coop_umusaruro(email):
    departments = Department.query.get_or_404(email)
    employees = departments.members
    umusarurob = Umusarurob.query.filter_by(department_id=email).all()
    return render_template('cooperative_umusaruro.html', departments=departments, umusarurob=umusarurob)


@aicos_ferwacotamo.route('/members/inyongeramusaruro/')
@login_required
def federation_inyongeramusaruro():
    employee = Department.query.all()
    return render_template('federation_inyongeramusaruro.html', employee=employee)

@aicos_ferwacotamo.route('/cooperative/inyongeramusaruro/<string:email>')
@login_required
def coop_inyongeramusaruro(email):
    departments = Department.query.get_or_404(email)
    employees = departments.members
    inyongeramusaruro = InyongeraMusaruro.query.filter_by(department_id=email).all()
    return render_template('cooperative_inyongeramusaruro.html', departments=departments, inyongeramusaruro=inyongeramusaruro)

@aicos_ferwacotamo.route('/members/imisanzu/')
@login_required
def federation_imisanzu():
    employee = Department.query.all()
    return render_template('federation_imisanzu.html', employee=employee)

@aicos_ferwacotamo.route('/cooperative/imisanzu/<string:email>')
@login_required
def coop_imisanzu(email):
    departments = Department.query.get_or_404(email)
    employees = departments.members
    imisanzu = Umusanzu.query.filter_by(department_id=email).all()
    return render_template('coop_imisanzu.html', departments=departments, imisanzu=imisanzu)

@aicos_ferwacotamo.route('/members/ibirarane/')
@login_required
def federation_ibirarane():
    employee = Department.query.all()
    return render_template('federation_ibirarane.html', employee=employee)

@aicos_ferwacotamo.route('/cooperative/ibirarane/<string:email>')
@login_required
def coop_ibirarane(email):
    departments = Department.query.get_or_404(email)
    employees = departments.members
    ibirarane = Ibirarane.query.filter_by(department_id=email).all()
    return render_template('coop_ibirarane.html', departments=departments, ibirarane=ibirarane)

@aicos_ferwacotamo.route('/members/ibihano/')
@login_required
def federation_ibihano():
    employee = Department.query.all()
    return render_template('federation_ibihano.html', employee=employee)

@aicos_ferwacotamo.route('/cooperative/ibihano/<string:email>')
@login_required
def coop_ibihano(email):
    departments = Department.query.get_or_404(email)
    employees = departments.members
    ibihano = Ibihano.query.filter_by(department_id=email).all()
    return render_template('coop_ibihano.html', departments=departments, ibihano=ibihano)


@aicos_ferwacotamo.route('/members/ibindi/')
@login_required
def federation_ibindi():
    employee = Department.query.all()
    return render_template('federation_ibindi.html', employee=employee)

@aicos_ferwacotamo.route('/cooperative/ibindi/<string:email>')
@login_required
def coop_ibindi(email):
    departments = Department.query.get_or_404(email)
    employees = departments.members
    ibindi = Ibindi.query.filter_by(department_id=email).all()
    return render_template('coop_ibindi.html', departments=departments, ibindi=ibindi)





