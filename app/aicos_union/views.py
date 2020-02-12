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
from . import aicos_union
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

def check_union_admin():
    if not current_user.is_union_admin:
        abort(403)




@aicos_union.route('/')
def ferwacotamo_dashboard():
	return redirect(url_for('aicos_union.dashboard_overalls'))

# Views for serving the overall administrator blocks.
@aicos_union.route('/admin/unions/dashboard_overall')
@login_required
def Unions_overall():
    #check_admin()
    #check_overall()
    #check_union_admin()
    employees = Member.query.all()
    departments = Department.query.all()
    all_depts = Department.query.count()
    all_mbs = Employee.query.count()
    all_depts_kigali = Department.query.filter_by(province='Kigali City').count()
    all_depts_west = Department.query.filter_by(province='West').count()
    all_depts_north = Department.query.filter_by(province='North').count()
    all_depts_south = Department.query.filter_by(province='South').count()
    all_depts_east = Department.query.filter_by(province='East').count()
    return render_template("union/Unions.html", employees=employees, 
    						departments=departments, all_mbs=all_mbs, all_depts=all_depts, 
    						all_depts_kigali=all_depts_kigali,
    						all_depts_south = all_depts_south,
    						all_depts_north = all_depts_north,
    						all_depts_east = all_depts_east,
    						all_depts_west = all_depts_west,
    						title="Dashboard Overall")

@aicos_union.route('/admin/members_overall')
@login_required
def members_overall():
    #check_admin()
    #check_overall()
    #check_union_admin()
    employees = Member.query.all()
    departments = Department.query.all()
    all_depts = Department.query.count()
    all_mbs = Employee.query.count()
    return render_template("members_overall.html", employees=employees, departments=departments, all_mbs=all_mbs, 
                            all_depts=all_depts, title="Dashboard Overall")

@aicos_union.route('/admin/waka/dashboard_overalls')
@login_required
def dashboard_overalls():
    #check_admin()
    #check_overall()
    #check_union_admin()
    employees = Member.query.all()
    departments = Department.query.all()
    all_depts = Department.query.count()
    all_mbs = Member.query.count()
    notifications = Notification.query.all()
    return render_template("union/dash_new.html", employees=employees, 
    						notifications=notifications, departments=departments, 
    						all_mbs=all_mbs, all_depts=all_depts,
    						title="Dashboard Overall")

@aicos_union.route('/admin/dashboard_Union')
@login_required
def dashboard_union():
    #check_admin()
    #check_union_admin()
    employees = Member.query.all()
    departments = Department.query.all()
    all_depts = Department.query.count()
    all_mbs = Member.query.count()
    notes = Department.query.filter_by(email=current_user.email).first()
    notifications = Notification.query.filter_by(department_id='abahuza@gmail.com')
    return render_template("dashboard_union.html", notifications=notifications, 
                            employees=employees, departments=departments, all_mbs=all_mbs, 
                            all_depts=all_depts, title="Dashboard union Admin")


# Views for the full details of a specific employee
@aicos_union.route('/Union_details/<string:email>', methods=['GET', 'POST'])
@login_required
def union_details(email):
    #check_admin()
    #check_overall()
    #check_union_admin()
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
        return render_template("admin/Union_details.html", departments=departments, 
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
        						title="Union's details")
    return redirect(url_for('admin.list_employees'))

@aicos_union.route('/memberDetails/<int:id>', methods=['GET', 'POST'])
@login_required
def memberDetails(id):
    #check_admin()
    employee = Member.query.get_or_404(id)
    if employee is not None:
        return render_template("overall_member_details.html", employee=employee)
    return redirect(url_for('aicos_members.aicos_members_home'))



@aicos_union.route('/members/umusaruro/')
@login_required
def federation_umusaruro():
    employee = Department.query.all()
    return render_template("federation_umusaruro.html", employee=employee)

