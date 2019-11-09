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
        
        department = Department(email='department@gmail.com', name="IT", description="The IT Department")
        
        goal = Goal(name='name',Description='description',Amount='amount',startingDate='startingDate',endingDate='endingDate')
        staff = Staff(first_name='firstName',last_name='lastName',nid='Nid',district='District',sector='Sector',
                      sex='Sex',yob='Yob',position='Position',education='Education',telephone='Telephone',
                      email='Email',monthly_net_salary='monthlyNetSalary')
        committee = Committee(first_name='firstName',last_name='lastName',nid='Nid',district='District',
                      sector='Sector',sex='Sex',yob='Yob',committee='Committee',position='Position',
                      education='Education',telephone='Telephone',email='Email',
                      monthly_net_salary='monthlyNetSalary')
        activity = Activity(name='name',description='description')
        asset = Asset(asset_type='assetType',asset_location='assetLocation',asset_value='assetValue',
                      description='description')
        role = Role(name="CEO", description="Run the whole company")
        payment = Payment(reason='name',amount='amount',date='date')
        howto = Howto(name='name',labels='labels',description='description',steps='steps',file='file')
        link = Link(link='link',title='title',labels='labels',sharewith='sharewith',comment='comment')
        report = Report(status='status',description='description')
        dec = Decision(status='status',decision='decision',owner='owner',stakeholders='stakeholders',
                      due_date='due_date',background='background')
        contr = Contribution()
        com = Communication(ms_from='ms_from',to='to',message='message',comment='comment')
        notif = Notification(action="Communication",done_by=employee.username,done_from='IP',
                      done_time = "frank",done_to="tapayi",effect = "system upgraded")
        app = Application(emailaa='emailaa',firstNameaa='firstNameaa',secondNameaa='secondNameaa',
                      othersaa='othersaa',Districtaa='Districtaa',Sectoraa='Sectoraa',
                      Cellaa='Cellaa',nIdaa='nIdaa',entryDateaa='entryDateaa',shareaa='shareaa',
                      exitDateaa='exitDateaa',umuzunguraaa='umuzunguraaa',umukonoaa='umukonoaa',genderaa='genderaa',
                      dobaa='dobaa',phoneaa='phoneaa',Amashuriaa='Amashuriaa',Ubumugaaa='Ubumugaaa')
                      
        # member = Member(sno='sno',izina_ribanza='izina_ribanza',izina_rikurikira='izina_rikurikira',
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
        #               )
        # subs = Subscription(subscribe_for='subscribe_for',description='description',subscription_plan='subscription_plan',
        #               subscription_date='subscription_date',credit_card_no='credit_card_no')
        zone = Zone(izina='izina',ubusobanuro='description',impamvu='impamvu')
        
        # save models instances to database

        db.session.add(admin)
        db.session.add(employee)
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
        db.session.add(contr)
        db.session.add(com)
        db.session.add(notif)
        db.session.add(app)
        # db.session.add(member)
        # db.session.add(subs)
        db.session.add(zone)

        db.session.commit()

        # print(employee.id)

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestModels(TestBase):

    # def test_employee_model(self):
    #     """
    #     Test number of records in Employee table
    #     """

    # def test_department_model(self):
    #     """
    #     Test number of records in Department table
    #     """

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
        self.assertEqual(Employee.query.count(), 2)
        self.assertEqual(Decision.query.count(), 1)
        self.assertEqual(Communication.query.count(), 1)
        self.assertEqual(Notification.query.count(), 1)
        self.assertEqual(Application.query.count(), 1)
        # self.assertEqual(Member.query.count(), 1)
        # self.assertEqual(Subscription.query.count(), 1)
        self.assertEqual(Zone.query.count(), 1)


