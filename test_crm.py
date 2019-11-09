# import os
import sys
import unittest

from flask_testing import TestCase
from app import create_app, db
 
from app.models import Department, Employee, CRM
from app.models import *

from datetime import datetime
import datetime
from flask import Flask, abort, url_for
from flask_login import current_user, LoginManager, login_user

from werkzeug.security import generate_password_hash, check_password_hash


# from sqlalchemy import DateTime

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

        # create test department
        self.department = Department(email='depar@gmail.com', name="IT", description="The IT Department")

        # create test non-admin user
        self.employee = Employee(email='joe@joes.com',username="test_user",
                    first_name='Joe',password="test2016",department = self.department)

        # create test self.crm_item
        self.crm_item = CRM(
                    department  = self.department,
                    tag='tag',company_name='company_name',
                    email='company_email@gmail.com',website='www.company_name.com',
                    address='company_address',contact_type='contact',
                    phone_number='+250788888888',city='city',
                    country='country',employee=self.employee,
                    description='description',status='status'
                    )

        # save models instances to database
        db.session.add(admin)
        db.session.add(self.employee)
        db.session.add(self.department)
        db.session.add(self.crm_item)
        db.session.commit()

        @login_manager.user_loader
        def load_user(user_id):
            return Department.query.get(int(user_id))

        # employee = Employee.query.filter_by(email='joe@joes.com').first()

        # with self.client:
        #     response = self.client.post(url_for('auth.login'),data=dict(email="joe@joes.com",password="test2016"))

        #     self.assertEqual(response.status_code, 200)
        #     # self.assertEqual(current_user.first_name, 'joe')

        #     self.assertIn(b"joe",response.data)

        #     self.assertTrue(employee.is_authenticated)  
        #     self.assertTrue(employee.is_active)  
        #     self.assertFalse(employee.is_anonymous)  
        #     self.assertEqual(employee.id, int(employee.get_id()))

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

        self.assertEqual(self.employee.username,'test_user')

    def test_department_model(self):
        """
        Test number of records in Department table
        """
        self.assertEqual(Department.query.count(), 1)

        self.assertEqual(self.department.email,'depar@gmail.com')
        self.assertEqual(self.department.name,'IT')
        self.assertEqual(self.department.description,'The IT Department')

    # def test_role_model(self):
    #     """
    #     Test number of records in Role table
    #     """

    #     # create test role
    #     role = Role(name="CEO", description="Run the whole company")

    #     # save role to database
    #     db.session.add(role)
    #     db.session.commit()

    #     self.assertEqual(Role.query.count(), 1)

    #     # self.assertEqual(self.new_review.movie_id,12345)
    #     # self.assertEqual(self.new_review.movie_title,'Review for movies')
    #     # self.assertEqual(self.new_review.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
    #     # self.assertEqual(self.new_review.movie_review,'This movie is the best thing since sliced bread')
    #     # self.assertEqual(self.new_review.user,self.user_James)

    def test_CRM_model(self):
        """
        Test number of records in CRMs table
        """
        self.assertEqual(CRM.query.count(), 1)

        self.assertEqual(self.crm_item.tag,'tag')
        self.assertEqual(self.crm_item.company_name,'company_name')
        self.assertEqual(self.crm_item.email,'company_email@gmail.com')
        self.assertEqual(self.crm_item.website,'www.company_name.com')
        self.assertEqual(self.crm_item.address,'company_address')
        self.assertEqual(self.crm_item.contact_type,'contact')
        self.assertEqual(self.crm_item.phone_number,'+250788888888')
        self.assertEqual(self.crm_item.city,'city')
        self.assertEqual(self.crm_item.country,'country')
        self.assertEqual(self.crm_item.employee,self.employee)
        self.assertEqual(self.crm_item.description,'description')
        self.assertEqual(self.crm_item.status,'status')

# class TestViews(TestBase):

#     def test_homepage_view(self):
#         """
#         Test that homepage is accessible without login
#         """
#         response = self.client.get(url_for('home.homepage'))
#         self.assertEqual(response.status_code, 200)

