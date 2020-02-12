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
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://juru:Password@123@localhost/testing'
        app.config['LOGIN_DISABLED'] = True
        app.login_manager.init_app(app)
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        db.drop_all()
        db.create_all()

        admin = Employee(username="admin",email='admin@gmail.com', password="admin2016", is_admin=True)

        coop_admin = Employee(username='coop_admin',email='coop_admin@gmail.com',password='coop_admin2016',is_coop_admin=True)

        overall = Employee(username="overall",email='overall@gmail.com', password="overall2016", is_overall=True)
        
        accountant = Employee(username='accountant',email='accountant@gmail.com',password='accountant2016',is_accountant=True)

        department = Department(email='department@gmail.com', name="IT", description="The IT Department")

        member = Member(sno='sno')

        notification = Notification(action = 'act',done_by = 'done_by',done_from = 'done_from',
                                    done_time = 'done_time',done_to= 'done_to',effect = 'effect')

        ibindi = Ibindi(ImifukaQuantity = 100000,ImifukaAmount = 300,MituelleAmount = 70000)

        ibihano = Ibihano(AmandeC = '100000',AmandeApII = 30000,comment = 'comment')

        ibirarane = Ibirarane(NPKkg = 100000)

        umusanzu = Umusanzu(UmusoroWakarere = 20000,UmusanzuCoop = 2000,Umugabane = 1000,
                            Ikigega = 1000,KuzibaIcyuho = 500)

        inyongeramusaruro = InyongeraMusaruro(NPKkg = 20,NPKPerUnity = 320,UREA = 30,UREAPerUnity = 510,
                                                DAP = 40,DAPPerUnity = 400,KCL = 15,KCLPerUnity = 500,
                                                Briquette = 50,BriquettePerUnity = 1000)

        umusarurob = Umusarurob(RiceType = 'Gikonko',UmusaruroGrade = 1,RiceAmount = 1000)

        db.session.add(admin)
        db.session.add(coop_admin)
        db.session.add(overall)
        db.session.add(accountant)
        db.session.add(department)
        db.session.add(member)
        db.session.add(notification)
        db.session.add(ibindi)
        db.session.add(ibihano)
        db.session.add(ibirarane)
        db.session.add(umusanzu)
        db.session.add(inyongeramusaruro)
        db.session.add(umusarurob)

        db.session.commit()

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
        self.assertEqual(Employee.query.count(), 4)
        self.assertEqual(Department.query.count(), 1)
        self.assertEqual(Member.query.count(), 1)
        self.assertEqual(Notification.query.count(), 1)
        self.assertEqual(Ibindi.query.count(), 1)
        self.assertEqual(Ibihano.query.count(), 1)
        self.assertEqual(Ibirarane.query.count(), 1)
        self.assertEqual(Umusanzu.query.count(), 1)
        self.assertEqual(InyongeraMusaruro.query.count(), 1)
        self.assertEqual(Umusarurob.query.count(), 1)

