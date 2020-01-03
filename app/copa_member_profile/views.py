"""
This is the views file that is processing the new users registrations
and processing the registered users who are logging in
"""
# Third-party imports
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user

# Internal imports.
from . import member_profile
from .. import db


#The route for registration page and processing.
@member_profile.route('/')
def member_home_page():
    return render_template('tab1.html', title='Home')




#The route for registration page and processing.
@member_profile.route('/memberStock')
def member_stock():
    return render_template('tab2.html', title='Home')




#The route for registration page and processing.
@member_profile.route('/memberFinance')
def member_finance():
    return render_template('tab3.html', title='Home')




#The route for registration page and processing.
@member_profile.route('/memberShare')
def member_share():
    return render_template('tab4.html', title='Home')


 
#The route for registration page and processing.
@member_profile.route('/memberNotification')
def member_notification():
    return render_template('tab5.html', title='Home')