#     def test_login_view(self):
#         """
#         Test that login page is accessible without login
#         """
#         response = self.client.get(url_for('auth.login'))
#         self.assertEqual(response.status_code, 200)

    @login_manager.user_loader
    def test_login_fn(self):
        employee = Employee.query.filter_by(email='joe@joes.com').first()
        # db.session.add(employee)
        # db.session.commit()
        # print(employee.id)
        with self.client:
            response = self.client.post(url_for('auth.login'),data=dict(email="joe@joes.com",password="test2016"))

            self.assertEqual(response.status_code, 200)
            # self.assertEqual(current_user.first_name, 'joe')

            self.assertIn(b"joe",response.data)

            self.assertTrue(employee.is_authenticated)  
            self.assertTrue(employee.is_active)  
            self.assertFalse(employee.is_anonymous)  
            self.assertEqual(employee.id, int(employee.get_id()))

    # # def test_logout_view_redirects(self):
    # #     """
    # #     Test that logout link is inaccessible without login
    # #     and redirects to login page then to logout
    # #     """
    # #     target_url = url_for('auth.logout')
    # #     redirect_url = url_for('auth.login', next=target_url)
    # #     response = self.client.get(target_url)
    # #     self.assertEqual(response.status_code, 302)
    # #     self.assertRedirects(response, redirect_url)

    # def test_logout_view(self):
    #     """
    #     Test that logout works as expected
    #     """
    #     # Employee(first_name="Joe", email="joe@joes.com", password="12345")
    #     with self.client:
    #         target_url = url_for("auth.login")
    #         response = self.client.post(target_url,data=dict(email="joe@joes.com",password="12345"),follow_redirects=True)
            
    #         self.assertEqual(response.status_code, 200)
    #         # self.assertTrue(current_user.first_name == 'Joe')

    #         # self.assertFalse(current_user.is_anonymous())

    #         # self.client.get(url_for("auth.logout"))
    #         # self.assertTrue(current_user.is_anonymous())

    #         # self.assertIn(b"Umaze gusohoka muri konti yawe neza!.",response.data)
    #         # self.assertIn(b"Welcome patkennedy79@gmail.com!",response.data)
    #         self.assertIn(b"Nta konti ufite ?",response.data)
    #         self.assertIn(b"login",response.data)
    #         self.assertNotIn(b"logout",response.data)
    #         self.assertIn(b"register",response.data)

    # def test_dashboard_view(self):
    #     """
    #     Test that dashboard is inaccessible without login
    #     and redirects to login page then to dashboard
    #     """
    #     target_url = url_for('home.dashboard')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, redirect_url)

    # def test_admin_dashboard_view(self):
    #     """
    #     Test that dashboard is inaccessible without login
    #     and redirects to login page then to dashboard
    #     """
    #     target_url = url_for('home.admin_dashboard')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, redirect_url)

    # # def test_departments_view(self):
    # #     """
    # #     Test that departments page is inaccessible without login
    # #     and redirects to login page then to departments page
    # #     """
    # #     target_url = url_for('admin.list_departments')
    # #     redirect_url = url_for('auth.login', next=target_url)
    # #     response = self.client.get(target_url)
    # #     self.assertEqual(response.status_code, 302)
    # #     self.assertRedirects(response, redirect_url)

    # def test_roles_view(self):
    #     """
    #     Test that roles page is inaccessible without login
    #     and redirects to login page then to roles page
    #     """
    #     target_url = url_for('aicos_members.list_roles')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, redirect_url)

    # def test_employees_view(self):
    #     """
    #     Test that employees page is inaccessible without login
    #     and redirects to login page then to employees page
    #     """
    #     target_url = url_for('aicos_members.list_employees')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, redirect_url)





    # def test_CRM_items_table_view(self):
    #     """
    #     Test that crm_items_table page is inaccessible without login
    #     and redirects to login page then to crm_items_table page
    #     """        
    #     target_url = url_for('aicos_crm.table')
    #     # redirect_url = url_for('auth.login', next=target_url)
    #     response1 = self.client.get(target_url)
    #     # self.assertEqual(302, response1.status_code)
    #     # self.assertRedirects(response1, redirect_url)

    #     response2 = self.client.get(target_url,follow_redirects=True)
    #     self.assertEqual(response2.status_code, 200)

    # def test_add_CRM_item_view(self):
    #     """
    #     Test that new_crm_item_add page is inaccessible without login
    #     and redirects to login page then to new_crm_item_add page
    #     """        
    #     target_url = url_for('aicos_crm.add_item')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response1 = self.client.get(target_url)
    #     self.assertEqual(302, response1.status_code)
    #     self.assertRedirects(response1, redirect_url)

    def test_add_CRM_item_view_redirects(self):
        """
        Test that new_crm_item_add page redirects to table page
        """ 
        target_url = url_for('aicos_crm.add_item')
        redirect_url2 = url_for('aicos_crm.table', next=target_url)
        response2 = self.client.post(target_url,follow_redirects=True)
        self.assertEqual(response2.status_code, 200)
        # self.assertRedirects(response2, redirect_url2)
        # self.assertIn(b'Thanks for registering!', response2.data)

    @login_manager.user_loader
    def test_edit_CRM_item_view_redirects(self):
        """
        Test that crm_item_edit page is inaccessible without login
        and redirects to login page then to crm_item_edit page
        """
        # target_url = url_for('aicos_crm.edit_item', id=1, employee_id=2)
        # redirect_url = url_for('auth.login', next=target_url)
        # response1 = self.client.get(target_url)
        # self.assertEqual(302, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

        # @login_manager.user_loader
        # def load_user(department_id):
        #     return Department.query.get(department_id)

        crm_item = CRM.query.filter_by(department=self.department).first()

        employee = Employee.query.filter_by(department=self.department).first()

        resp = login_user(employee, remember=False, duration=None, force=True, fresh=True)
        self.assertTrue(resp)
        self.assertTrue(employee.is_authenticated)  
        # self.assertTrue(department.is_active)  
        self.assertFalse(employee.is_anonymous)  
        self.assertEqual(employee.id, int(employee.get_id()))

        target_url2 = url_for('aicos_crm.edit_item', id=crm_item.id, employee_id=employee.id)

        with self.client:

            # response2 = self.client.get(target_url2)
            # # self.assertEqual(response2.status_code,200)
            # # self.assertRedirects(response2, redirect_url2)        
                        
            response2 = self.client.post(target_url2, data=dict(description='SecondDescription'))
            redirect_url2 = url_for('aicos_crm.table', next=target_url2)
            self.assertEqual(response2.status_code,200)
            response3 = self.client.get(redirect_url2)
            self.assertIn(b'SecondDescription',response3.data)

    # def test_login_disabled_is_set(self):
    #     config_name = 'testing'
    #     app = create_app(config_name)
    #     with app.app_context():
    #         login_manager = LoginManager(self.app, add_context_processor=True)
    #         self.assertTrue(login_manager._login_disabled)