@aicos_union.route('/Union/umusaruro/<string:email>')
@login_required
def union_umusaruro(email):
    departments = Department.query.get_or_404(email)
    employees = departments.members
    umusarurob = Umusarurob.query.filter_by(department_id=email).all()
    return render_template('Union_umusaruro.html', departments=departments, umusarurob=umusarurob)


@aicos_union.route('/members/inyongeramusaruro/')
@login_required
def federation_inyongeramusaruro():
    employee = Department.query.all()
    return render_template('federation_inyongeramusaruro.html', employee=employee)

@aicos_union.route('/Union/inyongeramusaruro/<string:email>')
@login_required
def union_inyongeramusaruro(email):
    departments = Department.query.get_or_404(email)
    employees = departments.members
    inyongeramusaruro = InyongeraMusaruro.query.filter_by(department_id=email).all()
    return render_template('Union_inyongeramusaruro.html', departments=departments, inyongeramusaruro=inyongeramusaruro)

@aicos_union.route('/members/imisanzu/')
@login_required
def federation_imisanzu():
    employee = Department.query.all()
    return render_template('federation_imisanzu.html', employee=employee)

@aicos_union.route('/Union/imisanzu/<string:email>')
@login_required
def union_imisanzu(email):
    departments = Department.query.get_or_404(email)
    employees = departments.members
    imisanzu = Umusanzu.query.filter_by(department_id=email).all()
    return render_template('union_imisanzu.html', departments=departments, imisanzu=imisanzu)

@aicos_union.route('/members/ibirarane/')
@login_required
def federation_ibirarane():
    employee = Department.query.all()
    return render_template('federation_ibirarane.html', employee=employee)

@aicos_union.route('/Union/ibirarane/<string:email>')
@login_required
def union_ibirarane(email):
    departments = Department.query.get_or_404(email)
    employees = departments.members
    ibirarane = Ibirarane.query.filter_by(department_id=email).all()
    return render_template('union_ibirarane.html', departments=departments, ibirarane=ibirarane)

@aicos_union.route('/members/ibihano/')
@login_required
def federation_ibihano():
    employee = Department.query.all()
    return render_template('federation_ibihano.html', employee=employee)

@aicos_union.route('/Union/ibihano/<string:email>')
@login_required
def union_ibihano(email):
    departments = Department.query.get_or_404(email)
    employees = departments.members
    ibihano = Ibihano.query.filter_by(department_id=email).all()
    return render_template('union_ibihano.html', departments=departments, ibihano=ibihano)


@aicos_union.route('/members/ibindi/')
@login_required
def federation_ibindi():
    employee = Department.query.all()
    return render_template('federation_ibindi.html', employee=employee)

@aicos_union.route('/Union/ibindi/<string:email>')
@login_required
def union_ibindi(email):
    departments = Department.query.get_or_404(email)
    employees = departments.members
    ibindi = Ibindi.query.filter_by(department_id=email).all()
    return render_template('union_ibindi.html', departments=departments, ibindi=ibindi)




