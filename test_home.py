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
from flask_login import current_user

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

        # create test non-admin user
        employee = Employee(username="test_user", password="test2016")

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


        # save crm_item and users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.add(crm_item)
        db.session.commit()

        # print(employee.id)

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
        self.assertEqual(CRM.query.count(), 1)

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

    def test_login_fn(self):
        employee = Employee(first_name='Joe', email='joe@joes.com', password='12345')
        with self.client:
            response = self.client.post(url_for('auth.login',{'email': 'joe@joes.com', 'password': '12345'}))

            self.assertTrue(employee.is_authenticated)
            self.assertTrue(employee.is_active)
            self.assertFalse(employee.is_anonymous)
            self.assertEqual(employee.id, int(response.get_id()))

    def test_logout_view_redirects(self):
        """
        Test that logout link is inaccessible without login
        and redirects to login page then to logout
        """
        target_url = url_for('auth.logout')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_logout_view(self):
        """
        Test that logout works as expected
        """
        Employee(first_name="Joe", email="joe@joes.com", password="12345")
        with self.client:
            target_url = url_for("auth.login",data={Employee:{"email": "joe@joes.com","password": "12345"}})
            self.client.post(target_url)
            self.assertTrue(current_user.first_name == 'Joe')
            self.assertFalse(current_user.is_anonymous())

            self.client.get(url_for("auth.logout"))
            self.assertTrue(current_user.is_anonymous())

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





    def test_CRM_items_table_view(self):
        """
        Test that crm_items_table page is inaccessible without login
        and redirects to login page then to crm_items_table page
        """        
        target_url = url_for('aicos_crm.table')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

        response2 = self.client.get(target_url,follow_redirects=True)
        self.assertEqual(response2.status_code, 200)

    def test_add_CRM_item_view(self):
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        
        target_url = url_for('aicos_crm.add_item')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

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

    def test_edit_CRM_item_view_redirects(self):
        """
        Test that crm_item_edit page is inaccessible without login
        and redirects to login page then to crm_item_edit page
        """
        target_url = url_for('aicos_crm.edit_item', id=1, employee_id=2)
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_edit_CRM_item_view(self):
        """
        Test that crm_item_edit view works as expected
        """
        crm_item = CRM.query.filter_by(id=1).first()
        crm_item.tag = 'secondtag'

        target_url = url_for('aicos_crm.edit_item', id=1, employee_id=2)
        response2 = self.client.post(target_url)
        self.assertEqual(response2.status_code, 200)

        self.assertIs(crm_item.tag,'secondtag')
        # self.assertRedirects(response2, redirect_url2)
        # self.assertIn(b'Thanks for registering!', response2.data)

    def test_remove_CRM_item_view_redirects(self):
        """
        Test that crm_item_remove page is inaccessible without login
        and redirects to login page then to crm_item_remove page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_crm.remove_item', id=1)
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_remove_CRM_item_view(self):
        """
        Test that crm_item_remove view works as expected
        """
        crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_crm.remove_item', id=1)
        # redirect_url2 = url_for('aicos_crm.table', next=target_url)
        # response2 = self.client.get('aicos_crm.add_item',follow_redirects=True)
        response3 = self.client.get(target_url)
        self.assertEqual(response3.status_code, 200)
        # self.assertRedirects(response3, redirect_url2)
        # self.assertIn(b'Thanks for registering!', response3.data)

        self.assertIsNone(crm_item)



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