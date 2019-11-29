# import os
import sys
import unittest

from flask_testing import TestCase
from app import *
from app import create_app, app, db
 
from app.models import *

from datetime import datetime
import datetime
from flask import Flask, abort, url_for

from flask_login import current_user, LoginManager, login_user,login_manager 

from app.aicos_members.views import check_admin,check_overall,check_accountant
from conftest import init_database,test_client

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

        coop = Cooperative(name='coop')

        self.admin = Employee(username="admin",email='admin@gmail.com', password="admin2016", is_admin=True)

        self.coop_admin = Employee(username='coop_admin',email='coop_admin@gmail.com',password='coop_admin2016',is_coop_admin=True)

        self.overall = Employee(username="overall",email='overall@gmail.com', password="overall2016", is_overall=True)
        
        self.accountant = Employee(username='accountant',email='accountant@gmail.com',password='accountant2016',is_accountant=True)

        department = Department(email='deparitoma1111@gmail.com', name="IT", description="The IT Department")
        
        goal = Goal(name='name1111',Description='description',Amount='amount',startingDate='startingDate',endingDate='endingDate')
        staff = Staff(first_name='firstName',last_name='lastName',nid='Nid',district='District',sector='Sector',
                      sex='Sex',yob='Yob',position='Position',education='Education',telephone='Telephone',
                      email='Email',monthly_net_salary='monthlyNetSalary')
        committee = Committee(first_name='firstName',last_name='lastName',nid='Nid',district='District',
                      sector='Sector',sex='Sex',yob='Yob',committee='Committee',position='Position',
                      education='Education',telephone='Telephone',email='Email',
                      monthly_net_salary='monthlyNetSalary')
        activity = Activity(name='name1111',description='description2')
        asset = Asset(asset_type='assetType',asset_location='assetLocation',asset_value='assetValue',
                      description='description')
        role = Role(name="CEO 1111", description="Run the whole company")
        payment = Payment(reason='name1111',amount='amount',date='date')
        howto = Howto(name='name1111',labels='labels',description='description',steps='steps',file='file')
        link = Link(link='link',title='title',labels='labels',sharewith='sharewith',comment='comment')
        report = Report(status='status',description='description')
        dec = Decision(status='status',decision='decision',owner='owner',stakeholders='stakeholders',
                      due_date='due_date',background='background')
        # contr = Contribution()
        com = Communication(ms_from='ms_from',to='to',message='message',comment='comment')
        notif = Notification(action="Communication",done_from='IP',done_time = "frank",
                      done_to="tapayi",effect = "system upgraded")
        app = Application(emailaa='emailaa',firstNameaa='firstNameaa',secondNameaa='secondNameaa',
                      othersaa='othersaa',Districtaa='Districtaa',Sectoraa='Sectoraa',
                      Cellaa='Cellaa',nIdaa='nIdaa',entryDateaa='entryDateaa',shareaa='shareaa',
                      exitDateaa='exitDateaa',umuzunguraaa='umuzunguraaa',umukonoaa='umukonoaa',genderaa='genderaa',
                      dobaa='dobaa',phoneaa='phoneaa',Amashuriaa='Amashuriaa',Ubumugaaa='Ubumugaaa')
                      
        member = Member(sno=111001)
        # subs = Subscription(subscribe_for='subscribe_for',description='description',subscription_plan='subscription_plan',
        #               subscription_date='subscription_date',credit_card_no='credit_card_no')
        zone = Zone(izina='izina',ubusobanuro='description',impamvu='impamvu')
        
        # save models instances to database

        db.session.add(coop)
        db.session.add(self.admin)
        db.session.add(self.coop_admin)
        db.session.add(self.overall)
        db.session.add(self.accountant)
        db.session.add(department)
        db.session.add(goal)
        db.session.add(staff)
        db.session.add(committee)
        db.session.add(activity)
        db.session.add(asset)
        db.session.add(role)
        db.session.add(payment)
        db.session.add(howto)
        db.session.add(link)
        db.session.add(report)
        db.session.add(dec)
        # db.session.add(contr)
        db.session.add(com)
        db.session.add(notif)
        db.session.add(app)
        db.session.add(member)
        # db.session.add(subs)
        db.session.add(zone)

        db.session.commit()


        # with self.client:
            # admin = self.admin 
            # resp = login_user(admin, remember=True, duration=None, force=True, fresh=True)
            # self.assertTrue(resp)
            # self.assertTrue(admin.is_authenticated)  
            # self.assertTrue(admin.is_active)  
            # self.assertFalse(admin.is_anonymous)  
            # self.assertEqual(admin.id, int(admin.get_id()))
            # # current_user = admin
            # # check_admin()

        self.client.post(url_for('auth.login'),data=dict(email="admim@gmail.com",password="admim2016"), follow_redirects=True)
        self.client.post(url_for('auth.login'),data=dict(email="coop_admim@gmail.com",password="coop_admim2016"), follow_redirects=True)
        self.client.post(url_for('auth.login'),data=dict(email="overall@gmail.com",password="overall2016"), follow_redirects=True)
        self.client.post(url_for('auth.login'),data=dict(email="accountant@gmail.com",password="accountant2016"), follow_redirects=True)

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.app.login_manager._current_user = Employee.query.filter_by(is_active=True)


        # self.client.force_login(self.admin)

        # with self.client:
            # response = self.client.post(url_for('auth.login'),data=dict(email="overall@gmail.com",password="overall2016"))
            # self.assertEqual(response.status_code, 200)
            # self.assertTrue(self.overall.is_authenticated)  
            # self.assertTrue(self.overall.is_active)  
            # self.assertFalse(self.overall.is_anonymous)  
            # self.assertEqual(self.overall.id, int(self.overall.get_id()))
            # current_user = self.overall
            # # check_overall()
        
        # with self.client:
            # response = self.client.post(url_for('auth.login'),data=dict(email="accountant@gmail.com",password="accountant2016"))
            # self.assertEqual(response.status_code, 200)
            # self.assertTrue(self.accountant.is_authenticated)  
            # self.assertTrue(self.accountant.is_active)  
            # self.assertFalse(self.accountant.is_anonymous)  
            # self.assertEqual(self.accountant.id, int(self.accountant.get_id()))
            # current_user = self.accountant
            # # check_accountant()


    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()


