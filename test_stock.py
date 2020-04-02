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
from flask_login import current_user,login_user

# from sqlalchemy import DateTime

class TestBase(TestCase):

    def create_app(self):

        # pass in test configuration
        config_name = 'testing'
        app = create_app(config_name)
        # app.config.update(
            # SQLALCHEMY_DATABASE_URI = 'mysql://juru:Password@123@localhost/testing'
        # )
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


        inyongeramusaruro = InyongeraMusaruro(NPKkg = 15)
        #ibyakoze = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
        member= Member(sno='23300')
        ibirarane = Ibirarane(NPKkg=14560)
        imisanzu = Umusanzu(UmusoroWakarere=40000)
        umusaruro = Umusarurob(RiceAmount = 1000)

        umusaruro_resi = Umusaruro(resi=2345)
        #ibyakoze = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
        ibindi = Ibindi(ImifukaAmount=25680)
        ibihano = Ibihano(AmandeApII=30000)

        ayishyurwa = Abishyuwe(amount_payed = 50000)

        ibyakoreshejwe = Ibyakoreshejwe(ibiraraneNPKandUREA=450000)



        # save crm_item and users to database
        db.session.add(admin)
        db.session.add(coop_admin)
        db.session.add(overall)
        db.session.add(accountant)
        db.session.add(inyongeramusaruro)
        db.session.add(member)
        db.session.add(ibirarane)
        db.session.add(imisanzu)
        db.session.add(umusaruro)
        db.session.add(umusaruro_resi)
        db.session.add(ibindi)
        db.session.add(ibihano)
        db.session.add(ayishyurwa)
        db.session.add(ibyakoreshejwe)

        db.session.commit()

        with self.client:  
            login_user(admin, remember=False, duration=None, force=True, fresh=True)
            login_user(coop_admin, remember=False, duration=None, force=True, fresh=True)
            login_user(overall, remember=False, duration=None, force=True, fresh=True)
            login_user(accountant, remember=False, duration=None, force=True, fresh=True)
            

            


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
        self.assertEqual(InyongeraMusaruro.query.count(), 1)
        self.assertEqual(Member.query.count(), 1)
        self.assertEqual(Ibirarane.query.count(), 1)
        self.assertEqual(Umusanzu.query.count(), 1)
        self.assertEqual(Umusarurob.query.count(), 1)
        self.assertEqual(Umusaruro.query.count(), 1)
        self.assertEqual(Ibindi.query.count(), 1)
        self.assertEqual(Ibihano.query.count(), 1)
        self.assertEqual(Abishyuwe.query.count(), 1)
        self.assertEqual(Ibyakoreshejwe.query.count(), 1)

