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
        # app.config.update(
            # SQLALCHEMY_DATABASE_URI = 'mysql://juru:Password@123@localhost/testing'
        # )
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.create_all()

        # create test department
        self.department = Department(email='dep3@gmail.com', name="Finance", description="The Finance Department")
        
        # create test role
        # role = Role(name="COO3",description="Run the Overall Operations",department=self.department)

        # create test coop_admin
        self.coop_admin = Employee(username="admin", password="admin2016", is_coop_admin=True)

        # create test admin user
        self.admin = Employee(username="admin", password="admin2016", is_admin=True)

        # create test non-admin user
        self.employee = Employee(username="test_user",email="test_user@gmail.com",password="test2016", is_overall=True)

        # crm_item = CRM(
        #             department  = self.department,
        #             tag            = 'tag',
        #             company_name   = 'company_name',
        #             email     = 'company_email@gmail.com',
        #             website   = 'www.company_name.com',
        #             address   = 'company_address',
        #             contact_type   = 'contact',
        #             phone_number   = '+250788888888',
        #             city           = 'city',
        #             country        = 'country',
        #             employee    = self.employee,
        #             description    = 'description',
        #             status         = 'status'
        #             )

        self.profile = Profile(
                        primary_school='primary_school',secondary_school='secondary_school',
                        university_school='university_school',vocational_school='vocational_school',
                        exp1='exp1',exp2='exp2',exp3='exp3',strn1='strn1',strn2='strn2',strn3='strn3',
                        car1='car1',car2='car2',car3='car3',district='district',
                        inter1='inter1',inter2='inter2',inter3='inter3'
                        )

        self.applicant = Application(
                        emailaa='Emaila',firstNameaa='firstNamea',secondNameaa='secondNamea',
                        othersaa='othersa',Districtaa='Districta',Sectoraa='Sectora',
                        Cellaa='Cella',nIdaa='nIda',entryDateaa='entryDatea',
                        shareaa='sharea',exitDateaa='exitDatea',umuzunguraaa='umuzunguraa',
                        umukonoaa='umukonoa',genderaa='gendera',dobaa='ormdoba',
                        phoneaa='phonea',Amashuriaa='amashuria',
                        Ubumugaaa='ubumugaa',department=self.department
                        )

        # save models to database
        # db.session.add(self.department)
        db.session.add(self.coop_admin)
        db.session.add(self.admin)
        db.session.add(self.employee)
        # db.session.add(crm_item)
        db.session.add(self.profile)
     
        db.session.commit()

        # @login_manager.user_loader
        # def load_user(user_id):
        #     return Employee.query.get(int(user_id))

        with self.client:
            employee = self.employee

            response = self.client.post(url_for('auth.login'),data=dict(email="joe@joes.com",password="test2016"))

            self.assertEqual(response.status_code, 200)
            # self.assertEqual(current_user.first_name, 'joe')

            self.assertIn(b"joe",response.data)

            self.assertTrue(employee.is_authenticated)  
            self.assertTrue(employee.is_active)  
            self.assertFalse(employee.is_anonymous)  
            self.assertEqual(employee.id, int(employee.get_id()))

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
        self.assertEqual(Employee.query.count(), 3)

    def test_department_model(self):
        """
        Test number of records in Department table
        """
        self.assertEqual(Department.query.count(), 1)

    # def test_role_model(self):
    #     """
    #     Test number of records in Role table
    #     """
    #     self.assertEqual(Role.query.count(), 1)

    # def test_CRM_model(self):
    #     """
    #     Test number of records in CRMs table
    #     """
    #     self.assertEqual(CRM.query.count(), 1)