#     def test_edit_CRM_item_view(self):
#         """
#         Test that crm_item_edit view works as expected
#         """
#         # self.crm_item = CRM.query.filter_by(id=1).first()
#         # self.crm_item.tag = 'secondtag'

#         target_url = url_for('aicos_crm.edit_item', id=1, employee_id=2)
#         redirect_url = url_for('auth.login', next=target_url)
#         response2 = self.client.post(target_url)
#         self.assertEqual(response2.status_code, 302)
#         self.assertRedirects(response2, redirect_url)

#         # self.assertIs(self.crm_item.tag,'secondtag')
#         # self.assertRedirects(response2, redirect_url2)
#         # self.assertIn(b'Thanks for registering!', response2.data)

#     def test_remove_CRM_item_view_redirects(self):
#         """
#         Test that crm_item_remove page is inaccessible without login
#         and redirects to login page then to crm_item_remove page
#         """
#         # self.crm_item = CRM.query.filter_by(id=1).first()
#         target_url = url_for('aicos_crm.remove_item', id=1)
#         redirect_url = url_for('auth.login', next=target_url)
#         response1 = self.client.get(target_url)
#         self.assertEqual(302, response1.status_code)
#         self.assertRedirects(response1, redirect_url)

#         # self.assertMessageFlashed('You have successfully deleted the assignment.', category='message')

#     def test_remove_CRM_item_view(self):
#         """
#         Test that crm_item_remove view works as expected
#         """
#         # config_name = 'testing'
#         # app = create_app(config_name)
#         # app.config['LOGIN_DISABLED'] = True

#         # self.crm_item = CRM.query.filter_by(id=1).first()

#         target_url = url_for('aicos_crm.remove_item', id=1)
#         redirect_url = url_for('auth.login', next=target_url)
#         # response2 = self.client.get('aicos_crm.add_item',follow_redirects=True)
#         response3 = self.client.get(target_url)
#         self.assertStatus(response3, 302)
#         self.assertRedirects(response3, redirect_url)
#         # self.assertIn(b'Thanks for registering!', response3.data)

#         # self.assertIsNone(self.crm_item)



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