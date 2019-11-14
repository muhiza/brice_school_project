from flask import Flask, abort, url_for

# def test_check_admin(test_client,init_database):
#     target_url = ''

# def test_check_overall(test_client,init_database):
#     target_url = ''

# def test_check_coop_admin(test_client,init_database):
#     target_url = ''

# def test_check_rca(test_client,init_database):
#     target_url = 

def test_rca_dashboard(test_client,init_database):
    target_url = 'rca_dashboard.html'
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_rca_new_dashboard(test_client,init_database):
    target_url = 'rca/dashboard.html'
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_rca_cooperatives_overall(test_client,init_database):
    target_url = 'rca/cooperatives_dashboard.html'
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_members_overall(test_client,init_database):
    target_url = 'rca_members_overall.html'
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_dashboard_overalls(test_client,init_database):
    target_url = 'dashboard_overall.html'
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_dashboard_coop(test_client,init_database):
    target_url = 'dashboard_coop.html'
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_rca_coop_details(training,test_client,init_database):
    target_url = 'rca/rca_overall_cooperative_details.html'
    redirect_url = url_for('admin.list_employees',email=department.email)
    resp1 = test_client.get(target_url) 

    # assert resp1.status_code == 200 
    assert resp1 and redirect_url == redirects

def test_memberDetails(training,test_client,init_database):
    target_url = 'overall_member_details.html'
    redirect_url = url_for('aicos_members.aicos_members_home',id=member.id)
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_appliedTraining(test_client,init_database):
    target_url = 'training/appliedTrainigList.html'
    resp1 = test_client.get(target_url,follow_redirects=True) 

    assert resp1.status_code == 200 

def test_preparedTrainig(test_client,init_database):
    target_url = 'training/preparedTraining.html'
    resp1 = test_client.get(target_url) 

    assert resp1.status_code == 200 

def test_models(training,test_client,init_database):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    assert training.name == 'ingingo'
    assert training.trainer == 'trainer'
    assert training.about == 'about'
    assert training.description == 'description'
    assert training.sno == '1000'
    # assert Member.query.count() == 1 
    # assert training.Department. == 1 
    # assert training.applyTraining.query.count() == 1 
    # assert training.Notification.query.count() == 1 
    # assert training.Employee.query.count() == 1 
    # # assert Federation.query.count() == 1 
    # assert Training.query.count() == 1 

def test_prepareTraining(test_client, init_database):
    redirect_url = url_for('aicos_rca.appliedTrainig')
    target_url = url_for('aicos_rca.prepareTraining')

    resp1 = test_client.get(target_url, follow_redirects=True) 

    assert resp1.status_code == 200 
 



# # import os
# import sys
# import unittest

# from flask_testing import TestCase
# from app import create_app, db
 
# from app.models import Department, Employee, CRM
# from app.models import *

# from datetime import datetime
# import datetime
# from flask import Flask, abort, url_for
# from flask_login import current_user

# # from sqlalchemy import DateTime

# class TestBase(TestCase):

#     def create_app(self):

#         # pass in test configuration
#         config_name = 'testing'
#         app = create_app(config_name)
#         app.config.update(
#             SQLALCHEMY_DATABASE_URI = 'mysql://juru:Password@123@localhost/test'
#         )
#         return app

#     def setUp(self):
#         """
#         Will be called before every test
#         """

#         db.create_all()

#         # create test admin user
#         admin = Employee(username="admin", password="admin2016", is_admin=True)

#         # create test non-admin user
#         employee = Employee(username="test_user", password="test2016")

#         crm_item = CRM(
#                     # department  = self.department,

#                     tag            = 'tag',
#                     company_name   = 'company_name',
#                     email     = 'company_email@gmail.com',
#                     website   = 'www.company_name.com',
#                     address   = 'company_address',
#                     contact_type   = 'contact',
#                     phone_number   = '+250788888888',
#                     city           = 'city',
#                     country        = 'country',

