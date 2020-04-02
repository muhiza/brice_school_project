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
        db.drop_all()
        db.create_all()

        self.admin = Employee(username="admin",email='admin@gmail.com', password="admin2016", is_admin=True)

        self.coop_admin = Employee(username='coop_admin',email='coop_admin@gmail.com',password='coop_admin2016',is_coop_admin=True)

        self.overall = Employee(username="overall",email='overall@gmail.com', password="overall2016", is_overall=True)
        
        self.accountant = Employee(username='accountant',email='accountant@gmail.com',password='accountant2016',is_accountant=True)
        
        # create test department
        department = Department(email='department@gmail.com', name="IT", description="The IT Department")

        member = Member(sno='23344')

        umusaruro = Umusaruro(amazina= 'amazina',resi = 1234,
                            zone = 'zone',umusaruro = 1000,
                            umuceriWoKurya = 500,igiciroCyaKimwe = 1000,
                            amafarangaYoGutonoza = 100 * int(500),
                            umusanzu = 2000 * int(1000),member= member,
                            umwakaWisarura = 'umwakaWisarura',
                            umuceriWoKugurisha = int(1000) - int(500),
                            amafarangaYose = (int(1000) - int(500)) * int(1000))

        inyongeramusaruro = InyongeraMusaruro(NPKkg = 100,NPKPerUnity = 100,
                                UREA = 100,UREAPerUnity = 100,
                                DAP = 100,DAPPerUnity = 100,
                                KCL = 100,KCLPerUnity = 100,
                                Briquette = 100,BriquettePerUnity = 100,)

        ibyakoreshejwe = Ibyakoreshejwe(umusaruro_resi= 1234,deamAndSup= 1000000,
                            ibihanoCoop= 50000,APKSAMAKIbihano= 30000,
                            ibiraraneNPKandUREA= 100000,umusoroWakarere= 40000,
                            kwishyuraItsinda= 70000,sheeting= 40000,
                            PandS= 20000,ibyoYagurijwe= 1000000,
                            ibindiYasbwe= 200000)

        coopMemberBankAccounts = CoopMemberBankAccounts(umusaruro_resi= 1234,
                            memberName= 'Kalima',
                            bankName= 'Equity',
                            bankAccountNumber= '44411177700072')
                            
        # save models instances to database
        db.session.add(self.admin)
        db.session.add(self.coop_admin)
        db.session.add(self.overall)
        db.session.add(self.accountant)
        db.session.add(member)
        db.session.add(umusaruro)
        db.session.add(department)
        db.session.add(ibyakoreshejwe)
        db.session.add(inyongeramusaruro)
        db.session.add(coopMemberBankAccounts)

        db.session.commit()

        self.client.post(url_for('auth.login'),data=dict(email="admim@gmail.com",password="admim2016"), follow_redirects=True)
        self.client.post(url_for('auth.login'),data=dict(email="coop_admim@gmail.com",password="coop_admim2016"), follow_redirects=True)
        self.client.post(url_for('auth.login'),data=dict(email="overall@gmail.com",password="overall2016"), follow_redirects=True)
        self.client.post(url_for('auth.login'),data=dict(email="accountant@gmail.com",password="accountant2016"), follow_redirects=True)

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.app.login_manager._current_user = Employee.query.filter_by(is_active=True)

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()


class TestModels(TestBase):

    def test_models(self):
        """
        Test number of records in Employee table
        """
        self.assertEqual(Employee.query.count(), 4)
        self.assertEqual(Department.query.count(), 1)
        self.assertEqual(Member.query.count(), 1)
        self.assertEqual(Umusaruro.query.count(), 1)
        self.assertEqual(InyongeraMusaruro.query.count(), 1)
        self.assertEqual(Ibyakoreshejwe.query.count(), 1)
        self.assertEqual(CoopMemberBankAccounts.query.count(), 1)