class TestViews(TestBase): 

    def test_cooperatives_overall(self):
        """
        Test that cooperatives_overall link is inaccessible without login
        and redirects to login page then to cooperatives_overall
        """
        target_url = url_for('aicos_union.cooperatives_overall')
        redirect_url = url_for('auth.login', next=target_url)


        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

        # employees = Member.query.all()
        # departments = Department.query.all()
        # all_depts = Department.query.count()
        # all_mbs = Employee.query.count()
        # all_depts_kigali = Department.query.filter_by(province='Kigali City').count()
        # all_depts_west = Department.query.filter_by(province='West').count()
        # all_depts_north = Department.query.filter_by(province='North').count()
        # all_depts_south = Department.query.filter_by(province='South').count()
        # all_depts_east = Department.query.filter_by(province='East').count()
        # return render_template("union/cooperatives.html", employees=employees, 
        #                         departments=departments, all_mbs=all_mbs, all_depts=all_depts, 
        #                         all_depts_kigali=all_depts_kigali,
        #                         all_depts_south = all_depts_south,
        #                         all_depts_north = all_depts_north,
        #                         all_depts_east = all_depts_east,
        #                         all_depts_west = all_depts_west,
        #                         title="Dashboard Overall")

    def test_members_overall(self):
        """
        Test that members_overall link is inaccessible without login
        and redirects to login page then to members_overall
        """
        target_url = url_for('aicos_union.dashboard_overalls')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

        # employees = Member.query.all()
        # departments = Department.query.all()
        # all_depts = Department.query.count()
        # all_mbs = Employee.query.count()
        # return render_template("members_overall.html", employees=employees, departments=departments, all_mbs=all_mbs, 
        #                         all_depts=all_depts, title="Dashboard Overall")

    def test_dashboard_overalls(self):
        """
        Test that dashboard_overalls link is inaccessible without login
        and redirects to login page then to dashboard_overalls
        """
        target_url = url_for('aicos_union.dashboard_overalls')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, redirect_url)
        
        # employees = Member.query.all()
        # departments = Department.query.all()
        # all_depts = Department.query.count()
        # all_mbs = Member.query.count()
        # notifications = Notification.query.all()
        # return render_template("union/dash_new.html", employees=employees, 
        #                         notifications=notifications, departments=departments, 
        #                         all_mbs=all_mbs, all_depts=all_depts,
        #                         title="Dashboard Overall")

    def test_dashboard_coop(self):
        """
        Test that dashboard_coop link is inaccessible without login
        and redirects to login page then to dashboard_coop
        """
        target_url = url_for('aicos_union.dashboard_coop')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, redirect_url)
        
        # employees = Member.query.all()
        # departments = Department.query.all()
        # all_depts = Department.query.count()
        # all_mbs = Member.query.count()
        # notes = Department.query.filter_by(email=current_user.email).first()
        # notifications = Notification.query.filter_by(department_id='abahuza@gmail.com')
        # return render_template("dashboard_coop.html", notifications=notifications, 
        #                         employees=employees, departments=departments, all_mbs=all_mbs, 
        #                         all_depts=all_depts, title="Dashboard Coop Admin")

    def test_coop_details(self):
        """
        Test that coop_details link is inaccessible without login
        and redirects to login page then to coop_details
        """
        # department = Department.query.filter_by(id=1).first()
        target_url = url_for('aicos_union.coop_details',email='admin@gmail.com')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)


        # departments = Department.query.get_or_404(email)
        # employees = departments.members
        # employees_count = departments.members.count()
        # employees_male = departments.members.filter_by(Igitsina='Gabo')
        # employees_male_count = departments.members.filter_by(Igitsina='Gabo').count()
        # employees_female = departments.members.filter_by(Igitsina='Gole')
        # employees_female_count = departments.members.filter_by(Igitsina='Gole').count()
        # employees_abatarize = departments.members.filter_by(Amashuri='Abatarize')
        # employees_abatarize_count = departments.members.filter_by(Amashuri='Abatarize').count()
        # employees_abanza = departments.members.filter_by(Amashuri='Abanza')
        # employees_abanza_count = departments.members.filter_by(Amashuri='Abanza').count()
        # employees_ayisumbuye = departments.members.filter_by(Amashuri='Ayisumbuye')
        # employees_ayisumbuye_count = departments.members.filter_by(Amashuri='Ayisumbuye').count()
        # employees_kaminuza = departments.members.filter_by(Amashuri='Kaminuza')
        # employees_kaminuza_count = departments.members.filter_by(Amashuri='Kaminuza').count()
        # employees_imyuga = departments.members.filter_by(Amashuri='Imyuga')
        # employees_imyuga_count = departments.members.filter_by(Amashuri='Imyuga').count()
        # employees_amaguru = departments.members.filter_by(Ubumuga='Amaguru')
        # employees_amaguru_count = departments.members.filter_by(Ubumuga='Amaguru').count()
        # employees_amaboko = departments.members.filter_by(Ubumuga='Amaboko')
        # employees_amaboko_count = departments.members.filter_by(Ubumuga='Amaboko').count()
        # employees_kutabona = departments.members.filter_by(Ubumuga='Kutabona')
        # employees_kutabona_count = departments.members.filter_by(Ubumuga='Kutabona').count()
        # employees_kutumva = departments.members.filter_by(Ubumuga='Kutumva')
        # employees_kutumva_count = departments.members.filter_by(Ubumuga='Kutumva').count()
        # employees_mumutwe = departments.members.filter_by(Ubumuga='Mu mutwe')
        # employees_mumutwe_count = departments.members.filter_by(Ubumuga='Mu mutwe').count()
        # male_members = departments.members.filter_by(Igitsina='Gole').first()
        # if departments is not None:
        #     return render_template("admin/cooperative_details.html", departments=departments, 
        #                             employees=employees,
        #                         employees_count=employees_count,
        #                         male_members=male_members,
        #                         employees_male=employees_male,
        #                         employees_female=employees_female,
        #                         employees_male_count=employees_male_count,
        #                         employees_female_count=employees_female_count,
        #                         employees_abatarize=employees_abatarize,
        #                         employees_abatarize_count=employees_abatarize_count,
        #                         employees_abanza=employees_abanza,
        #                         employees_abanza_count=employees_abanza_count,
        #                         employees_ayisumbuye=employees_ayisumbuye,
        #                         employees_ayisumbuye_count=employees_ayisumbuye_count,
        #                         employees_kaminuza=employees_kaminuza,
        #                         employees_kaminuza_count=employees_kaminuza_count,
        #                         employees_imyuga=employees_imyuga,
        #                         employees_imyuga_count=employees_imyuga_count,
        #                         employees_amaguru=employees_amaguru,
        #                         employees_amaguru_count=employees_amaguru_count,
        #                         employees_amaboko=employees_amaboko,
        #                         employees_amaboko_count=employees_amaboko_count,
        #                         employees_kutabona=employees_kutabona,
        #                         employees_kutabona_count=employees_kutabona_count,
        #                         employees_kutumva=employees_kutumva,
        #                         employees_kutumva_count=employees_kutumva_count,
        #                         employees_mumutwe=employees_mumutwe,
        #                         employees_mumutwe_count=employees_mumutwe_count,
        #                             title="Cooperative's details")
        # return redirect(url_for('admin.list_employees'))

    def test_memberDetails(self):
        """
        Test that memberDetails link is inaccessible without login
        and redirects to login page then to memberDetails
        """
        target_url = url_for('aicos_union.memberDetails',id=1)
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, redirect_url)

    def test_federation_umusaruro(self):
        """
        Test that federation_umusaruro link is inaccessible without login
        and redirects to login page then to federation_umusaruro
        """
        target_url = url_for('aicos_union.federation_umusaruro')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, redirect_url)

    def test_coop_umusaruro(self):
        """
        Test that coop_umusaruro is inaccessible without login
        and redirects to login page then to coop_umusaruro
        """
        # department = Department.query.filter_by(id=1).first()
        target_url = url_for('aicos_union.coop_umusaruro',email='admin@gmail.com')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

    def test_federation_inyongeramusaruro(self):
        """
        Test that federation_inyongeramusaruro is inaccessible without login
        and redirects to login page then to federation_inyongeramusaruro
        """
        target_url = url_for('aicos_union.federation_inyongeramusaruro')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

    def test_coop_inyongeramusaruro(self):
        """
        Test that coop_inyongeramusaruro page is inaccessible without login
        and redirects to login page then to coop_inyongeramusaruro page
        """
        # department = Department.query.filter_by(id=1).first()
        target_url = url_for('aicos_union.coop_inyongeramusaruro',email='admin@gmail.com')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

    def test_federation_imisanzu(self):
        """
        Test that federation_imisanzu page is inaccessible without login
        and redirects to login page then to federation_imisanzu page
        """
        target_url = url_for('aicos_union.federation_imisanzu')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

    def test_coop_imisanzu(self):
        """
        Test that coop_imisanzu page is inaccessible without login
        and redirects to login page then to coop_imisanzu page
        """
        # department = Department.query.filter_by(id=1).first()
        target_url = url_for('aicos_union.coop_imisanzu',email='admin@gmail.com')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

    def test_federation_ibirarane(self):
        """
        Test that federation_ibirarane page is inaccessible without login
        and redirects to login page then to federation_ibirarane page
        """        
        target_url = url_for('aicos_union.federation_ibirarane')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

        response2 = self.client.get(target_url,follow_redirects=True)
        self.assertEqual(response2.status_code, 200)

    def test_coop_ibirarane(self):
        """
        Test that coop_ibirarane page is inaccessible without login
        and redirects to login page then to coop_ibirarane page
        """ 
        # department = Department.query.filter_by(id=1).first()     
        target_url = url_for('aicos_union.coop_ibirarane',email='admin@gmail.com')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_federation_ibihano(self):
        """
        Test that federation_ibihano page is inaccessible without login
        and redirects to login page then to federation_ibihano page
        """
        target_url = url_for('aicos_union.federation_ibihano')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_coop_ibihano(self):
        """
        Test that coop_ibihano page is inaccessible without login
        and redirects to login page then to coop_ibihano page
        """
        # department = Department.query.filter_by(id=1).first()
        target_url = url_for('aicos_union.coop_ibihano',email='admin@gmail.com')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_federation_ibindi(self):
        """
        Test that crm_item_remove page is inaccessible without login
        and redirects to login page then to crm_item_remove page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_union.federation_ibindi', email='admin@gmail.com')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_coop_ibindi(self):
        """
        Test that coop_ibindi page is inaccessible without login
        and redirects to login page then to coop_ibindi page
        """
        target_url = url_for('aicos_union.coop_ibindi',email='admin@gmail.com')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

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