#                     employee    = employee,

#                     description    = 'description',
#                     status         = 'status'
#                     )


#         # save crm_item and users to database
#         db.session.add(admin)
#         db.session.add(employee)
#         db.session.add(crm_item)
#         db.session.commit()

#         # print(employee.id)

#     def tearDown(self):
#         """
#         Will be called after every test
#         """

#         db.session.remove()
#         db.drop_all()


# class TestModels(TestBase):

#     def test_employee_model(self):
#         """
#         Test number of records in Employee table
#         """
#         self.assertEqual(Employee.query.count() == 2)

#     def test_department_model(self):
#         """
#         Test number of records in Department table
#         """

#         # create test department
#         department = Department(email='department@gmail.com', name="IT", description="The IT Department")

#         # save department to database
#         db.session.add(department)
#         db.session.commit()

#         self.assertEqual(Department.query.count() == 1)

#     def test_role_model(self):
#         """
#         Test number of records in Role table
#         """

#         # create test role
#         role = Role(name="CEO", description="Run the whole company")

#         # save role to database
#         db.session.add(role)
#         db.session.commit()

#         self.assertEqual(Role.query.count() == 1)

#     def test_CRM_model(self):
#         """
#         Test number of records in CRMs table
#         """
#         self.assertEqual(CRM.query.count() == 1)

# class TestViews(TestBase):

#     # def test_homepage_view(self):
#     #     """
#     #     Test that homepage is accessible without login
#     #     """
#     #     response = self.client.get(url_for('home.homepage'))
#     #     self.assertEqual(response.status_code, 200)

#     # def test_login_view(self):
#     #     """
#     #     Test that login page is accessible without login
#     #     """
#     #     response = self.client.get(url_for('auth.login'))
#     #     self.assertEqual(response.status_code, 200)

#     # def test_login_fn(self):
#     #     employee = Employee(first_name='Joe', email='joe@joes.com', password='12345')
#     #     with self.client:
#     #         response = self.client.post(url_for('auth.login',{'email': 'joe@joes.com', 'password': '12345'}))

#     #         self.assertTrue(employee.is_authenticated)
#     #         self.assertTrue(employee.is_active)
#     #         self.assertFalse(employee.is_anonymous)
#     #         self.assertEqual(employee.id, int(response.get_id()))

#     # def test_logout_view_redirects(self):
#     #     """
#     #     Test that logout link is inaccessible without login
#     #     and redirects to login page then to logout
#     #     """
#     #     target_url = url_for('auth.logout')
#     #     redirect_url = url_for('auth.login', next=target_url)
#     #     response = self.client.get(target_url)
#     #     self.assertEqual(response.status_code, 302)
#     #     self.assertRedirects(response, redirect_url)

#     # def test_logout_view(self):
#     #     """
#     #     Test that logout works as expected
#     #     """
#     #     Employee(first_name="Joe", email="joe@joes.com", password="12345")
#     #     with self.client:
#     #         target_url = url_for("auth.login",data={Employee:{"email": "joe@joes.com","password": "12345"}})
#     #         self.client.post(target_url)
#     #         self.assertTrue(current_user.first_name == 'Joe')
#     #         self.assertFalse(current_user.is_anonymous())

#     #         self.client.get(url_for("auth.logout"))
#     #         self.assertTrue(current_user.is_anonymous())

#     # def test_dashboard_view(self):
#     #     """
#     #     Test that dashboard is inaccessible without login
#     #     and redirects to login page then to dashboard
#     #     """
#     #     target_url = url_for('home.dashboard')
#     #     redirect_url = url_for('auth.login', next=target_url)
#     #     response = self.client.get(target_url)
#     #     self.assertEqual(response.status_code, 302)
#     #     self.assertRedirects(response, redirect_url)

