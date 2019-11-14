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

# class TestViews(TestBase):

    # def test_trainer_dashboard(self):
        # training = Training.query.all()
        # training_count = Training.query.count()
        # applied_training = applyTraining.query.all()
        # applied_training_count = applyTraining.query.count()
        # return render_template('trainer_dashboard.html', title="E trainer templates",
        #                         training_count=training_count,
        #                         applied_training_count=applied_training_count)

    # def trainingList(self):
        # applied_training = applyTraining.query.all()
        # return render_template('trainingList.html', applied_training=applied_training)

    # def test_providedTrainingList(self):
        # provided_training = Training.query.all()
        # return render_template('ProvidedTrainingList.html', provided_training=provided_training)

    # def test_applyTrainingzx(self):
        # form = applyTrainingForm()
        # if form.validate_on_submit():

        #     newTraining = applyTraining(
        #                             namea = form.ingingo.data,
        #                             abouta = form.abouta.data,
        #                             descriptiona = form.descriptiona.data,
        #                             datea       = form.datea.data,
        #                             department_id = current_user.email
        #                             )
        #     try:
        #         db.session.add(newTraining)
        #         db.session.commit()
        #         flash("Umaze gusaba amahugurwa neza!")
        #     except:
        #         flash("Ntago amakuru watanze ameze neza!")
        #     return redirect(url_for('aicos_trainer.trainer_dashboard'))
        # return render_template('training.html', form=form)

    



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