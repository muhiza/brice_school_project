# import os
import sys
import unittest

from flask_testing import TestCase
from app import create_app, db
 
from app.models import Department, Employee, CRM
from app.models import *
# from app.aicos_crm.forms import *
# from app.aicos_crm.views import *

from datetime import datetime
import datetime
from flask import Flask, abort, url_for

# from sqlalchemy import DateTime

# topdir = os.path.join(os.path.dirname(__file__),"..")
# sys.path.append(topdir)

# TEST_DB = 'test.db'


class TestBase(TestCase):

    def create_app(self):

        # pass in test configuration
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'mysql://juru:Password@123@localhost/test'
        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.create_all()

        # create test admin user
        admin = Employee(username="admin", password="admin2016", is_admin=True)

        # create test non-admin user
        employee = Employee(username="test_user", password="test2016")
        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

        print(employee.id)

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestModels(TestBase):

    def test_employee_model(self):
        """
        Test number of records in Employee table
        """
        self.assertEqual(Employee.query.count(), 2)

    def test_department_model(self):
        """
        Test number of records in Department table
        """

        # create test department
        department = Department(email='department@gmail.com', name="IT", description="The IT Department")

        # save department to database
        db.session.add(department)
        db.session.commit()

        self.assertEqual(Department.query.count(), 1)

    def test_role_model(self):
        """
        Test number of records in Role table
        """

        # create test role
        role = Role(name="CEO", description="Run the whole company")

        # save role to database
        db.session.add(role)
        db.session.commit()

        self.assertEqual(Role.query.count(), 1)

    def test_CRM_model(self):
        """
        Test number of records in CRMs table
        """
        # create test crm
        employee = Employee.query.filter_by(id=2).first()
        crm_item = CRM(
                    # department  = self.department,

                    tag            = 'tag',
                    company_name   = 'company_name',
                    email     = 'company_email@gmail.com',
                    website   = 'www.company_name.com',
                    address   = 'company_address',
                    contact_type   = 'contact',
                    phone_number   = '+250788888888',
                    city           = 'city',
                    country        = 'country',

                    employee    = employee,

                    description    = 'description',
                    status         = 'status'
                    )


        # save crm to database
        db.session.add(crm_item)
        db.session.commit()

        self.assertEqual(CRM.query.count(), 1)
        print(crm_item.id)


class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home.homepage'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        """
        Test that login page is accessible without login
        """
        response = self.client.get(url_for('auth.login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        """
        Test that logout link is inaccessible without login
        and redirects to login page then to logout
        """
        target_url = url_for('auth.logout')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_dashboard_view(self):
        """
        Test that dashboard is inaccessible without login
        and redirects to login page then to dashboard
        """
        target_url = url_for('home.dashboard')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_admin_dashboard_view(self):
        """
        Test that dashboard is inaccessible without login
        and redirects to login page then to dashboard
        """
        target_url = url_for('home.admin_dashboard')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    # def test_departments_view(self):
    #     """
    #     Test that departments page is inaccessible without login
    #     and redirects to login page then to departments page
    #     """
    #     target_url = url_for('admin.list_departments')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, redirect_url)

    def test_roles_view(self):
        """
        Test that roles page is inaccessible without login
        and redirects to login page then to roles page
        """
        target_url = url_for('aicos_members.list_roles')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_employees_view(self):
        """
        Test that employees page is inaccessible without login
        and redirects to login page then to employees page
        """
        target_url = url_for('aicos_members.list_employees')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_add_CRM_item_view(self):
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        
        target_url = url_for('aicos_crm.add_item')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, redirect_url)

    def test_edit_CRM_item_view(self):
        """
        Test that crm_item_edit page is inaccessible without login
        and redirects to login page then to crm_item_edit page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        # employee = Employee.query.filter_by(id=2).first()
        target_url = url_for('aicos_crm.edit_item', id=1, employee_id=2)
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_remove_CRM_item_view(self):
        """
        Test that crm_item_remove page is inaccessible without login
        and redirects to login page then to crm_item_remove page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_crm.remove_item', id=1)
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(302, response.status_code)

        # crm_item = CRM.query.filter_by(id=12345).first()
        # self.assertIsNone(find(crm_item))



class TestErrorPages(TestBase):

    def test_403_forbidden(self):
        # create route to abort the request with the 403 Error
        @self.app.route('/403')
        def forbidden_error():
            abort(403)

        response = self.client.get('/403')
        self.assertEqual(response.status_code, 403)
        # self.assertTrue("403 Error" in response.data)

    def test_404_not_found(self):
        response = self.client.get('/nothinghere')
        self.assertEqual(response.status_code, 404)
        # self.assertTrue("404 Error" in response.data)

    def test_500_internal_server_error(self):
        # create route to abort the request with the 500 Error
        @self.app.route('/500')
        def internal_server_error():
            abort(500)

        response = self.client.get('/500')
        self.assertEqual(response.status_code, 500)
        # self.assertTrue("500 Error" in response.data)