class TestViews(TestBase):
    def test_check_admin(self):
        admin = Employee.query.filter_by(is_admin=True).first()
        current_user = admin
        self.assertTrue(current_user.is_admin)

    def test_check_overall(self):
        employee = Employee.query.filter_by(is_overall=True).first()
        current_user = employee
        self.assertTrue(current_user.is_overall)

    def test_check_coop_admin(self):
        coop_admin = Employee.query.filter_by(is_coop_admin=True).first()
        current_user = coop_admin
        self.assertTrue(current_user.is_coop_admin)

    def test_homepage(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home.homepage'))
        self.assertEqual(response.status_code, 200)

    def test_allSolutions(self):
        target_url = 'home/allSolutions.html'
        response1 = self.client.get(target_url)
        self.assertTrue(response1.status_code,200)

    def test_pay(self):
        target_url = url_for('home.homepage')
        response1 = self.client.get(target_url)
        self.assertTrue(response1.status_code,200)

    def test_dashboard(self):
        target_url = 'home/dashboard.html'
        response1 = self.client.get(target_url)
        self.assertTrue(response1.status_code,200)

    def test_products(self):
        target_url = 'home/products.html'
        response1 = self.client.get(target_url)
        self.assertTrue(response1.status_code,200)

    def test_admin_dashboard(self):
        target_url = 'home/admin_dashboard.html'
        response1 = self.client.get(target_url)
        self.assertTrue(response1.status_code,200)

    def test_admin_home_dashboard(self):
        target_url = 'home/admin_home_dashboard.html'
        response1 = self.client.get(target_url)
        self.assertTrue(response1.status_code,200)

    def test_join_cooperative(self):
        target_url = 'home/all_cooperatives.html'
        response1 = self.client.get(target_url)
        self.assertTrue(response1.status_code,200)

    def test_search_coop(self):
        target_url = 'home/search_coop.html'
        response1 = self.client.get(target_url)
        self.assertTrue(response1.status_code,200)

    def test_table_search(self):
        target_url = 'home/table_search.html'
        response1 = self.client.get(target_url)
        self.assertTrue(response1.status_code,200)

    # def test_done(self):
    #     target_url = 'done.html'
    #     response1 = self.client.get(target_url)
    #     self.assertTrue(response1.status_code,200)

    def test_coopInfo(self):
        department = Department(
            email='dep3@gmail.com', name="Finance3", description="The Finance Department3")
        
        target_url = 'home/coop_info.html'
        redirect_url = url_for('home.coopInfo',email=department.email)

        response1 = self.client.post(target_url,data=dict(
            email='dep4@gmail.com', name="Finance4", description="The Finance Department4"))

        self.assertEqual(response1.status_code,200)
        self.assertRedirects(response1,redirect_url)

    def test_newApplication(self):
        target_url = 'home/new_coop.html'
        redirect_url = url_for('home.done')

        response1 = self.client.post(target_url,data=dict(
            email='dep3@gmail.com', name='Finance', description='The Finance Department'))

        self.assertEqual(response1.status_code,200)
        self.assertRedirects(response1,redirect_url)

    # def test_sendCode(self):
    #     redirect_url = url_for('home.done')
    #     response1 = self.client.get(redirect_url)
    #     self.assertTrue(response1.status_code,200)

    def test_thankyou(self):
        target_url = 'home/thankyou.html'
        response1 = self.client.get(target_url)
        self.assertTrue(response1.status_code,200)

    def test_cooperative_details(self):
        target_url = 'home/cooperative_details.html'
        response1 = self.client.get(target_url)
        self.assertTrue(response1.status_code,200)

    def test_coop_categories(self):
        target_url = 'home/cooperatives_categories.html'
        response1 = self.client.get(target_url)
        self.assertTrue(response1.status_code,200)

    # def test_user_profile(self):
    #     target_url = 'home/user_profile.html'
    #     response1 = self.client.get(target_url)
    #     self.assertTrue(response1.status_code,200)

    def test_accept(self):
        target_url = 'home/user_profile.html'
        response1 = self.client.get(target_url)
        self.assertTrue(response1.status_code,200)

    def test_application(self):
        target_url = 'home/application.html'
        redirect_url = url_for('home.thankyou')

        response1 = self.client.post(target_url,
                    data=dict(
                        emailaa='Emaila',firstNameaa='firstNamea',secondNameaa='secondNamea',
                        othersaa='othersa',Districtaa='Districta',Sectoraa='Sectora',
                        Cellaa='Cella',nIdaa='nIda',entryDateaa='entryDatea',
                        shareaa='sharea',exitDateaa='exitDatea',umuzunguraaa='umuzunguraa',
                        umukonoaa='umukonoa',genderaa='gendera',dobaa='ormdoba',
                        phoneaa='phonea',Amashuriaa='amashuria',
                        Ubumugaaa='ubumugaa',department=self.department
                    )
                    )

        self.assertEqual(response1.status_code,200)
        self.assertRedirects(response1,redirect_url)

    def test_user_profile_about(self):
        target_url = 'home/user_profile_about.html'
        redirect_url = url_for('home.user_profile',id=self.employee.id,username=self.employee.username)
        
        response1 = self.client.post(target_url,
                    data=dict(
                        primary_school='primary_school',secondary_school='secondary_school',
                        university_school='university_school',vocational_school='vocational_school',
                        exp1='exp1',exp2='exp2',exp3='exp3',strn1='strn1',strn2='strn2',strn3='strn3',
                        car1='car1',car2='car2',car3='car3',district='district',
                        inter1='inter1',inter2='inter2',inter3='inter3'
                    )
                    )
        
        self.assertEqual(response1.status_code,200)
        self.assertRedirects(response1,redirect_url)

# class TestErrorPages(TestBase):

#     def test_403_forbidden(self):
#         # create route to abort the request with the 403 Error
#         @self.app.route('/403')
#         def forbidden_error():
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
#         def internal_server_error():
#             abort(500)

#         response = self.client.get('/500')
#         self.assertEqual(response.status_code, 500)
#         # self.assertTrue("500 Error" in response.data)


if __name__ == '__main__':
    unittest.main()