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
# hostname = socket.gethostname()
# IP = socket.gethostbyname(hostname)
# client = nexmo.Client(key='e7096025', secret='ab848459dae27b51')

from flask import Flask, jsonify
from twilio.rest import Client
import os


def send_sms(to_number,body):
    account_sid = 'AC748e888b9c42a401f6f9a04021e16be2'
    auth_token  = '489a7fe543032bdb42e4975d480a8784'
    number = '+12055764624'
    client = Client(account_sid, auth_token)  
    message = client.messages \
            .create(
                    body=body,
                    from_=number,
                    to=to_number
                )

    return message

@aicos_crm.route('/items_table', methods=['GET', 'POST'])
@login_required
def table():
    assignments = CRM.query.filter_by(department=current_user.department).all()
    
    # for assignment in assignments:
    #     department = assignment.department.name
    #     return render_template("table.html", assignments=assignments, department=department)
    return render_template("table.html", assignments=assignments)

@aicos_crm.route('/add_new_item', methods=['GET', 'POST'])
@login_required
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
                        description = form.description.data,
                        status = form.status.data
                        )

        newCRM.department = current_user.department
        employee = Employee.query.filter_by(username=str(form.employee_id.data)).first()
        newCRM.employee = employee
        
        newCRM.add_new_item()
        flash("Umaze kwandika ikindi gikorwa neza!")

        try: 
            send_sms(to_number=newCRM.phone_number,body='New assignment.')

            flash("Ubutumwa bwagiye neza!")
        except Exception:
            flash("Ntabwo ubutumwa bwabashije kugenda neza!")

        return redirect(url_for('aicos_crm.table', employee=employee))
    return render_template("new_item.html",form=form)

@aicos_crm.route('/items_table/delete/<id>', methods=['GET', 'POST'])
@login_required
def remove_item(id):
    # print(id)
    asgmt = CRM.query.filter_by(id=id).first()
    
    asgmt.delete_item()
    flash('You have successfully deleted the assignment.')

    try: 
        send_sms(to_number=asgmt.phone_number,body='Deleted assignment.')

        flash("Ubutumwa bwagiye neza!")
    except Exception:
        flash("Ntabwo ubutumwa bwabashije kugenda neza!")

    return redirect(url_for('aicos_crm.table'))

@aicos_crm.route('/items_table/edit/<id>/<employee_id>', methods=['GET', 'POST'])
@login_required
def edit_item(id, employee_id):
    add_item = False
    crm = CRM.query.filter_by(id=id).first()
    # crm.department = current_user
    employee = Employee.query.filter_by(id=employee_id).first()
    username = employee.username
    # print(crm.employee_id)
    # crm.employee_id = employee.id
    form = ItemForm(obj=crm)
    if form.validate_on_submit():

        crm.department     = current_user.department
        crm.tag            = form.tag.data
        crm.company_name   = form.company_name.data
        crm.email          = form.email.data
        crm.website        = form.website.data
        crm.address        = form.address.data
        crm.contact_type   = form.contact_type.data
        crm.phone_number   = form.phone_number.data
        crm.city           = form.city.data
        crm.country        = form.country.data
        crm.employee_id    = Employee.query.filter_by(username=str(form.employee_id.data)).first().id
        crm.description    = form.description.data
        crm.status         = form.status.data

        crm.edit_item()
        
        flash('You have successfully edited the assignment.')

        send_sms(to_number=crm.phone_number,body='Edited assignment.')

        flash("Ubutumwa bwagiye neza!")

        return redirect(url_for('aicos_crm.table'))

    # form.department_id.data = current_user.email
    form.tag.data          = crm.tag
    form.company_name.data = crm.company_name
    form.email.data        = crm.email
    form.website.data      = crm.website
    form.address.data      = crm.address
    form.contact_type.data = crm.contact_type
    form.phone_number.data = crm.phone_number
    form.city.data         = crm.city
    form.country.data      = crm.country
    form.employee_id.data  = Employee.query.filter_by(id=crm.employee_id).first().username
    form.description.data  = crm.description
    form.status.data       = crm.status

    return render_template('new_item.html', action="Edit",
                           add_item=add_item, form=form,
                           crm=crm, title="Edit Assignment")

@aicos_crm.route('/add_new_item', methods=['GET', 'POST'])
def assign():
    # form = ItemForm()
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