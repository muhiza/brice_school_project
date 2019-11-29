import sys
import unittest

from flask_testing import TestCase
from app import create_app, db
 
from app.models import *

from datetime import datetime
import datetime
from flask import Flask, abort, url_for
from flask_login import current_user, login_user, login_manager


class TestBase(TestCase):

    def create_app(self):

        # pass in test configuration
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'mysql://juru:Password@123@localhost/testing'
        )
        app.config['LOGIN_DISABLED'] = True
        app.login_manager.init_app(app)
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        db.drop_all()
        db.create_all()

        self.admin = Employee(username="admin",email='admin@gmail.com', password="admin2016", is_admin=True)

        training = Training(name='name',trainer='trainer',about='about',description='description')
        apply = applyTraining(namea = 'name',abouta = 'about',descriptiona = 'description')

        db.session.add(self.admin)

        db.session.add(training)
        db.session.add(apply)

        db.session.commit()

        login_user(self.admin, remember=False, duration=None, force=True, fresh=True)

        login_manager.current_user=self.admin

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()


class TestModels(TestBase):

    def test_models(self):
        """
        Test number of records in tables
        """
        self.assertEqual(Employee.query.count(), 1)
        self.assertEqual(Training.query.count(), 1)
        self.assertEqual(applyTraining.query.count(), 1)


class TestViews(TestBase):

    def test_trainer_dashboard(self):
        target_url = url_for('aicos_trainer.trainer_dashboard')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(self.admin.is_active)
                    # training = Training.query.all()
        # training_count = Training.query.count()
        # applied_training = applyTraining.query.all()
        # applied_training_count = applyTraining.query.count()
        # return render_template('trainer_dashboard.html', title="E trainer templates",
        #                         training_count=training_count,
        #                         applied_training_count=applied_training_count)

    def test_trainingList(self):
        target_url = url_for('aicos_trainer.trainingList')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(self.admin.is_active)
            
        # applied_training = applyTraining.query.all()
        # return render_template('trainingList.html', applied_training=applied_training)

    def test_providedTrainingList(self):
        target_url = url_for('aicos_trainer.providedTrainingList')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(self.admin.is_active)
            
        # provided_training = Training.query.all()
        # return render_template('ProvidedTrainingList.html', provided_training=provided_training)

    def test_applyTrainingzx(self):
        target_url = url_for('aicos_trainer.applyTrainingzx')
        with self.client:
            response = self.client.post(target_url,data=dict(namea = 'ingingo',
                                    abouta = 'abouta',descriptiona = 'descriptiona'))
            self.assertEqual(response.status_code, 200)
            self.assertTrue(self.admin.is_active)
            
        # form = applyTrainingForm()
        # if validate_on_submit():

        #     newTraining = applyTraining(
        #                             namea = ingingo,
        #                             abouta = abouta,
        #                             descriptiona = descriptiona,
        #                             datea       = datea,
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

    



# class TestErrorPages(TestBase):

    # def test_403_forbidden(self):
    #     # create route to abort the request with the 403 Error
    #     @self.app.route('/403')
    #     def forbidden_error():
    #         abort(403)

    #     response = self.client.get('/403')
    #     self.assertEqual(response.status_code, 403)
    #     # self.assertTrue("403 Error" in response)

    # def test_404_not_found(self):
    #     response = self.client.get('/nothinghere')
    #     self.assertEqual(response.status_code, 404)
    #     # self.assertTrue("404 Error" in response)

    # def test_500_internal_server_error(self):
    #     # create route to abort the request with the 500 Error
    #     @self.app.route('/500')
    #     def internal_server_error():
    #         abort(500)

    #     response = self.client.get('/500')
    #     self.assertEqual(response.status_code, 500)
    #     # self.assertTrue("500 Error" in response)


if __name__ == '__main__':
    unittest.main()