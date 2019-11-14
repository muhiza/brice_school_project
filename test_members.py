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
        self.employee = Employee(username="test_user", password="test2016")
        
        department = Department(email='departoma123@gmail.com', name="IT", description="The IT Department")
        
        goal = Goal(name='name123',Description='description',Amount='amount',startingDate='startingDate',endingDate='endingDate')
        staff = Staff(first_name='firstName',last_name='lastName',nid='Nid',district='District',sector='Sector',
                      sex='Sex',yob='Yob',position='Position',education='Education',telephone='Telephone',
                      email='Email',monthly_net_salary='monthlyNetSalary')
        committee = Committee(first_name='firstName',last_name='lastName',nid='Nid',district='District',
                      sector='Sector',sex='Sex',yob='Yob',committee='Committee',position='Position',
                      education='Education',telephone='Telephone',email='Email',
                      monthly_net_salary='monthlyNetSalary')
        activity = Activity(name='name123',description='description2')
        asset = Asset(asset_type='assetType',asset_location='assetLocation',asset_value='assetValue',
                      description='description')
        role = Role(name="CEO 123", description="Run the whole company")
        payment = Payment(reason='name123',amount='amount',date='date')
        howto = Howto(name='name123',labels='labels',description='description',steps='steps',file='file')
        link = Link(link='link',title='title',labels='labels',sharewith='sharewith',comment='comment')
        report = Report(status='status',description='description')
        dec = Decision(status='status',decision='decision',owner='owner',stakeholders='stakeholders',
                      due_date='due_date',background='background')
        # contr = Contribution()
        com = Communication(ms_from='ms_from',to='to',message='message',comment='comment')
        notif = Notification(action="Communication",done_by=self.employee.username,done_from='IP',
                      done_time = "frank",done_to="tapayi",effect = "system upgraded")
        app = Application(emailaa='emailaa',firstNameaa='firstNameaa',secondNameaa='secondNameaa',
                      othersaa='othersaa',Districtaa='Districtaa',Sectoraa='Sectoraa',
                      Cellaa='Cellaa',nIdaa='nIdaa',entryDateaa='entryDateaa',shareaa='shareaa',
                      exitDateaa='exitDateaa',umuzunguraaa='umuzunguraaa',umukonoaa='umukonoaa',genderaa='genderaa',
                      dobaa='dobaa',phoneaa='phoneaa',Amashuriaa='Amashuriaa',Ubumugaaa='Ubumugaaa')
                      
        member = Member(sno=1000
        #,izina_ribanza='izina_ribanza',izina_rikurikira='izina_rikurikira'#,
        #               Ayandi ='Ayandi',zone ='zone',itsinda='itsinda',Igitsina='Igitsina',
        #               Indangamuntu='Indangamuntu',tariki_yavukiye='tariki_yavukiye',Intara='Intara',
        #               Akarere='Akarere',Umurenge='Umurenge',Akagari='Akagari',Umudugudu='Umudugudu',
        #               tariki_yinjiriye='tariki_yinjiriye',umugabane_ukwezi='umugabane_ukwezi',Umukono='Umukono',
        #               nomero_telephone='nomero_telephone',Amashuri='Amashuri',Ubumuga='Ubumuga',
        #               Arubatse='Arubatse',umubare_abana='umubare_abana',icyiciro_ubudehe='icyiciro_ubudehe',
        #               Ubwishingizi='Ubwishingizi',akazi_akora_muri_koperative='akazi_akora_muri_koperative',
        #               akazi_akora_ahandi='akazi_akora_ahandi',ubuso_ahingaho='ubuso_ahingaho',
        #               ubwoko_igihingwa='ubwoko_igihingwa',ubuso_ahingaho_ibindi='ubuso_ahingaho_ibindi',
        #               ubwoko_igihingwa_kindi='ubwoko_igihingwa_kindi',ubuso_budakoreshwa='ubuso_budakoreshwa'
                      )
        # subs = Subscription(subscribe_for='subscribe_for',description='description',subscription_plan='subscription_plan',
        #               subscription_date='subscription_date',credit_card_no='credit_card_no')
        zone = Zone(izina='izina',ubusobanuro='description',impamvu='impamvu')
        
        # save models instances to database

        db.session.add(admin)
        db.session.add(self.employee)
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

        with self.client:  
            resp = login_user(admin, remember=False, duration=None, force=True, fresh=True)
            self.assertTrue(resp)
            self.assertTrue(admin.is_authenticated)  
            # self.assertTrue(department.is_active)  
            self.assertFalse(admin.is_anonymous)  
            self.assertEqual(admin.id, int(admin.get_id()))

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestModels(TestBase):

    def test_models(self):
        """
        Test number of records in Role table
        """
        self.assertEqual(Employee.query.count(), 2)
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
    def aicos_members_home(self):
        target_url = 'indexz.html'

    def dashboard(self):
        target_url = 'home.html'

    def test_memberDetails(self):
        target_url = 'member_details.html'
        redirect_url = url_for('aicos_members.aicos_members_home',id=1, next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_cooper_det(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'deta/coop_det.html'
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)

    def test_memberPayments(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'payments/payment_list.html'
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)

    def test_goalPayments(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'payments/goals/newGoal.html'
        redirect_url = url_for('aicos_members.memberPayments', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_goalDelete(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        redirect_url = url_for('aicos_members.memberPayments')
        response1 = self.client.get(redirect_url)
        self.assertEqual(200, response1.status_code)

    def test_joiningChart(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'employees/joining_chart.html'

    def test_memberCreate(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'create/create.html'

    def test_list_roles(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'roles/roles.html'
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)

    def test_add_role(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = 'roles/role.html'
        redirect_url = url_for('aicos_members.list_roles', id=1, next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_list_staffs(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'roles/staffs.html'
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)

    def test_add_staff(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = 'roles/staff.html'
        redirect_url = url_for('aicos_members.list_staffs', id=1, next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_list_committees(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'roles/committees.html'
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)

    def test_add_committee(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = 'roles/committee.html'
        redirect_url = url_for('aicos_members.list_committees', id=1, next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_list_activities(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'roles/activities.html'
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)

    def test_add_activity(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = 'roles/activity.html'
        redirect_url = url_for('aicos_members.list_activities', id=1, next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_list_assets(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'roles/assets.html'
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)

    def test_add_asset(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        target_url = 'roles/asset.html'
        redirect_url = url_for('aicos_members.list_assets', id=1, next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_edit_role(self):
        """
        Test that edit_role view works as expected
        """
        target_url = 'roles/role.html'
        redirect_url = url_for('aicos_members.edit_role', id=1, next=target_url)
        response = self.client.post(target_url, data=dict(name='secondRoleName'),follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIs(report.name,'secondname')
        self.assertRedirects(response, redirect_url)

    # def test_delete_role(self):
    #     redirect_url = url_for('aicos_members.list_roles')
    #     response = self.client.get(redirect_url)
    #     self.assertEqual(200, response.status_code)
    #     self.assertEqual(Role.query.count(),0)

    def test_list_reports(self):
        target_url = 'tools/reports/reports.html'
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)

    def test_add_report(self):
        target_url = 'tools/reports/report.html'
        redirect_url = url_for('aicos_members.list_reports', id=1, next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_edit_report(self):
        """
        Test that edit_report view works as expected
        """
        target_url = 'tools/reports/report.html'
        redirect_url = url_for('aicos_members.list_reports', id=1, next=target_url)
        response = self.client.post(target_url, data=dict(name='secondname'),follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIs(report.name,'secondname')
        self.assertRedirects(response, redirect_url)
        # self.assertIn(b'Thanks for registering!', response2.data)

    def test_delete_report(self):
        redirect_url = url_for('aicos_members.list_reports')
        response1 = self.client.get(redirect_url)
        self.assertEqual(200, response1.status_code)

    def test_decisions_list(self):
        """
        Test that decisions_list page is inaccessible without login
        and redirects to login page then to decisions_list page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'tools/decisions_list.html'
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)

    def test_add_payment(self):
        target_url = 'payments/new_payment.html'
        redirect_url = url_for('aicos_members.list_roles', next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_create_decision(self):
        target_url = 'tools/create_decision.html'
        redirect_url = url_for('aicos_members.decisions_list', next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_how_to_list(self):
        target_url = 'tools/how_to/how_to_list.html'
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)

    def test_create_how_to(self):
        target_url = 'tools/how_to/create_how_to.html'
        redirect_url = url_for('aicos_members.how_to_list', next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_links_list(self):
        target_url = 'tools/links/links_list.html'
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)

    def test_create_link(self):
        target_url = 'tools/links/create_link.html'
        redirect_url = url_for('aicos_members.links_list', next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_create_file(self):
        target_url = 'tools/file/shareFile.html'
        redirect_url = url_for('aicos_members.links_list', next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_files_list(self):
        target_url = 'tools/file/filesList.html'
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)

    def test_list_employees(self):
        """
        Test that decisions_list page is inaccessible without login
        and redirects to login page then to decisions_list page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'employees/employees.html'
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)

    def test_member_details(self):
        """
        Test that member_details page is inaccessible without login
        and redirects to login page then to member_details page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'member_details.html'
        # redirect_url = url_for('aicos_members.list_employees', id=1, next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_doimportmbs(self):
        target_url = 'employees/upload.html'
        redirect_url = url_for('aicos_members.aicos_members_home')
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
        target_url = 'employees/membership_form.html'
        redirect_url = url_for('aicos_members.aicos_members_home', next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_reports_list(self):
        target_url = 'tools/reports_list.html'
        response = self.client.get(target_url)
        self.assertEqual(response.status_code,200)

    def test_create_report(self):
        """
        Test that create_report page is inaccessible without login
        and redirects to login page then to create_report page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'tools/create_report.html'
        redirect_url = url_for('aicos_members.reports_list', next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_create_meeting_notes(self):
        """
        Test that create_meeting_notes page is inaccessible without login
        and redirects to login page then to create_meeting_notes page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'tools/create_decision.html'
        redirect_url = url_for('aicos_members.decisions_list', next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_contributions_list(self):
        target_url = 'tools/contributions_list.html'
        response = self.client.get(target_url)
        self.assertEqual(response.status_code,200)

    def test_add_contribution(self):
        """
        Test that add_contribution page is inaccessible without login
        and redirects to login page then to add_contribution page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'tools/add_contribution.html'
        redirect_url = url_for('aicos_members.contributions_list', next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    # def test_pdf_template(self):

    def test_communications_list(self):
        target_url = 'tools/communications_list.html'
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)


    def test_add_communication(self):
        """
        Test that add_communication page is inaccessible without login
        and redirects to login page then to add_communication page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = 'tools/add_communication.html'
        redirect_url = url_for('aicos_members.communications_list', next=target_url)
        response1 = self.client.post(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_list_applications(self):
        """
        Test that applications page is inaccessible without login
        and redirects to login page then to applications page
        """
        target_url = 'employees/applied_members.html'
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

    # def test_applicant_details(self):
    #     """
    #     Test that applicatiapplicant_detailsons page is inaccessible without login
    #     and redirects to login page then to applicant_details page
    #     """
    #     target_url = 'employees/applicant_details.html'
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 200)
    #     # self.assertRedirects(response, redirect_url)

    # def test_assign_employee(self):
    #     """
    #     Test that assign_employee page is inaccessible without login
    #     and redirects to login page then to assign_employee page
    #     """
    #     target_url = 'employees/employee.html'
    #     redirect_url = url_for('aicos_members.assign_employee',id=self.employee.id, next=target_url)
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertRedirects(response, redirect_url)

    def test_delete_member(self):
        """
        Test that delete_member page is inaccessible without login
        and redirects to login page then to delete_member page
        """
        redirect_url = url_for('aicos_members.aicos_members_home')
        # response = self.client.get(redirect_url)
        # self.assertEqual(200,response.status_code)
        # self.assertEqual(Member.query.count(), 0)

    # def test_confirm_member(self):
    #     """
    #     Test that assign_employee page is inaccessible without login
    #     and redirects to login page then to confirm_member page
    #     """
    #     redirect_url = url_for('aicos_members.confirm_member',id=1)
    #     response = self.client.post(target_url,data=dict(email='email',
    #                   username='others',
    #                   first_name='first_name',
    #                   last_name='last_name',
    #                   department_id=current_user.email))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertRedirects(response, redirect_url)

    # def test_invite_members(self):
    #     target_url = 'home/invite_members.html'

    # def test_add_member(self):
    #     redirect_url = url_for('aicos_members.invite_members',id=self.employee.id)
    #     response = self.client.post(redirect_url)
    #     self.assertEqual(response.status_code,200)

    # def test_invite(self):
    #     redirect_url = url_for('aicos_members.invite_members',id=self.employee.id)
    #     response = self.client.post(redirect_url)
    #     self.assertEqual(response.status_code,200)

    # def test_sendsms(self):
    #     target_url = 'employees/sendsms.html'

    # def test_sendemail(self):
    #     target_url = 'employees/sendemail.html'

    # def test_subscriptions(self):
    #     """
    #     Test that subscriptions page is inaccessible without login
    #     and redirects to login page then to subscriptions page
    #     """
    #     target_url = url_for('departments/subscriptions.html')
    #     redirect_url = url_for('aicos_members.list_departments', next=target_url)
    #     response = self.client.post(target_url, data=dict(subscribe_for=form.subscribe_for.data,
    #                         description=form.description.data,
    #                         subscription_plan=form.subscription_plan.data,
    #                         subscription_date=form.subscription_date.data,
    #                         credit_card_no   =form.credit_card_no.data))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertRedirects(response, redirect_url)

    # def test_sendRemainder(self):
    #     """
    #     Test that sendRemainder page is inaccessible without login
    #     and redirects to login page then to sendRemainder page
    #     """
    #     target_url = 'employees/sendRemainder.html'
    #     # redirect_url = url_for('auth.login', next=target_url)
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 200)
    #     # self.assertRedirects(response, redirect_url)

    # def test_settings(self):
    #     target_url = 'settings.html'

    # def test_blank(self):
    #     target_url = 'tools/blank.html'

    # def test_coop_details(self):
    #     """
    #     Test that coop_details page is inaccessible without login
    #     and redirects to login page then to coop_details page
    #     """
    #     redirect_url = url_for('aicos_members.coop_details')
    #     target_url = 'cooperative_detail.html'
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 200)
    #     # self.assertRedirects(response, redirect_url)

    # def test_imyishyurire(self):
    #     target_url = '/imyishyurire/index.html'
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 200)

    # def test_zone(self):
    #     target_url = '/zones/zones.html'
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 200)

    # def test_addZone(self):
    #     redirect_url = url_for('aicos_members.zone')
    #     target_url = '/zones/add_zone.html'
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()