#     # def test_admin_dashboard_view(self):
#     #     """
#     #     Test that dashboard is inaccessible without login
#     #     and redirects to login page then to dashboard
#     #     """
#     #     target_url = url_for('home.admin_dashboard')
#     #     redirect_url = url_for('auth.login', next=target_url)
#     #     response = self.client.get(target_url)
#     #     self.assertEqual(response.status_code, 302)
#     #     self.assertRedirects(response, redirect_url)

#     # # def test_departments_view(self):
#     # #     """
#     # #     Test that departments page is inaccessible without login
#     # #     and redirects to login page then to departments page
#     # #     """
#     # #     target_url = url_for('admin.list_departments')
#     # #     redirect_url = url_for('auth.login', next=target_url)
#     # #     response = self.client.get(target_url)
#     # #     self.assertEqual(response.status_code, 302)
#     # #     self.assertRedirects(response, redirect_url)

#     # def test_roles_view(self):
#     #     """
#     #     Test that roles page is inaccessible without login
#     #     and redirects to login page then to roles page
#     #     """
#     #     target_url = url_for('aicos_members.list_roles')
#     #     redirect_url = url_for('auth.login', next=target_url)
#     #     response = self.client.get(target_url)
#     #     self.assertEqual(response.status_code, 302)
#     #     self.assertRedirects(response, redirect_url)

#     # def test_employees_view(self):
#     #     """
#     #     Test that employees page is inaccessible without login
#     #     and redirects to login page then to employees page
#     #     """
#     #     target_url = url_for('aicos_members.list_employees')
#     #     redirect_url = url_for('auth.login', next=target_url)
#     #     response = self.client.get(target_url)
#     #     self.assertEqual(response.status_code, 302)
#     #     self.assertRedirects(response, redirect_url)





#     # def test_CRM_items_table_view(self):
#     #     """
#     #     Test that crm_items_table page is inaccessible without login
#     #     and redirects to login page then to crm_items_table page
#     #     """        
#     #     target_url = url_for('aicos_crm.table')
#     #     redirect_url = url_for('auth.login', next=target_url)
#     #     response1 = self.client.get(target_url)
#     #     self.assertEqual(302, response1.status_code)
#     #     self.assertRedirects(response1, redirect_url)

#     #     response2 = self.client.get(target_url,follow_redirects=True)
#     #     self.assertEqual(response2.status_code, 200)

#     # def test_add_CRM_item_view(self):
#     #     """
#     #     Test that new_crm_item_add page is inaccessible without login
#     #     and redirects to login page then to new_crm_item_add page
#     #     """        
#     #     target_url = url_for('aicos_crm.add_item')
#     #     redirect_url = url_for('auth.login', next=target_url)
#     #     response1 = self.client.get(target_url)
#     #     self.assertEqual(302, response1.status_code)
#     #     self.assertRedirects(response1, redirect_url)

#     # def test_add_CRM_item_view_redirects(self):
#     #     """
#     #     Test that new_crm_item_add page redirects to table page
#     #     """ 
#     #     target_url = url_for('aicos_crm.add_item')
#     #     redirect_url2 = url_for('aicos_crm.table', next=target_url)
#     #     response2 = self.client.post(target_url,follow_redirects=True)
#     #     self.assertEqual(response2.status_code, 200)
#     #     # self.assertRedirects(response2, redirect_url2)
#     #     # self.assertIn(b'Thanks for registering!', response2.data)

#     # def test_edit_CRM_item_view_redirects(self):
#     #     """
#     #     Test that crm_item_edit page is inaccessible without login
#     #     and redirects to login page then to crm_item_edit page
#     #     """
#     #     target_url = url_for('aicos_crm.edit_item', id=1, employee_id=2)
#     #     redirect_url = url_for('auth.login', next=target_url)
#     #     response1 = self.client.get(target_url)
#     #     self.assertEqual(302, response1.status_code)
#     #     self.assertRedirects(response1, redirect_url)

#     # def test_edit_CRM_item_view(self):
#     #     """
#     #     Test that crm_item_edit view works as expected
#     #     """
#     #     crm_item = CRM.query.filter_by(id=1).first()
#     #     crm_item.tag = 'secondtag'