class TestModels(TestBase):

    def test_models(self):
        """
        Test number of records in models
        """
        assert Employee.query.count() == 4
        self.assertEqual(Department.query.count(), 1)
        self.assertEqual(Role.query.count(), 1)
        self.assertEqual(Goal.query.count(), 1)
        self.assertEqual(Staff.query.count(), 1)
        self.assertEqual(Committee.query.count(), 1)
        self.assertEqual(Activity.query.count(), 1)
        self.assertEqual(Asset.query.count(), 1)
        self.assertEqual(Payment.query.count(), 1)
        self.assertEqual(Howto.query.count(), 1)
        self.assertEqual(Link.query.count(), 1)
        self.assertEqual(Report.query.count(), 1)
        self.assertEqual(Decision.query.count(), 1)
        self.assertEqual(Communication.query.count(), 1)
        self.assertEqual(Notification.query.count(), 1)
        self.assertEqual(Application.query.count(), 1)
        self.assertEqual(Member.query.count(), 1)
        # self.assertEqual(Subscription.query.count(), 1)
        self.assertEqual(Zone.query.count(), 1)


class TestViews(TestBase):
#     def aicos_members_home(self):
        # target_url = 'indexz.html'

#     def dashboard(self):
#         target_url = 'home.html'

    # def test_memberDetails(test_client):
    #     target_url = 'member_details.html'
    #     redirect_url = url_for('aicos_members.aicos_members_home',id=1, next=target_url)

    #     response = test_client.get(target_url)
    #     assert 200 == response.status_code
    #     # self.assertRedirects(response1, redirect_url)
    
    # @login_manager.user_loader
    def test_login_fn(self):
        employee = Employee.query.filter_by(email='admin@gmail.com').first()
        with self.client:
            response = self.client.post(url_for('auth.login'),data=dict(email="admin@gmail.com",password="admin2016"))

            self.assertEqual(response.status_code, 200)

            self.assertTrue(employee.is_authenticated)  
            self.assertTrue(employee.is_active)  
            self.assertFalse(employee.is_anonymous)  
            self.assertEqual(employee.id, int(employee.get_id()))
    
    def test_cooper_det(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        with self.client:
            self.client.post(url_for('auth.login'),data=dict(email='admin@gmail.com',password='admin2016'))
            target_url = url_for('aicos_members.coop_details')
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_memberPayments(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.memberPayments')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_goalPayments(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = url_for('aicos_members.goalPayments')
        redirect_url = url_for('aicos_members.memberPayments', next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            response2 = self.client.get(redirect_url)
            self.assertEqual(200, response1.status_code)
            # self.assertRedirects(response1, redirect_url)

    def test_goalDelete(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = url_for('aicos_members.goalDelete', id=1)
        redirect_url = url_for('aicos_members.memberPayments', next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)
            # self.assertRedirects(response1, redirect_url)

    def test_joiningChart(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = url_for('aicos_members.joiningChart',email=self.admin.email)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_memberCreate(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = url_for('aicos_members.memberCreate')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_list_roles(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.list_roles')
        with self.client:
            response1 = self.client.get(target_url)

            self.assertTrue(self.admin.is_authenticated)
            current_user = self.admin
            if current_user.is_authenticated:
                self.assertEqual(200, response1.status_code)

    def test_add_role(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = url_for('aicos_members.add_role')
        redirect_url = url_for('aicos_members.list_roles', next=target_url)
        with self.client:
            response1 = self.client.post(target_url)
            self.assertEqual(200, response1.status_code)
            # self.assertRedirects(response1, redirect_url)

    def test_list_staffs(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.list_staffs')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_add_staff(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = url_for('aicos_members.add_staff',id=1)
        redirect_url = url_for('aicos_members.list_staffs', next=target_url)
        with self.client:
            response1 = self.client.post(target_url)
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    def test_list_committees(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.list_committees')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_add_committee(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = url_for('aicos_members.add_committee')
        redirect_url = url_for('aicos_members.list_committees', next=target_url)

        with self.client:
            response1 = self.client.post(target_url,data=dict(first_name='fname',last_name='lname'))
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    def test_list_activities(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.list_activities')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_add_activity(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = url_for('aicos_members.add_activity')
        redirect_url = url_for('aicos_members.list_activities', next=target_url)

        with self.client:
            response1 = self.client.post(target_url,data=dict(name='act2',description='desc2'))
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    def test_list_assets(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.list_assets')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_add_asset(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = url_for('aicos_members.add_asset')
        redirect_url = url_for('aicos_members.list_assets', next=target_url)

        with self.client:
            response1 = self.client.post(target_url,data=dict(asset_type='Maison',asset_location='Kagugu'))
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    # def test_edit_role(test_client):
    #     """
    #     Test that edit_role view works as expected
    #     """
    #     target_url = 'roles/role.html'
    #     redirect_url = url_for('aicos_members.edit_role', id=1, next=target_url)
    #     response = test_client.post(target_url, data=dict(name='secondRoleName'),follow_redirects=True)
        
    #     assert 200 == response.status_code
        # self.assertIs(report.name,'secondname')
        # self.assertRedirects(response, redirect_url)

    def test_delete_role(self):
        target_url = url_for('aicos_members.delete_role',id=1)
        redirect_url = url_for('aicos_members.list_roles')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(200, response.status_code)
            self.assertEqual(Role.query.count(),0)
            self.assertRedirects(response, redirect_url)

    def test_list_reports(self):
        target_url = url_for('aicos_members.list_roles')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_add_report(self):
        target_url = url_for('aicos_members.add_report')
        redirect_url = url_for('aicos_members.list_reports', id=1, next=target_url)

        with self.client:
            response1 = self.client.post(target_url)
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    # def test_edit_report(test_client):
    #     """
    #     Test that edit_report view works as expected
    #     """
    #     target_url = 'tools/reports/report.html'
    #     redirect_url = url_for('aicos_members.list_reports', id=1, next=target_url)
    #     response = test_client.post(target_url, data=dict(name='secondname'),follow_redirects=True)
        
    #     assert 200 == response.status_code
    # self.assertIs(report.name,'secondname')
    # self.assertRedirects(response, redirect_url)
#         # self.assertIn(b'Thanks for registering!', response2.data)

    def test_delete_report(self):
        target_url = url_for('aicos_members.delete_report',id=1)
        redirect_url = url_for('aicos_members.list_reports')
        # response1 = self.client.get(target_url)
        with self.client:
            response1 = self.client.get(redirect_url)
            self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response, redirect_url)

    def test_decisions_list(self):
        """
        Test that decisions_list page is inaccessible without login
        and redirects to login page then to decisions_list page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.decisions_list')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_add_payment(self):
        target_url = url_for('aicos_members.add_payment')
        redirect_url = url_for('aicos_members.list_roles', next=target_url)

        with self.client:
            response1 = self.client.post(target_url)
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    def test_create_decision(self):
        target_url = url_for('aicos_members.create_decision')
        redirect_url = url_for('aicos_members.decisions_list', next=target_url)

        with self.client:
            response1 = self.client.post(target_url)
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    def test_how_to_list(self):
        target_url = url_for('aicos_members.how_to_list')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_create_how_to(self):
        target_url = url_for('aicos_members.create_how_to')
        redirect_url = url_for('aicos_members.how_to_list', next=target_url)

        with self.client:
            response1 = self.client.post(target_url)
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    def test_links_list(self):
        target_url = url_for('aicos_members.links_list')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_create_link(self):
        target_url =url_for('aicos_members.create_link')
        redirect_url = url_for('aicos_members.links_list', next=target_url)

        with self.client:
            response1 = self.client.post(target_url)
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    def test_create_file(self):
        target_url = url_for('aicos_members.create_file')
        redirect_url = url_for('aicos_members.links_list', next=target_url)

        with self.client:
            response1 = self.client.post(target_url)
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    def test_files_list(self):
        target_url = url_for('aicos_members.files_list')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_list_employees(self):
        """
        Test that decisions_list page is inaccessible without login
        and redirects to login page then to decisions_list page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.list_employees')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_member_details(self):
        """
        Test that member_details page is inaccessible without login
        and redirects to login page then to member_details page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.member_details',id=1)
        # redirect_url = url_for('aicos_members.list_employees', id=1, next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_doimportmbs(self):
        target_url = url_for('aicos_members.doimportmbs')
        redirect_url = url_for('aicos_members.aicos_members_home', next=target_url)
        with self.client:
            response1 = self.client.post(target_url)
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

# #     def test_templateDownload(self):

    def test_AddNewMember(self):
        """
        Test that AddNewMember page is inaccessible without login
        and redirects to login page then to AddNewMember page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.AddNewMember')
        redirect_url = url_for('aicos_members.aicos_members_home', next=target_url)
        with self.client:
            response1 = self.client.post(target_url,data=dict(sno='30003'))
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    def test_reports_list(self):
        target_url = url_for('aicos_members.reports_list')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code,200)

    def test_create_report(self):
        """
        Test that create_report page is inaccessible without login
        and redirects to login page then to create_report page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.create_report')
        redirect_url = url_for('aicos_members.reports_list', next=target_url)
        with self.client:
            response1 = self.client.post(target_url)
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    def test_create_meeting_notes(self):
        """
        Test that create_meeting_notes page is inaccessible without login
        and redirects to login page then to create_meeting_notes page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.create_meeting_notes')
        redirect_url = url_for('aicos_members.decisions_list', next=target_url)

        with self.client:
            response1 = self.client.post(target_url)
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    def test_contributions_list(self):
        target_url = url_for('aicos_members.contributions_list')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code,200)

    def test_add_contribution(self):
        """
        Test that add_contribution page is inaccessible without login
        and redirects to login page then to add_contribution page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.add_contribution')
        redirect_url = url_for('aicos_members.contributions_list', next=target_url)

        with self.client:
            response1 = self.client.post(target_url)
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

#     # def test_pdf_template(self):

    def test_communications_list(self):
        target_url = url_for('aicos_members.communications_list')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)


    def test_add_communication(self):
        """
        Test that add_communication page is inaccessible without login
        and redirects to login page then to add_communication page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.add_communication')
        redirect_url = url_for('aicos_members.communications_list', next=target_url)

        with self.client:
            response1 = self.client.post(target_url)
            self.assertEqual(200, response1.status_code)
            self.assertRedirects(response1, redirect_url)

    def test_list_applications(self):
        """
        Test that applications page is inaccessible without login
        and redirects to login page then to applications page
        """
        target_url = url_for('aicos_members.list_applications')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

    def test_applicant_details(self):
        """
        Test that applicatiapplicant_detailsons page is inaccessible without login
        and redirects to login page then to applicant_details page
        """
        target_url = url_for('aicos_members.applicant_details',id=1)
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

    def test_assign_employee(self):
        """
        Test that assign_employee page is inaccessible without login
        and redirects to login page then to assign_employee page
        """
        target_url = url_for('aicos_members.assign_employee',id=2)
        # redirect_url = url_for('aicos_members.assign_employee',id=1, next=target_url)
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
            # self.assertRedirects(response, redirect_url)

    def test_delete_member(self):
        """
        Test that delete_member page is inaccessible without login
        and redirects to login page then to delete_member page
        """
        redirect_url = url_for('aicos_members.aicos_members_home',id=1)
        with self.client:
            response = self.client.get(redirect_url)
            self.assertEqual(200,response.status_code)
            self.assertEqual(Member.query.count(), 0)

    def test_confirm_member(self):
        """
        Test that assign_employee page is inaccessible without login
        and redirects to login page then to confirm_member page
        """
        target_url = url_for('aicos_members.confirm_member',id=1)
        with self.client:
            response = self.client.post(target_url,data=dict(email='email',
                        username='others',
                        first_name='first_name',
                        last_name='last_name',
                        department_id=current_user.email))
            self.assertEqual(response.status_code, 200)
            self.assertRedirects(response, redirect_url)

#     def test_invite_members(self):
#         target_url = 'home/invite_members.html'

    def test_add_member(self):
        redirect_url = url_for('aicos_members.add_member')
        with self.client:
            response = self.client.post(data=dict(sno='12345'))
            self.assertEqual(response.status_code,200)

    def test_invite(self):
        redirect_url = url_for('aicos_members.invite_members',id=1)
        with self.client:
            response = self.client.post(redirect_url)
            self.assertEqual(response.status_code,200)

#     def test_sendsms(self):
#         target_url = 'employees/sendsms.html'

#     def test_sendemail(self):
#         target_url = 'employees/sendemail.html'

    # def test_subscriptions(self):
    #     """
    #     Test that subscriptions page is inaccessible without login
    #     and redirects to login page then to subscriptions page
    #     """
    #     target_url = url_for('departments/subscriptions.html')
    #     redirect_url = url_for('aicos_members.list_departments', next=target_url)
    # #     response = self.client.post(target_url, data=dict(subscribe_for=form.subscribe_for.data,
    # #                         description=form.description.data,
    # #                         subscription_plan=form.subscription_plan.data,
    # #                         subscription_date=form.subscription_date.data,
    # #                         credit_card_no   =form.credit_card_no.data))
    # #     self.assertEqual(response.status_code, 200)
    #     self.assertRedirects(response, redirect_url)

    def test_sendRemainder(self):
        """
        Test that sendRemainder page is inaccessible without login
        and redirects to login page then to sendRemainder page
        """
        target_url = url_for('aicos_members.sendRemainder')
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

    # def test_settings(self):
    #     target_url = 'settings.html'

    # def test_blank(self):
    #     target_url = 'tools/blank.html'

    def test_coop_details(self):
        """
        Test that coop_details page is inaccessible without login
        and redirects to login page then to coop_details page
        """
        target_url = url_for('aicos_members.coop_details')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

    def test_imyishyurire(self):
        target_url = url_for('aicos_members.imyishyurire')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_zone(self):
        target_url = url_for('aicos_members.zone')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_addZone(self):
        redirect_url = url_for('aicos_members.zone')
        target_url = url_for('aicos_members.addZone')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()