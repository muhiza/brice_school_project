from flask import render_template, abort, flash, redirect, url_for, request
from . import aicos_crm
from flask_login import current_user, login_required
from ..models import * 
from .forms import *
# import flask_excel
# import flask_excel as excel
# from sqlalchemy import func

import nexmo

import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
client = nexmo.Client(key='e7096025', secret='ab848459dae27b51')

@aicos_crm.route('/items_table', methods=['GET', 'POST'])
def table():
    # assignments = CRM.query.filter_by(id=current_user.id).all()
    return render_template("table.html")

@aicos_crm.route('/add_new_item', methods=['GET', 'POST'])
def add_item():
    add_item = True
    form = ItemForm()
    if form.validate_on_submit():
        newCRM = CRM (
                        tag = form.tag.data,
                        company_name = form.company_name.data,
                        email = form.email.data,
                        website = form.website.data,
                        address = form.address.data,
                        contact_type = form.contact_type.data,
                        phone_number = form.phone_number.data,
                        city = form.city.data,
                        country = form.country.data,
                        # employee_id = form.employee_id.data,
                        description = form.description.data,
                        status = form.status.data
                        )

        # newCRM.cooperative_id = current_user.id
        employee = Employee.query.filter_by(username=form.employee_id.data.username).first()
        newCRM.employee_id = employee.id
        try:
            
            db.session.add(newCRM)
            db.session.commit()

            console.log(newCRM.employee_id)
            
            to_number = newCRM.phone_number
            message = current_user.email + 'New assignment has been given to '+newCRM.assignee+'of the cooperative '+newCRM.cooperative.name+'to work with you.'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]

            flash("Umaze kwandika ikindi gikorwa neza!")
            return redirect(url_for('aicos_crm.table'))
        except Exception:
            # db.session.close()
            flash("Ntago amakuru watanze yashoboye kwakirwa neza!")
    return render_template("new_item.html",form=form)

@aicos_crm.route('/add_new_item', methods=['GET', 'POST'])
def remove_item(id):
    crm = CRM.query.get_or_404(id)
    db.session.delete(crm)
    db.session.commit()
    
    to_number = newCRM.phone_number
    message = current_user.email + 'The assignment which has been given to '+newCRM.assignee+'of the cooperative '+newCRM.cooperative.name+'to work with you, has been deleted.'
    response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
    response_text = response['messages'][0]

    flash('You have successfully deleted the assignment.')
    # redirect to the departments page
    return redirect(url_for('aicos_crm.table'))
    return render_template(title="Delete Assignment")

@aicos_crm.route('/add_new_item', methods=['GET', 'POST'])
def edit_item(id):
    add_item = False
    crm = CRM.query.get_or_404(id)
    form = ItemForm(obj=crm)
    if form.validate_on_submit():

        crm.cooperative_id = current_user.id
        crm.tag            = form.tag.data
        crm.company_name   = form.company_name.data
        crm.email          = form.email.data
        crm.website        = form.website.data
        crm.address        = form.address.data
        crm.contact_type   = form.contact_type.data
        crm.phone_number   = form.phone_number.data
        crm.city           = form.city.data
        crm.country        = form.country.data
        crm.assignee       = form.assignee.data
        crm.description    = form.description.data
        crm.status         = form.status.data

        db.session.commit()
        flash('You have successfully edited the assignment.')
        return redirect(url_for('aicos_crm.table'))

    form.tag.data          = crm.tag
    form.company_name.data = crm.company_name
    form.email.data        = crm.email
    form.website.data      = crm.website
    form.address.data      = crm.address
    form.contact_type.data = crm.contact_type
    form.phone_number.data = crm.phone_number
    form.city.data         = crm.city
    form.country.data      = crm.country
    form.assignee.data     = crm.assignee
    form.description.data  = crm.description
    form.status.data       = crm.status

    return render_template('new_item.html', action="Edit",
                           add_item=add_item, form=form,
                           crm=crm, title="Edit Assignment")

@aicos_crm.route('/add_new_item', methods=['GET', 'POST'])
def assign():
    form = ItemForm()
    # if form.validate_on_submit():
    #     newGoal = Goal (
    #                     name = form.name.data,
    #                     Description = form.description.data,
    #                     Amount = form.amount.data,
    #                     startingDate = form.startingDate.data,
    #                     endingDate = form.endingDate.data
    #                     )
    #     try:
    #          db.session.add(newGoal)
    #          db.session.commit()
    #          flash("Umuaze kwandika ikindi gikorwa neza!")
    #          return redirect(url_for('aicos_members.memberPayments'))
    #     except Exception:
    #         flash("Ntago amakuru watanze yashoboye kwakirwa neza!")
    return render_template("new_item.html",form=form)

@aicos_crm.route('/add_new_item', methods=['GET', 'POST'])
def send_sms():
    form = ItemForm()
    # if form.validate_on_submit():
    #     newGoal = Goal (
    #                     name = form.name.data,
    #                     Description = form.description.data,
    #                     Amount = form.amount.data,
    #                     startingDate = form.startingDate.data,
    #                     endingDate = form.endingDate.data
    #                     )
    #     try:
    #          db.session.add(newGoal)
    #          db.session.commit()
    #          flash("Umuaze kwandika ikindi gikorwa neza!")
    #          return redirect(url_for('aicos_members.memberPayments'))
    #     except Exception:
    #         flash("Ntago amakuru watanze yashoboye kwakirwa neza!")
    return render_template("new_item.html",form=form)