#     #     target_url = url_for('aicos_crm.edit_item', id=1, employee_id=2)
#     #     response2 = self.client.post(target_url)
#     #     self.assertEqual(response2.status_code, 200)

#     #     self.assertIs(crm_item.tag,'secondtag')
#     #     # self.assertRedirects(response2, redirect_url2)
#     #     # self.assertIn(b'Thanks for registering!', response2.data)

#     # def test_remove_CRM_item_view_redirects(self):
#     #     """
#     #     Test that crm_item_remove page is inaccessible without login
#     #     and redirects to login page then to crm_item_remove page
#     #     """
#     #     # crm_item = CRM.query.filter_by(id=1).first()
#     #     target_url = url_for('aicos_crm.remove_item', id=1)
#     #     redirect_url = url_for('auth.login', next=target_url)
#     #     response1 = self.client.get(target_url)
#     #     self.assertEqual(302, response1.status_code)
#     #     self.assertRedirects(response1, redirect_url)

#     # def test_remove_CRM_item_view(self):
#     #     """
#     #     Test that crm_item_remove view works as expected
#     #     """
#     #     crm_item = CRM.query.filter_by(id=1).first()
#     #     target_url = url_for('aicos_crm.remove_item', id=1)
#     #     # redirect_url2 = url_for('aicos_crm.table', next=target_url)
#     #     # response2 = self.client.get('aicos_crm.add_item',follow_redirects=True)
#     #     response3 = self.client.get(target_url)
#     #     self.assertEqual(response3.status_code, 200)
#     #     # self.assertRedirects(response3, redirect_url2)
#     #     # self.assertIn(b'Thanks for registering!', response3.data)

#     #     self.assertIsNone(crm_item)

#     # def rca_dashboard(test_client,init_database):
#     #     #check_admin()
#     #     #check_overall()
#     #     #check_coop_admin()
#     #     employees = Member.query.all()
#     #     departments = Department.query.all()
#     #     all_depts = Department.query.count()
#     #     all_mbs = Member.query.count()
#     #     training = applyTraining.query.all()
#     #     training_count = applyTraining.query.count()


#     #     notifications = Notification.query.all()
#     #     return render_template("rca_dashboard.html", employees=employees, 
#     #                             notifications=notifications, departments=departments, 
#     #                             all_mbs=all_mbs, all_depts=all_depts, training_count=training_count,
#     #                             title="Dashboard Overall")





#     # def rca_new_dashboard(test_client,init_database):
#     #     #check_admin()
#     #     #check_overall()
#     #     #check_coop_admin()
#     #     employees = Member.query.all()
#     #     departments = Department.query.all()
#     #     all_depts = Department.query.count()
#     #     all_mbs = Member.query.count()
#     #     training = applyTraining.query.all()
#     #     federations = Federation.query.all()
#     #     training_count = applyTraining.query.count()


#     #     notifications = Notification.query.all()
#     #     return render_template("rca/dashboard.html", employees=employees, 
#     #                             notifications=notifications, departments=departments, 
#     #                             all_mbs=all_mbs, all_depts=all_depts, training_count=training_count,
#     #                             title="Dashboard Overall", federations=federations)





#     # Views for serving the overall administrator blocks.
#     def test_rca_cooperatives_overall(self):
#         """
#         Test that rca_cooperatives_overall page is inaccessible without login
#         and redirects to login page then to rca_cooperatives_overall page
#         """
#         # crm_item = CRM.query.filter_by(id=1).first()
#         target_url = url_for('aicos_crm.rca_cooperatives_overall')
#         redirect_url = url_for('auth.login', next=target_url)
#         response1 = self.client.get(target_url)
#         self.assertEqual(302, response1.status_code)
#         self.assertRedirects(response1, redirect_url)