if __name__ == '__main__':
    unittest.main()






# class TestBase(TestCase):
#     '''

#     '''

#     # SQLALCHEMY_DATABASE_URI = "mysql://"
#     # TEST = True

#     ############################
#     #### setup and teardown ####
#     ############################

#     def create_app(self):

#         # pass in test configuration
#         config_name = 'testing'
#         app = create_app(config_name)
#         app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#         # app.config['TESTING'] = True
#         # app.config['WTF_CSRF_ENABLED'] = False
#         app.config.update(
#             SQLALCHEMY_DATABASE_URI = 'mysql://juru:Password@123@localhost/test'
#         )
        
#         return app


#     # executed prior to each test

#     def setUp(self):
#         # config_name = 'testing'
#         # app = create_app(config_name)
#         # app.config['TESTING'] = True
#         # app.config['WTF_CSRF_ENABLED'] = False
#         # app.config['SQLALCHEMY_BINDS'] = {'test':'mysql://juru:Password@123@localhost/test'}
#             # os.path.join(app.config['BASEDIR'], TEST)        
#         # self.app = app.test_client()
#         config_name = 'testing'
#         app = create_app(config_name)
#         with app.app_context():
#             # db.drop_all()
#             db.create_all()

#         self.department = Department(
#                     no = 100,code  = 'COP1000',name  = 'CORIKA',
#                     email = 'department@gmail.com',
#                     regdate = 'regdate',certificate = 'certificate',
#                     description = 'description',
#                     province    = 'province',district = 'district',
#                     sector      = 'sector',cell = 'cell',
#                     Activity    = 'act',coop_type = 'type',
#                     category   = 'category',field = 'field',
#                     started_data = datetime.datetime.now(),
#                     starting_share   = '200000',
#                     share_per_person = '20000', male_members = '40',
#                     female_members   = '60',is_active = 0
#                     )
#         self.employee = Employee(
#                     email = 'employee@gmail.com',
#                     username = 'uname',
#                     first_name = 'fname',
#                     last_name = 'lname',
#                     phone_number = '+250788000000',
#                     password_hash = db.Column(db.String(128)),

#                     department = self.department,

#                     is_admin = 1,is_coop_admin = 0,is_overall = 0,
#                     is_invited = 0,is_union   = 0,is_ferwacotamo = 0,
#                     is_confederation = 0,is_rca = 0,is_manager = 0,
#                     is_accountant = 0,is_production_manager = 0,
#                     invited_by = 'enviter',district   = 'district'
#                     )
#         self.emp1 = Employee(
#                     email = 'emp1@gmail.com',
#                     username = 'uname',
#                     first_name = 'fname',
#                     last_name = 'lname',
#                     phone_number = '+250788000000',
#                     password_hash = db.Column(db.String(128)),

#                     department = self.department,

#                     is_admin = 1,is_coop_admin = 0,is_overall = 0,
#                     is_invited = 0,is_union   = 0,is_ferwacotamo = 0,
#                     is_confederation = 0,is_rca = 0,is_manager = 0,
#                     is_accountant = 0,is_production_manager = 0,
#                     invited_by = 'enviter', district = 'Gasabo'
#                     )
#         self.new_item = CRM(
#                     department  = self.department,

#                     tag            = 'tag',
#                     company_name   = 'company_name',
#                     email     = 'company_email@gmail.com',
#                     website   = 'www.company_name.com',
#                     address   = 'company_address',
#                     contact_type   = 'contact',
#                     phone_number   = '+250788888888',
#                     city           = 'city',
#                     country        = 'country',

#                     employee    = self.employee,

#                     description    = 'description',
#                     status         = 'status'
#                     )

#         db.session.add(self.department)
#         db.session.add(self.employee)
#         db.session.add(self.emp1)
#         db.session.add(self.new_item)

#         config_name = 'testing'
#         app = create_app(config_name)
#         with app.app_context():
#             db.session.commit()


#     def tearDown(self):
#         # config_name = 'testing'
#         # app = create_app(config_name)
#         # db.session.remove()
#         # with app.app_context():
#         #     db.drop_all()

#         CRM.query.delete()
#         Employee.query.delete()
#         Department.query.delete()


#     # def tearDown(self):
#     #     # config_name = 'testing'
#     #     # app = create_app(config_name)
#     #     # db.session.remove()
#     #     # with app.app_context():
#     #     #     db.drop_all()

#     #     CRM.query.delete()
#     #     Employee.query.delete()
#     #     Department.query.delete()


#     ###############
#     #### tests ####
#     ###############

# class TestModels(TestBase):

#     def test_check_instance_variables(self):
#         self.assertEqual(self.new_item.department,self.department)
#         self.assertEqual(self.new_item.tag,'tag')
#         self.assertEqual(self.new_item.company_name,'company_name')
        