class TestViews(TestBase):

    def test_cooper_det(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.cooper_det')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    # def test_memberPayments(self):
    #     """
    #     Test that report_remove page is inaccessible without login
    #     and redirects to login page then to report_remove page
    #     """
    #     # report = CRM.query.filter_by(id=1).first()
    #     target_url = url_for('aicos_members.memberPayments')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response1 = self.client.get(target_url)
    #     self.assertEqual(302, response1.status_code)
    #     self.assertRedirects(response1, redirect_url)

    # def test_goalPayments(self):
    #     """
    #     Test that report_remove page is inaccessible without login
    #     and redirects to login page then to report_remove page
    #     """
    #     # report = CRM.query.filter_by(id=1).first()
    #     target_url = url_for('aicos_members.goalPayments')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response1 = self.client.get(target_url)
    #     self.assertEqual(302, response1.status_code)
    #     self.assertRedirects(response1, redirect_url)

    # def test_goalDelete(self):
    #     """
    #     Test that report_remove page is inaccessible without login
    #     and redirects to login page then to report_remove page
    #     """
    #     # report = CRM.query.filter_by(id=1).first()
    #     target_url = url_for('aicos_members.goalDelete')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response1 = self.client.get(target_url)
    #     self.assertEqual(302, response1.status_code)
    #     self.assertRedirects(response1, redirect_url)

    # def test_joiningChart(self):
    #     """
    #     Test that report_remove page is inaccessible without login
    #     and redirects to login page then to report_remove page
    #     """
    #     # report = CRM.query.filter_by(id=1).first()
    #     target_url = url_for('aicos_members.joiningChart')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response1 = self.client.get(target_url)
    #     self.assertEqual(302, response1.status_code)
    #     self.assertRedirects(response1, redirect_url)

    # def test_memberCreate(self):
    #     """
    #     Test that report_remove page is inaccessible without login
    #     and redirects to login page then to report_remove page
    #     """
    #     # report = CRM.query.filter_by(id=1).first()
    #     target_url = url_for('aicos_members.memberCreate')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response1 = self.client.get(target_url)
    #     self.assertEqual(302, response1.status_code)
    #     self.assertRedirects(response1, redirect_url)

    def test_list_roles(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.list_roles')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_add_role(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.add_role')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_list_staffs(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.list_staffs')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_add_staff(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.add_staff')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_list_committees(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.list_committees')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_add_committee(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.add_committee')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_list_activities(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.list_activities')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_add_activity(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.add_activity')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_list_assets(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.list_assets')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_add_asset(self):
        """
        Test that report_remove page is inaccessible without login
        and redirects to login page then to report_remove page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.add_asset')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_edit_role(self):
        """
        Test that edit_role view works as expected
        """
        role = Role.query.filter_by(id=1).first()
        role.name = 'RoleName'

        target_url = url_for('aicos_members.edit_role', id=1)
        response2 = self.client.post(target_url, report,follow_redirects=True)
        self.assertEqual(response2.status_code, 200)

        self.assertIs(role.name,'RoleName')
        # self.assertRedirects(response2, redirect_url2)
        # self.assertIn(b'Thanks for registering!', response2.data)
#     def test_delete_role():
#     def test_list_reports():
    # def test_add_report():
    def test_edit_report(self):
        """
        Test that edit_report view works as expected
        """
        report = Report.query.filter_by(id=1).first()
        report.name = 'secondname'

        target_url = url_for('aicos_members.edit_report', id=1)
        response2 = self.client.post(target_url, report,follow_redirects=True)
        self.assertEqual(response2.status_code, 200)

        self.assertIs(report.name,'secondname')
        # self.assertRedirects(response2, redirect_url2)
        # self.assertIn(b'Thanks for registering!', response2.data)

#     def test_delete_report(self):

    # def test_decisions_list(self):
    #     """
    #     Test that decisions_list page is inaccessible without login
    #     and redirects to login page then to decisions_list page
    #     """
    #     # report = CRM.query.filter_by(id=1).first()
    #     target_url = url_for('aicos_members.decisions_list')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response1 = self.client.get(target_url)
    #     self.assertEqual(302, response1.status_code)
    #     self.assertRedirects(response1, redirect_url)

    # def test_add_payment(self):
#     def test_create_decision(self):
#     def test_how_to_list(self):
#     def test_create_how_to(self):
#     def test_links_list(self):
#     def test_create_link(self):
#     def test_create_file(self):
#     def test_files_list(self):

    def test_list_employees(self):
        """
        Test that decisions_list page is inaccessible without login
        and redirects to login page then to decisions_list page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.list_employees')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    # def test_member_details(self):
    #     """
    #     Test that member_details page is inaccessible without login
    #     and redirects to login page then to member_details page
    #     """
    #     report = CRM.query.filter_by(id=1).first()
    #     target_url = url_for('aicos_members.member_details')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response1 = self.client.get(target_url)
    #     self.assertEqual(302, response1.status_code)
    #     self.assertRedirects(response1, redirect_url)

#     def test_doimportmbs(self):
#     def test_templateDownload(self):

    def test_AddNewMember(self):
        """
        Test that AddNewMember page is inaccessible without login
        and redirects to login page then to AddNewMember page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.AddNewMember')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

#     def test_reports_list(self):

    def test_create_report(self):
        """
        Test that create_report page is inaccessible without login
        and redirects to login page then to create_report page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.create_report')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_create_meeting_notes(self):
        """
        Test that create_meeting_notes page is inaccessible without login
        and redirects to login page then to create_meeting_notes page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.create_meeting_notes')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

#     def test_contributions_list(self):
    def test_add_contribution(self):
        """
        Test that add_contribution page is inaccessible without login
        and redirects to login page then to add_contribution page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.add_contribution')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

#     def test_pdf_template(self):
#     def test_communications_list(self):

    def test_add_communication(self):
        """
        Test that add_communication page is inaccessible without login
        and redirects to login page then to add_communication page
        """
        # report = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_members.add_communication')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_list_applications(self):
        """
        Test that applications page is inaccessible without login
        and redirects to login page then to applications page
        """
        target_url = url_for('aicos_members.list_applications')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_applicant_details(self):
        """
        Test that applicatiapplicant_detailsons page is inaccessible without login
        and redirects to login page then to applicant_details page
        """
        target_url = url_for('aicos_members.applicant_details')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_assign_employee(self):
        """
        Test that assign_employee page is inaccessible without login
        and redirects to login page then to assign_employee page
        """
        target_url = url_for('aicos_members.assign_employee')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_delete_member(self):
        """
        Test that delete_member page is inaccessible without login
        and redirects to login page then to delete_member page
        """
        target_url = url_for('aicos_members.delete_member')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_confirm_member(self):
        """
        Test that assign_employee page is inaccessible without login
        and redirects to login page then to confirm_member page
        """
        target_url = url_for('aicos_members.confirm_member')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

#     def test_invite_members():
    # def test_add_member():
#     def test_invite():
#     def test_sendsms():
#     def test_sendemail():

    def test_subscriptions(self):
        """
        Test that subscriptions page is inaccessible without login
        and redirects to login page then to subscriptions page
        """
        target_url = url_for('aicos_members.subscriptions')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_sendRemainder(self):
        """
        Test that sendRemainder page is inaccessible without login
        and redirects to login page then to sendRemainder page
        """
        target_url = url_for('aicos_members.sendRemainder')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

#     def test_settings():
#     def test_blank():

    def test_coop_details(self):
        """
        Test that coop_details page is inaccessible without login
        and redirects to login page then to coop_details page
        """
        target_url = url_for('aicos_members.coop_details')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

#     def test_imyishyurire():
#     def test_zone():
#     def test_addZone():


if __name__ == '__main__':
    unittest.main()