#         # employees = Member.query.all()
#         # departments = Department.query.all()
#         # all_depts = Department.query.count()
#         # all_mbs = Employee.query.count()

#         # all_depts_kigali = Department.query.filter_by(province='Kigali City').count()
#         # all_depts_west = Department.query.filter_by(province='West').count()
#         # all_depts_north = Department.query.filter_by(province='North').count()
#         # all_depts_south = Department.query.filter_by(province='South').count()
#         # all_depts_east = Department.query.filter_by(province='East').count()


#         # return render_template("rca/cooperatives_dashboard.html", employees=employees, 
#         #                         departments=departments, all_mbs=all_mbs, all_depts=all_depts, 
#         #                         all_depts_kigali=all_depts_kigali,
#         #                         all_depts_south = all_depts_south,
#         #                         all_depts_north = all_depts_north,
#         #                         all_depts_east = all_depts_east,
#         #                         all_depts_west = all_depts_west,
#         #                         title="Dashboard Overall")


#     def test_members_overall(self):
#         """
#         Test that members_overall page is inaccessible without login
#         and redirects to login page then to members_overall page
#         """
#         # crm_item = CRM.query.filter_by(id=1).first()
#         target_url = url_for('aicos_crm.members_overall')
#         redirect_url = url_for('auth.login', next=target_url)
#         response1 = self.client.get(target_url)
#         self.assertEqual(302, response1.status_code)
#         self.assertRedirects(response1, redirect_url)


#         # #check_admin()
#         # #check_overall()
#         # check_rca()
#         # #check_coop_admin()
#         # employees = Member.query.all()
#         # departments = Department.query.all()
#         # all_depts = Department.query.count()
#         # all_mbs = Employee.query.count()



#         # employee = Department.query.filter_by(email=current_user.email).first()
#         # #employees = employee.members

#         # employees_male = Member.query.filter_by(gender='male')
#         # employees_male_count = Member.query.filter_by(gender='male').count()
#         # employees_female = Member.query.filter_by(gender='female')
#         # employees_female_count = Member.query.filter_by(gender='female').count()
#         # employees_abatarize = Member.query.filter_by(Amashuri='no')
#         # employees_abatarize_count = Member.query.filter_by(Amashuri='no').count()
#         # employees_abanza = Member.query.filter_by(Amashuri='low')
#         # employees_abanza_count = Member.query.filter_by(Amashuri='low').count()
#         # employees_ayisumbuye = Member.query.filter_by(Amashuri='medium')
#         # employees_ayisumbuye_count = Member.query.filter_by(Amashuri='medium').count()
#         # employees_kaminuza = Member.query.filter_by(Amashuri='high')
#         # employees_kaminuza_count = Member.query.filter_by(Amashuri='high').count()
#         # employees_imyuga = Member.query.filter_by(Amashuri='Imyuga')
#         # employees_imyuga_count = Member.query.filter_by(Amashuri='Imyuga').count()


#         # employees_amaguru = Member.query.filter_by(Ubumuga='Amaguru')
#         # employees_amaguru_count = Member.query.filter_by(Ubumuga='Amaguru').count()

#         # employees_amaboko = Member.query.filter_by(Ubumuga='Amaboko')
#         # employees_amaboko_count = Member.query.filter_by(Ubumuga='Amaboko').count()


#         # employees_kutabona = Member.query.filter_by(Ubumuga='Kutabona')
#         # employees_kutabona_count = Member.query.filter_by(Ubumuga='Kutabona').count()

#         # employees_kutumva = Member.query.filter_by(Ubumuga='Kutumva')
#         # employees_kutumva_count = Member.query.filter_by(Ubumuga='Kutumva').count()


#         # employees_mumutwe = Member.query.filter_by(Ubumuga='Mu mutwe')
#         # employees_mumutwe_count = Member.query.filter_by(Ubumuga='Mu mutwe').count()