#         self.assertEqual(self.new_item.email,'company_email@gmail.com')
#         self.assertEqual(self.new_item.website,'www.company_name.com')
#         self.assertEqual(self.new_item.address,'company_address')
        
#         self.assertEqual(self.new_item.contact_type,"contact")
#         self.assertEqual(self.new_item.phone_number,'+250788888888')
#         self.assertEqual(self.new_item.city,'city')
#         self.assertEqual(self.new_item.country,'country')
        
#         self.assertEqual(self.new_item.employee,self.employee)
#         self.assertEqual(self.new_item.description,'description')
#         self.assertEqual(self.new_item.status,'status')



#     def test_add_new_item(self):
#         config_name = 'testing'
#         app = create_app(config_name)
#         with app.app_context():
#             self.new_item.add_new_item()
#         self.assertTrue(len(CRM.query.all())>0)

#     def test_edit_item(self):
#         # self.new_item.add_new_item()
#         employee = self.employee
#         self.new_item.employee = self.emp1
#         self.new_item.edit_item()
#         self.assertTrue(len(CRM.query.all())>0)
#         self.assertEquals(self.new_item.employee.email,self.emp1.email)

#     def test_delete_item(self):

#         # self.new_item.add_new_item()
#         self.new_item.delete_item()
#         self.assertIsNone(self.new_item)
#         self.assertTrue(len(got_reviews) == 0)
# # We then test the get_reviews class method that we pass in the id of a movie and get a response which is a review for that movie.


#     # def test_add_CRM_item(self):
#     #     """
#     #     Test that 
#     #     """
#     #     # create an employee, a department and a crm_item
        
#     #     # config_name = 'testing'
#     #     # app = create_app(config_name)
#     #     # with app.app_context(), app.test_request_context():
#     #     crm_item = self.client.get(url_for('aicos_crm.add_item'))

#     #     self.assertEqual(201, crm_item.status_code)
#     #     # self.assertEqual('application/json', r1.content_type)
#     #     # d1 = json.loads(r1.get_data(as_text=True))
#     #     # self.assertEqual('A Random Species', d1['species'])

#     #     # config_name = 'testing'
#     #     # app = create_app(config_name)             

#     #     # with app.app_context():
#     #         # db.session.add(department)
#     #         # db.session.add(crm_item)
#     #         # db.session.commit()

#     #     # query the crm_item and destroy the session
#     #     # with app.app_context():
#     #         # crm_item = CRM.query.get(12345)
#     #         # db.session.remove()
#     #     # delete the crm_item using a new session
#     #         # db.session = db.create_scoped_session()
#     #         # db.session.delete(crm_item)
#     #         # db.session.commit()

#     # def test_edit_CRM_item(self):
#     #     """
#     #     Test that employees page is inaccessible without login
#     #     and redirects to login page then to employees page
#     #     """
#     #     # config_name = 'testing'
#     #     # app = create_app(config_name)        
#     #     # with app.app_context(), app.test_request_context():

#     #     target_url = url_for('aicos_crm.edit_item', id=12345, employee_id=1 )
#     #     redirect_url = url_for('aicos_crm.table', next=target_url)
#     #     response = self.client.get(target_url)
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertRedirects(response, redirect_url)

#     #     # self.insert_tree()
#     #     # r1 = self.app.patch('/trees/123', data=json.dumps({
#     #     #     'species': 'A random species',
#     #     #     'description': 'Hey look... a description!'
#     #     # }), headers={
#     #     #     'Accept': 'application/json', 'Content-Type': 'application/json', 'user_id': '1'
#     #     # })
#     #     # self.assertEqual(200, r1.status_code)
#     #     # self.assertEqual('application/json', r1.content_type)
#     #     # d1 = json.loads(r1.get_data(as_text=True))
#     #     # self.assertEqual('A random species', d1['species'])
#     #     # self.assertEqual('Hey look... a description!', d1['description'])


#     # def test_remove_CRM_item(self):
#     #     """
#     #     Test that CRM items table page has the number of items minus one
#     #     after removing one item
#     #     """
#     #     # config_name = 'testing'
#     #     # app = create_app(config_name)        
#     #     # with app.app_context():
#     #     #     crm_item = CRM.query.get(12345)
#     #     #     db.session.remove()
#     #     # delete the crm_item using a new session
#     #         # db.session = db.create_scoped_session()
#     #         # db.session.delete(crm_item)
#     #         # db.session.commit()
        
#     #     # self.insert_tree()
#     #     # crm_item = CRM.query.get(12345)
#     #     # with app.app_context(), app.test_request_context():
#     #     crm_item = self.client.delete(url_for('aicos_crm.edit_item', id=12345))
        
#     #     crm_item.remove_item()
#     #     self.assertEqual(204, crm_item.status_code)

#     #     crm_item = CRM.query.filter_by(id=12345).first()
#     #     self.assertIsNone(crm_item)


    
# if __name__ == '__main__':
#     unittest.main()