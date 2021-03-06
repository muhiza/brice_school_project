"""
This is the views file that is processing the new users registrations
and processing the registered users who are logging in
"""

# Third-party imports
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user

# Internal imports.
from . import auth
from .forms import LoginForm, RegistrationForm, ForgetPasswordForm, MemberLoginForm
from .. import db
from ..models import Employee, Notification, Member

# Third-party imports
from markupsafe import Markup
import socket
import nexmo

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

# Introducing nexmo instance which is used to send messages.
client = nexmo.Client(key='e88f8d53', secret='w7j2m7zksG7RPPVc')

#The route for registration page and processing.
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(email=form.email.data,
                            username=form.username.data,
                            #first_name=form.first_name.data,
                            #last_name=form.last_name.data,
                            phone_number = form.phone_number.data,
                            password=form.password.data)
        #member   = Member(firstName=form.first_name.data,
                         # secondName=form.last_name.data)
        notif = Notification(action="Created account",
                            done_by=form.username.data,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded")
        try:
            # add employee to the database
            db.session.add(employee)
            db.session.add(notif)
            #db.session.add(member)
            db.session.commit()

            """
            to_number = '+250786012383'
            message = 'Umaze kwinjizwa muri sisiteme AICOS. Uzajya ubona amakuru ajyanye na Cooperative buri gihe.'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            """
            flash('Umaze gufungura konti yawe neza, ubu ushobo kuyinjiramo!.')
            # redirect to the login page
            return redirect(url_for('auth.login'))
        except Exception:
            flash("Kwiyandikisha ntabwo byakunze neza")
            redirect(url_for('auth.register'))
    #load registration template
    return render_template('auth/cooperative_admin_register.html', form=form, title='Register')





#The route for registration page and processing / Kinyarwanda.
@auth.route('/rw/register', methods=['GET', 'POST'])
def rw_register():
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(email=form.email.data,
                            username=form.username.data,
                            #first_name=form.first_name.data,
                            #last_name=form.last_name.data,
                            phone_number = form.phone_number.data,
                            password=form.password.data)
        #member   = Member(firstName=form.first_name.data,
                         # secondName=form.last_name.data)
        notif = Notification(action="Created account",
                            done_by=form.username.data,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded")
        try:
            # add employee to the database
            db.session.add(employee)
            db.session.add(notif)
            #db.session.add(member)
            db.session.commit()

            """
            to_number = '+250786012383'
            message = 'Umaze kwinjizwa muri sisiteme AICOS. Uzajya ubona amakuru ajyanye na Cooperative buri gihe.'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            """
            flash('Umaze gufungura konti yawe neza, ubu ushobo kuyinjiramo!.')
            # redirect to the login page
            return redirect(url_for('auth.login'))
        except Exception:
            flash("Kwiyandikisha ntabwo byakunze neza")
            redirect(url_for('auth.register'))
    #load registration template
    return render_template('auth/rw_cooperative_admin_register.html', form=form, title='Register')




#The route for login page and processing the request.
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(
                form.password.data):
            #log employee in
            notif = Notification(action="Loged In",
                            done_by=form.email.data,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded")
            db.session.add(notif)
            db.session.commit()
            login_user(employee)
            # redirect to the appropriate dashboard page
            if employee.is_overall: 
                return redirect(url_for('aicos_ferwacotamo.dashboard_overalls'))
            elif employee.is_admin and employee.is_coop_admin:
                return redirect(url_for('aicos_members.dashboard'))
            elif employee.is_admin and employee.is_accountant:
                return redirect(url_for('aicos_req.accountingBooks'))
            elif employee.is_admin and employee.is_production_manager:
                return redirect(url_for('aicos_req.Production'))
            elif employee.is_union:
            	return redirect(url_for('aicos_union.ferwacotamo_dashboard'))
            elif employee.is_ferwacotamo:
                return redirect(url_for('aicos_ferwacotamo.ferwacotamo_dashboard'))
            elif employee.is_confederation:
                return redirect(url_for('aicos_confederation.confederation_dashboard'))
            elif employee.is_rca:
                return redirect(url_for('aicos_rca.rca_dashboard'))
            elif employee.is_super_user:
                return redirect(url_for('aicos_super_user.dashboard_overalls'))

            elif employee.is_admin:
                return redirect(url_for('home.dashboard'))
            else:
                return redirect(url_for('aicos_members.aicos_members_home'))
        # when login details are incorrect
        else:
            flash('Invalid email or password.')
    # load login template
    return render_template('auth/cooperative_admin_login.html', form=form, title='Login')






#The route for login page and processing the request / In Kinyarwanda.
@auth.route('/rw/login', methods=['GET', 'POST'])
def rw_login():
    form = LoginForm()
    if form.validate_on_submit():
        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(
                form.password.data):
            #log employee in
            notif = Notification(action="Loged In",
                            done_by=form.email.data,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded")
            db.session.add(notif)
            db.session.commit()
            login_user(employee)
            # redirect to the appropriate dashboard page
            if employee.is_overall: 
                return redirect(url_for('aicos_ferwacotamo.dashboard_overalls'))
            elif employee.is_admin and employee.is_coop_admin:
                return redirect(url_for('aicos_members.dashboard'))
            elif employee.is_admin and employee.is_accountant:
                return redirect(url_for('aicos_req.accountingBooks'))
            elif employee.is_admin and employee.is_production_manager:
                return redirect(url_for('aicos_req.Production'))
            elif employee.is_union:
            	return redirect(url_for('aicos_union.ferwacotamo_dashboard'))
            elif employee.is_ferwacotamo:
                return redirect(url_for('aicos_ferwacotamo.ferwacotamo_dashboard'))
            elif employee.is_confederation:
                return redirect(url_for('aicos_confederation.confederation_dashboard'))
            elif employee.is_rca:
                return redirect(url_for('aicos_rca.rca_dashboard'))
            elif employee.is_admin:
                return redirect(url_for('home.dashboard'))
            else:
                return redirect(url_for('aicos_members.aicos_members_home'))
        # when login details are incorrect
        else:
            flash('Invalid email or password.')
            return redirect(url_for('auth.rw_login'))
    # load login template
    return render_template('auth/rw_cooperative_admin_login.html', form=form, title='Login')







#The route for login page and processing the request.
@auth.route('/memberLogin', methods=['GET', 'POST'])
def member_login():
    form = MemberLoginForm()
    if form.validate_on_submit():
        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        member = Member.query.filter_by(id=form.member_id.data).first()
        if member is not None:
            #log employee in
            notif = Notification(action="Loged In",
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded")
            db.session.add(notif)
            db.session.commit()
            login_user(member)
            return redirect(url_for('auth.member_profile'))
        else:
            flash('Invalid email or password.')
    # load login template
    return render_template('auth/member_login.html', form=form, title='Login')



"""
@auth.route('/coopadmin')
def coopadmin():
"""

#The route for logout page and processing.
@auth.route('/logout')
@login_required
def logout():
        notif = Notification(action="Logged out",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded")
        db.session.add(notif)
        db.session.commit()
        logout_user()
        #flash('Umaze gusohoka muri konti yawe neza!.')
        flash(Markup('Umaze gusohoka muri konti yawe neza!.'), 'success')
        # redirect to the login page
        return redirect(url_for('auth.rw_login'))




# The route for forgot password page and processing.
@auth.route('/ForgotPassword', methods=['POST', 'GET'])
def ForgotPassword():
    form = ForgetPasswordForm()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None:
            # log employee want to change password
            notif = Notification(action="change password",
                            done_by=form.email.data,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded")
            """
            Send message for renew employee password
            """
            db.session.add(notif)
            db.session.commit()
            """
            update employee password
            and show go to confirm page for checking if he is real employee
            """
    return render_template('auth/forget_password.html', form=form)






