#         # male_members = Member.query.filter_by(gender='Gole').first()
#         # #male_members_all = male_members.query.all()
#         # employees_count = Member.query.count()
#         # #if employees is not None:
#         # #employees = Employee.query.filter_by(email=form.email.data)

#         # apps = Department.query.filter_by(email=current_user.email).first()
#         # #applications = apps.applications


#         # return render_template("rca_members_overall.html", 
#         #                         employees=employees, 
#         #                         departments=departments, 
#         #                         all_mbs=all_mbs, 
#         #                         all_depts=all_depts, 
#         #                         title="Dashboard Overall",

#         #                         employee=employee, 
#         #                         employees_count=employees_count,
#         #                         male_members=male_members,
#         #                         employees_male=employees_male,
#         #                         employees_female=employees_female,
#         #                         employees_male_count=employees_male_count,
#         #                         employees_female_count=employees_female_count,
#         #                         employees_abatarize=employees_abatarize,
#         #                         employees_abatarize_count=employees_abatarize_count,
#         #                         employees_abanza=employees_abanza,
#         #                         employees_abanza_count=employees_abanza_count,
#         #                         employees_ayisumbuye=employees_ayisumbuye,
#         #                         employees_ayisumbuye_count=employees_ayisumbuye_count,
#         #                         employees_kaminuza=employees_kaminuza,
#         #                         employees_kaminuza_count=employees_kaminuza_count,
#         #                         employees_imyuga=employees_imyuga,
#         #                         employees_imyuga_count=employees_imyuga_count,
                                
#         #                         employees_amaguru=employees_amaguru,
#         #                         employees_amaguru_count=employees_amaguru_count,
#         #                         employees_amaboko=employees_amaboko,
#         #                         employees_amaboko_count=employees_amaboko_count,
#         #                         employees_kutabona=employees_kutabona,
#         #                         employees_kutabona_count=employees_kutabona_count,
#         #                         employees_kutumva=employees_kutumva,
#         #                         employees_kutumva_count=employees_kutumva_count,
#         #                         employees_mumutwe=employees_mumutwe,
#         #                         employees_mumutwe_count=employees_mumutwe_count,
#         #                         #male_members_count=male_members_count,
#         #                         #applications=applications,
#         #                         )




#     def test_dashboard_overalls(self):
#         """
#         Test that dashboard_overalls page is inaccessible without login
#         and redirects to login page then to dashboard_overalls page
#         """
#         # crm_item = CRM.query.filter_by(id=1).first()
#         target_url = url_for('aicos_crm.dashboard_overalls')
#         redirect_url = url_for('auth.login', next=target_url)
#         response1 = self.client.get(target_url)
#         self.assertEqual(302, response1.status_code)
#         self.assertRedirects(response1, redirect_url)


#         # #check_admin()
#         # check_overall()
#         # #check_coop_admin()
#         # employees = Member.query.all()
#         # departments = Department.query.all()
#         # all_depts = Department.query.count()
#         # all_mbs = Member.query.count()




#         # notifications = Notification.query.all()
#         # return render_template("dashboard_overall.html", employees=employees, 
#         #                         notifications=notifications, departments=departments, 
#         #                         all_mbs=all_mbs, all_depts=all_depts,
#         #                         title="Dashboard Overall")

#     def test_dashboard_coop(self):
#         """
#         Test that dashboard_coop page is inaccessible without login
#         and redirects to login page then to dashboard_coop page
#         """
#         # crm_item = CRM.query.filter_by(id=1).first()
#         target_url = url_for('aicos_crm.dashboard_coop')
#         redirect_url = url_for('auth.login', next=target_url)
#         response1 = self.client.get(target_url)
#         self.assertEqual(302, response1.status_code)
#         self.assertRedirects(response1, redirect_url)


#         # #check_admin()
#         # #check_coop_admin()
#         # employees = Member.query.all()
#         # departments = Department.query.all()
#         # all_depts = Department.query.count()
#         # all_mbs = Member.query.count()
#         # notes = Department.query.filter_by(email=current_user.email).first()
#         # notifications = Notification.query.filter_by(department_id='abahuza@gmail.com')