@aicos_union.route('/unionInfo/edit/<string:email>', methods=['GET', 'POST'])
@login_required
def unionInfo(email):
    """
    Edit a role
    """
    check_admin()
    #add_role = False
    union = Union.query.get_or_404(email)
    form = UnionForm(obj=union)
    if form.validate_on_submit():
        union.code = form.Code.data
        union.name = form.Name.data
        union.regdate = form.RegDate.data
        union.Certificate = form.Certificate.data
        union.Province   = form.Province.data
        union.District   = form.District.data
        union.Sector     = form.Sector.data
        union.Cell       = form.Cell.data
        union.startingShare = form.startingShare.data
        union.Field         = form.Field.data
        union.Description   = form.Description.data
        union.email         = current_user.email
        union.is_active         = 1
        code               = form.Code.data
        current_user.is_union = True
        current_user.department_id = current_user.email
        if form.Code.data == union.code:        
            db.session.add(union)
            db.session.commit()
            #flash('Umaze kwinjiza Union yawe neza.')
            flash(Markup('Umaze kwinjiza Union yawe neza., <b>Ongera winjire muri konti yawe!.</b>'), 'success')
            return redirect(url_for('aicos_union.done'))
        else:
            #flash('Code urimo kwinjiza ntago ihuye na Union, Reba muri telephone yawe!.')
            #flash(Markup('Flashed message with <b>bold</b> statements'), 'success')
            flash(Markup('Code urimo kwinjiza ntago ihuye na Union, <b>Wemerewe kwinjiza Code inshuro imwe!.</b>'), 'danger')
            to_number = '250780400612'
            message = 'Code ya Union ' + union.name + ' ku rubuga AICOS ni ' + union.code
            response = client.send_message({'from' : '+250782061714', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]

        # redirect to the roles page
        return redirect(url_for('aicos_union.unionInfo', email=email))


    form.Code.data = union.code
    form.Name.data = union.name
    form.RegDate.data = union.regdate
    form.Certificate.data = union.certificate
    form.Province.data = union.province
    form.District.data = union.district
    form.Sector.data = union.sector
    form.Cell.data = union.cell
    form.startingShare.data = union.starting_share
    #form.Field.data = union.Field
    form.Description.data = union.description
    return render_template('reg/union_info.html',
                           form=form, title="Edit Role")


@aicos_union.route('/UnionInfo/newApplication', methods=['GET', 'POST'])
@login_required
def newApplication():
    """
    Edit a role
    """
    check_admin()
    #add_role = False
    form = newUnionForm()
    if form.validate_on_submit():
        #union.Code = form.Code.data
        newunion = Union(
                        name = form.Name.data,
                        province   = form.Province.data,
                        district   = form.District.data,
                        sector     = form.Sector.data,
                        cell       = form.Cell.data,
                        starting_share = form.startingSharex.data,
                        share_per_person = form.sharePerPerson.data,
                        male_members         = form.maleMembers.data,
                        female_members         = form.femaleMembers.data,
                        is_active         = 1,
                        activity          = form.Activity.data,
                        federation = Federation.query.filter_by(code=form.Federation.data).first(),
                        #current_user.is_union_admin     = 1,
                        email         = current_user.email
                        #current_user.is_admin = 1
                    )
        # return '<p>Code:{},Name:{}</p>'.format(form.Province.data)

        try:      
            db.session.add(newunion)
            current_user.is_union = 1
            db.session.commit()
            #flash('Umaze kwinjiza Union yawe neza.')
            flash(Markup('Umaze kwinjiza Union yawe neza., <b>Ongera winjire muri konti yawe!.</b>'), 'success')
            return redirect(url_for('aicos_union.done'))
        except:
            #flash('Code urimo kwinjiza ntago ihuye na Union, Reba muri telephone yawe!.')
            #flash(Markup('Flashed message with <b>bold</b> statements'), 'success')
            flash(Markup('Umwirondoro wa Koperative urimo gushyiramo ntago wuzuye, <b>Ongera ugerageze!.</b>'), 'danger')
            to_number = '250780400612'
            message = 'Code ya Union ku rubuga AICOS ni '
            response = client.send_message({'from' : '+250782061714', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]

        # redirect to the roles page
        return redirect(url_for('aicos_union.done'))

    return render_template('reg/new_union.html',form=form)

@aicos_union.route('/district/<province>')
def change_dist(province):
    for i in Provinces:
        if i==province:
            return jsonify({'districts':Provinces[i]})

@aicos_union.route('/federation/<activity>')
def change_fed(activity):
    federations = Federation.query.filter_by(activity=activity).all()
    fed_array = []
    for fed in federations:
        fedObj = {}
        fedObj['code'] = fed.code
        fedObj['name'] = fed.name
        fed_array.append(fedObj)
    return jsonify({'federations':fed_array})