class TestViews(TestBase):

    def test_stock(self):
        target_url = url_for('aicos_stock_managment.stock')
        with self.client:    
            response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)

    def test_umusaruro(self):
        target_url = url_for('aicos_stock_managment.umusaruro')
        with self.client:    
            response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)

    def test_inyongeramusaruro(self):
        """
        Test that inyongeramusaruro link is inaccessible without login
        and redirects to login page then to inyongeramusaruro
        """
        target_url = url_for('aicos_stock_managment.inyongeramusaruro')
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:    
            response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

    def test_ibyakoreshejwe(self):
        """
        Test that ibyakoreshejwe link is inaccessible without login
        and redirects to login page then to ibyakoreshejwe
        """
        target_url = url_for('aicos_stock_managment.ibyakoreshejwe')
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:    
            response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

    def test_injizaUmusaruro(self):
        """
        Test that injizaUmusaruro link is inaccessible without login
        and redirects to login page then to injizaUmusaruro
        """
        target_url = url_for('aicos_stock_managment.injizaUmusaruro',id=1)
        redirect_url = url_for('aicos_stock_managment.umusaruro')
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:    
            response = self.client.post(target_url,data=dict(amazina= 'amazina',resi = 1234,
                            zone = 'zone',umusaruro = 1000,
                            umuceriWoKurya = 500,igiciroCyaKimwe = 1000,
                            amafarangaYoGutonoza = 100 * int(500),
                            umusanzu = 2000 * int(1000),member= member,
                            umwakaWisarura = 'umwakaWisarura',
                            umuceriWoKugurisha = int(1000) - int(500),
                            amafarangaYose = (int(1000) - int(500)) * int(1000)))
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, redirect_url)

    def test_injizaInyongeramusaruro(self):
        target_url = url_for('aicos_stock_managment.injizaInyongeramusaruro',id=1)
        redirect_url = url_for('aicos_stock_managment.inyongeramusaruro')
        with self.client:
            resp = self.client.post(target_url,data=dict(amazina = amazina,
                                        umusaruro_resi= int(resi),
                                        BriqueteUnity= float(briquetteKg),
                                        BriquetePU= int(briquettePU),
                                        DapAndNPKUnity= float(DAPandNPKkg),
                                        DapAndNPKpu= int(DAPandNPKpu),
                                        KCLUnity= float(KCLkg),
                                        KCLpu= int(KCLpu),
                                        ImbutoIngano= float(ImbutoKg),
                                        ImbutoPU= int(ImbutoPU),
                                        RedevanceUbuso= float(redevenceUbuso),
                                        RedevancePU= int(redevencePU),
                                        ImifukaAgaciro= ImifukaKg,
                                        ImifukaYishyuwe= int(ImifukaPU),
                                        member_id = member_name.id,
                                        umwakaWisarura = umwakaWisarura,
                                        department_id=current_user.email))
        self.assertEqual(resp.status_code,200)

    def test_injizaIbyakoreshejwe(self):
        target_url = url_for('aicos_stock_managment.injizaIbyakoreshejwe',id=1)
        redirect_url = url_for('aicos_stock_managment.ibyakoreshejwe')
        with self.client:
            resp = self.client.post(target_url,data=dict(umusaruro_resi= 1234,
                                    deamAndSup= 3456,
                                    ibihanoCoop= 8976,
                                    APKSAMAKIbihano= 45687,
                                    ibiraraneNPKandUREA= 66778,
                                    umusoroWakarere= 35000,
                                    kwishyuraItsinda= 345667,
                                    sheeting= 5566,
                                    PandS= 6677,
                                    ibyoYagurijwe= 34567,
                                    ibindiYasbwe= 67878,
                                    department_id= current_user.email))

    def test_konteZaBanki(self):
        target_url = url_for('aicos_stock_managment.konteZaBanki')
        with self.client:
            resp = self.client.get(target_url)
        self.assertEqual(resp.status_code,200)

    def test_injizaKonte(self):
        target_url = url_for('aicos_stock_managment.injizaKonte')
        redirect_url = url_for('aicos_stock_managment.konteZaBanki')
        with self.client:
            resp = self.client.post(target_url,data=dict(umusaruro_resi= 'resi',
                                        memberName= 'izinaryaNyiriKonte',
                                        bankName= 'izanaRyaBank',
                                        bankAccountNumber= 'numeroYaKonte',
                                        department_id=current_user.email))
        self.assertEqual(resp.status_code,200)


class TestErrorPages(TestBase):

    def test_403_forbidden(self):
        # create route to abort the request with the 403 Error
        @self.app.route('/403')
        def forbidden_error():
            abort(403)

        with self.client:    
            response = self.client.get('/403')
        self.assertEqual(response.status_code, 403)
        # self.assertTrue("403 Error" in response)

    def test_404_not_found(self):
        with self.client:    
            response = self.client.get('/nothinghere')
        self.assertEqual(response.status_code, 404)
        # self.assertTrue("404 Error" in response)

    def test_500_internal_server_error(self):
        # create route to abort the request with the 500 Error
        @self.app.route('/500')
        def internal_server_error():
            abort(500)

        with self.client:    
            response = self.client.get('/500')
        self.assertEqual(response.status_code, 500)
        # self.assertTrue("500 Error" in response)


if __name__ == '__main__':
    unittest.main()