#         # return render_template("dashboard_coop.html", notifications=notifications, employees=employees, departments=departments, all_mbs=all_mbs, all_depts=all_depts, title="Dashboard Coop Admin")


#     # Views for the full details of a specific employee
#     def test_rca_coop_details(self):
#         """
#         Test that rca_coop_details page is inaccessible without login
#         and redirects to login page then to rca_coop_details page
#         """
#         department = Department.query.filter_by(id=1).first()
#         target_url = url_for('aicos_crm.rca_coop_details', email='department.email')
#         redirect_url = url_for('auth.login', next=target_url)
#         response1 = self.client.get(target_url)
#         self.assertEqual(302, response1.status_code)
#         self.assertRedirects(response1, redirect_url)


#         # #check_admin()

#         # #check_overall()
#         # #check_coop_admin()
#         # departments = Department.query.get_or_404(email)




#         # employees = departments.members
#         # employees_count = departments.members.count()
#         # employees_male = departments.members.filter_by(gender='Gabo')
#         # employees_male_count = departments.members.filter_by(gender='Gabo').count()
#         # employees_female = departments.members.filter_by(gender='Gole')
#         # employees_female_count = departments.members.filter_by(gender='Gole').count()
#         # employees_abatarize = departments.members.filter_by(Amashuri='Abatarize')
#         # employees_abatarize_count = departments.members.filter_by(Amashuri='Abatarize').count()
#         # employees_abanza = departments.members.filter_by(Amashuri='Abanza')
#         # employees_abanza_count = departments.members.filter_by(Amashuri='Abanza').count()
#         # employees_ayisumbuye = departments.members.filter_by(Amashuri='Ayisumbuye')
#         # employees_ayisumbuye_count = departments.members.filter_by(Amashuri='Ayisumbuye').count()
#         # employees_kaminuza = departments.members.filter_by(Amashuri='Kaminuza')
#         # employees_kaminuza_count = departments.members.filter_by(Amashuri='Kaminuza').count()
#         # employees_imyuga = departments.members.filter_by(Amashuri='Imyuga')
#         # employees_imyuga_count = departments.members.filter_by(Amashuri='Imyuga').count()


#         # employees_amaguru = departments.members.filter_by(Ubumuga='Amaguru')
#         # employees_amaguru_count = departments.members.filter_by(Ubumuga='Amaguru').count()

#         # employees_amaboko = departments.members.filter_by(Ubumuga='Amaboko')
#         # employees_amaboko_count = departments.members.filter_by(Ubumuga='Amaboko').count()


#         # employees_kutabona = departments.members.filter_by(Ubumuga='Kutabona')
#         # employees_kutabona_count = departments.members.filter_by(Ubumuga='Kutabona').count()

#         # employees_kutumva = departments.members.filter_by(Ubumuga='Kutumva')
#         # employees_kutumva_count = departments.members.filter_by(Ubumuga='Kutumva').count()


#         # employees_mumutwe = departments.members.filter_by(Ubumuga='Mu mutwe')
#         # employees_mumutwe_count = departments.members.filter_by(Ubumuga='Mu mutwe').count()


#         # male_members = departments.members.filter_by(gender='Gole').first()
#         # if departments is not None:
#         #     return render_template("rca/rca_overall_cooperative_details.html", departments=departments, 
#         #                             employees=employees,
#         #                         employees_count=employees_count,
#         #                         male_members=male_members,
#         #                         employees_male=employees_male,
#         #                         employees_female=employees_female,
#         #                         employees_male_count=employees_male_count,
#         #                         employees_female_count=employees_female_count,
#         #                         employees_abatarize=employees_abatarize,
#         #                         employees_abatarize_count=employees_abatarize_count,
#         #                         employees_abanza=employees_abanza,
#         #                         employees_abanza_count=employees_abanza_count,
#         #                         employees_ayisumbuye=employees_ayisumbuye,
#         #                         employees_ayisumbuye_count=employees_ayisumbuye_count,
#         #                         employees_kaminuza=employees_kaminuza,
#         #                         employees_kaminuza_count=employees_kaminuza_count,
#         #                         employees_imyuga=employees_imyuga,
#         #                         employees_imyuga_count=employees_imyuga_count,
                                