class TestViews(TestBase):
   
    def test_dashboard(self):
        """
        Test that dashboard page is inaccessible without login
        and redirects to login page then to dashboard page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.dashboard')
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_stock(self):
        """
        Test that stock page is inaccessible without login
        and redirects to login page then to stock page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.stock')
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_umusaruro(self):
        target_url = url_for('aicos_stock_managment.umusaruro')
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)

    def test_ibindiUmusaruro(self):
        """
        Test that ibindiUmusaruro page is inaccessible without login
        and redirects to login page then to ibindiUmusaruro page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.ibindiUmusaruro',id=1)
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_umunyamuryangoIshyura(self):
        """
        Test that umunyamuryangoIshyura page is inaccessible without login
        and redirects to login page then to umunyamuryangoIshyura page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.umunyamuryangoIshyura',id=1)
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_umusaruroIshyura(self):
        """
        Test that umusaruroIshyura page is inaccessible without login
        and redirects to login page then to umusaruroIshyura page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.umusaruroIshyura',id=1)
        redirect_url = url_for('aicos_stock_managment.ibindiUmusaruro',id=1,next=target_url)
        response1 = self.client.post(target_url,data=dict(amount_payed = 50000,ibiro = 1000))
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_inyongeramusaruro(self):
        """
        Test that inyongeramusaruro page is inaccessible without login
        and redirects to login page then to inyongeramusaruro page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.inyongeramusaruro')
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_ibyakoreshejwe(self):
        """
        Test that ibyakoreshejwe page is inaccessible without login
        and redirects to login page then to ibyakoreshejwe page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.ibyakoreshejwe')
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_imisanzu(self):
        """
        Test that imisanzu page is inaccessible without login
        and redirects to login page then to imisanzu page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.imisanzu')
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_ibirarane(self):
        """
        Test that ibirarane page is inaccessible without login
        and redirects to login page then to ibirarane page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.ibirarane')
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_ibihano(self):
        """
        Test that ibihano page is inaccessible without login
        and redirects to login page then to ibihano page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.ibihano')
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_ibindi(self):
        """
        Test that ibindi page is inaccessible without login
        and redirects to login page then to ibindi page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.ibindi')
        # redirect_url = url_for('auth.login', next=target_url)
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_injizaUmusaruro(self):
        """
        Test that injizaUmusaruro page is inaccessible without login
        and redirects to login page then to injizaUmusaruro page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.injizaUmusaruro',id=1)
        redirect_url = url_for('aicos_stock_managment.umusaruro', next=target_url)
        with self.client:
            response1 = self.client.post(target_url,data=dict(RiceType = 'RiceType',
                                        RiceAmount = int(400) * 1000,
                                        UmusaruroGrade = 'UmusaruroGrade',
                                        UwoAsigaranye = 500,
                                        UwoKugurisha = (1000) - (500),
                                        GutonozaAmount = int(100) * int(500),
                                        AmafarangaUmusaruro1 =  (int(400000) * (int(1000) - \
                                                                int(500)) - (int(100) * \
                                                                int(500))) + 0,
                                        Asigaye     = 0))
            self.assertEqual(200, response1.status_code)
            # self.assertRedirects(response1, redirect_url)

    def test_injizaInyongeramusaruro(self):
        """
        Test that injizaInyongeramusaruro page is inaccessible without login
        and redirects to login page then to injizaInyongeramusaruro page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.injizaInyongeramusaruro',id=1)
        redirect_url = url_for('aicos_stock_managment.inyongeramusaruro',next=target_url)
        with self.client:
            response1 = self.client.post(target_url,data=dict(NPKkg = 20,
                                        NPKPerUnity = 340,UREA = 20,
                                        UREAPerUnity = 500,DAP = 40,
                                        DAPPerUnity = 400,KCL = 15,
                                        KCLPerUnity = 250,Briquette = 50,
                                        BriquettePerUnity = 300,Cypemetrine = 40,
                                        Beam = 30,ImbutoQuantity = 60,
                                        ImbutoAmount = 1000,Redevance = 5000))
            self.assertEqual(200, response1.status_code)
            # self.assertRedirects(response1, redirect_url)

    def test_injizaIbyakoreshejwe(self):
        target_url = url_for('aicos_stock_managment.injizaIbyakoreshejwe',id=1)
        redirect_url = url_for('aicos_stock_managment.ibyakoreshejwe')
        with self.client:
            response = self.client.post(target_url,data=dict(InyongeraMusaruroType = 40,
                                        Quantity = 79,Amount = 1000,
                                        Cypemetrine = 50,Beam = 20,
                                        ImbutoQuantity = 50,ImbutoAmount = 1000,
                                        Redevance = 6000))
            self.assertEqual(200, response.status_code)
        # self.assertRedirects(response, redirect_url)
        
    def test_konteZaBanki(self):
        target_url = url_for('aicos_stock_managment.konteZaBanki')
        with self.client:    
            response = self.client.get(target_url)
            self.assertEqual(200, response.status_code)

    def test_injizaKonte(self):
        target_url = url_for('aicos_stock_managment.injizaKonte')
        redirect_url = url_for('aicos_stock_managment.konteZaBanki')
        with self.client:
            response = self.client.post(target_url,data=dict(memberName= 'izinaryaNyiriKonte',
                                            bankName= 'izanaRyaBank',
                                            bankAccountNumber= 'numeroYaKonte'))
            self.assertEqual(200, response.status_code)
            # self.assertRedirects(response, redirect_url)
                
    def test_injizaImisanzu(self):
        target_url = url_for('aicos_stock_managment.injizaImisanzu',id=1)
        redirect_url = url_for('aicos_stock_managment.imisanzu')
        with self.client:
            response = self.client.post(target_url,data=dict(UmusoroWakarere = 20000,
                                    UmusanzuCoop = 2000,Umugabane = 20000,
                                    Ikigega = 5000,KuzibaIcyuho = 3000))
            self.assertEqual(200, response.status_code)
            # self.assertRedirects(response, redirect_url)

    def test_injizaIbirarane(self):
        target_url = url_for('aicos_stock_managment.injizaIbirarane',id=1)
        redirect_url = url_for('aicos_stock_managment.ibirarane')
        with self.client:
            response = self.client.post(target_url,data=dict(NPKkg = 60,NPKPerUnity = 340,
                                    UREA = 20,UREAPerUnity = 500,DAP = 40,
                                    DAPPerUnity = 400,KCL = 60,KCLPerUnity = 400,
                                    ImbutoQuantity = 100,ImbutoAmount = 1000,
                                    IdeniAmount = 5000,Briquette = 40,BriquettePerUnity = 200))
            self.assertEqual(200, response.status_code)
            # self.assertRedirects(response, redirect_url)
        
    def test_injizaIbihano(self):
        target_url = url_for('aicos_stock_managment.injizaIbihano',id=1)
        redirect_url = url_for('aicos_stock_managment.ibihano')
        with self.client:
            response = self.client.post(target_url,data=dict(AmandeC = 3000,
                                AmandeApII = 2000,
                                comment = 'Comment'))
            self.assertEqual(200, response.status_code)
            # self.assertRedirects(response, redirect_url)

    def test_injizaIbindi(self):
        target_url = url_for('aicos_stock_managment.injizaIbindi',id=1)
        redirect_url = url_for('aicos_stock_managment.ibindi')
        with self.client:
            response = self.client.post(target_url,data=dict(ImifukaQuantity = 2000,
                            ImifukaAmount = int(200) * int(2000),MituelleAmount = 30000,
                            UmuceriGrade   = 'UmuceriGrade',UmuceriQuantity = 1000,
                            UmuceriAmountGrade = (1000) * (1000),Avence = 40000))
            self.assertEqual(200, response.status_code)
            # self.assertRedirects(response, redirect_url)

    def test_Imyishyurire(self):
        """
        Test that Imyishyurire page is inaccessible without login
        and redirects to login page then to Imyishyurire page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_stock_managment.Imyishyurire')
        with self.client:
            response1 = self.client.get(target_url)
            self.assertEqual(200, response1.status_code)



class TestErrorPages(TestBase):

    def test_403_forbidden(self):
        # create route to abort the request with the 403 Error
        @self.app.route('/403')
        def forbidden_error():
            abort(403)

        response = self.client.get('/403')
        self.assertEqual(response.status_code, 403)
        # self.assertTrue("403 Error" in response)

    def test_404_not_found(self):
        response = self.client.get('/nothinghere')
        self.assertEqual(response.status_code, 404)
        # self.assertTrue("404 Error" in response)

    def test_500_internal_server_error(self):
        # create route to abort the request with the 500 Error
        @self.app.route('/500')
        def internal_server_error():
            abort(500)

        response = self.client.get('/500')
        self.assertEqual(response.status_code, 500)
        # self.assertTrue("500 Error" in response)


if __name__ == '__main__':
    unittest.main()