#         #                         employees_amaguru=employees_amaguru,
#         #                         employees_amaguru_count=employees_amaguru_count,
#         #                         employees_amaboko=employees_amaboko,
#         #                         employees_amaboko_count=employees_amaboko_count,
#         #                         employees_kutabona=employees_kutabona,
#         #                         employees_kutabona_count=employees_kutabona_count,
#         #                         employees_kutumva=employees_kutumva,
#         #                         employees_kutumva_count=employees_kutumva_count,
#         #                         employees_mumutwe=employees_mumutwe,
#         #                         employees_mumutwe_count=employees_mumutwe_count,
#         #                             title="Cooperative's details")
#         # return redirect(url_for('admin.list_employees'))


#     def test_memberDetails(self):
#         """
#         Test that memberDetails page is inaccessible without login
#         and redirects to login page then to memberDetails page
#         """
#         # crm_item = CRM.query.filter_by(id=1).first()
#         target_url = url_for('aicos_crm.memberDetails', id=1)
#         redirect_url = url_for('auth.login', next=target_url)
#         response1 = self.client.get(target_url)
#         self.assertEqual(302, response1.status_code)
#         self.assertRedirects(response1, redirect_url)


#         # check_admin()
#         # employee = Member.query.get_or_404(id)
#         # if employee is not None:
#         #     return render_template("overall_member_details.html", employee=employee)
#         # return redirect(url_for('aicos_members.aicos_members_home'))




#     # def appliedTrainig(test_client,init_database):
#     #     applied = applyTraining.query.all()
#     #     return render_template('training/appliedTrainigList.html', applied=applied)



#     # def preparedTrainig(test_client,init_database):
#     #     prepared = Training.query.all()
#     #     return render_template('training/preparedTraining.html', prepared=prepared)





#     # def prepareTraining(test_client,init_database):
#     #     form = TrainingForm()
#     #     if form.validate_on_submit(test_client,init_database):

#     #         prepareTraining = Training(
#     #                                 name = form.ingingo.data,
#     #                                 trainer = form.trainer.data,
#     #                                 about = form.about.data,
#     #                                 description = form.description.data,
#     #                                 date       = form.date.data
#     #                                 )
#     #         try:
#     #             db.session.add(prepareTraining)
#     #             db.session.commit()
#     #             flash("Umaze gutegura amahugurwa neza!")
#     #         except:
#     #             flash("Ntago amakuru watanze ameze neza!")
#     #         return redirect(url_for('aicos_rca.appliedTrainig'))
#     #     return render_template('training/prepareTraining.html', form=form)

# class TestErrorPages(TestBase):

#     def test_403_forbidden(self):
#         # create route to abort the request with the 403 Error
#         @self.app.route('/403')
#         def forbidden_error(test_client,init_database):
#             abort(403)

#         response = self.client.get('/403')
#         self.assertEqual(response.status_code, 403)
#         # self.assertTrue("403 Error" in response.data)

#     def test_404_not_found(self):
#         response = self.client.get('/nothinghere')
#         self.assertEqual(response.status_code, 404)
#         # self.assertTrue("404 Error" in response.data)

#     def test_500_internal_server_error(self):
#         # create route to abort the request with the 500 Error
#         @self.app.route('/500')
#         def internal_server_error(test_client,init_database):
#             abort(500)

#         response = self.client.get('/500')
#         self.assertEqual(response.status_code, 500)
#         # self.assertTrue("500 Error" in response.data)


# if __name__ == '__main__':
#     unittest.main()