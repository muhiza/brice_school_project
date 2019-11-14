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


        employee = Department.query.filter_by(email=current_user.email).first()
        employees = employee.members
        #all_member_idd = Umusaruro.member_id
        memberss = Member.query.filter_by(department_id=current_user.email).all()
        umusaruro_resi = Umusarurob.query.filter_by(department_id=current_user.email).all()
        inyongeramusaruro = InyongeraMusaruro(
                                NPKkg = form.NPKkg.data,
                                NPKPerUnity = form.NPKPerUnity.data,
                                UREA = form.UREA.data,
                                UREAPerUnity = form.UREAPerUnity.data,
                                DAP = form.DAP.data,
                                DAPPerUnity = form.DAPPerUnity.data,
                                KCL = form.KCL.data,
                                KCLPerUnity = form.KCLPerUnity.data,
                                Briquette = form.Briquette.data,
                                BriquettePerUnity = form.BriquettePerUnity.data,
                                Cypemetrine = form.Cypemetrine.data,
                                Beam = form.Beam.data,
                                ImbutoQuantity = form.ImbutoQuantity.data,
                                ImbutoAmount = form.ImbutoAmount.data,
                                Redevance = form.Redevance.data,
                                member_id = memberid.id,
                                department_id = current_user.email
                                )
        #ibyakoze = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
        member_all = Employee.query.filter_by(department_id=current_user.email).all()
        ibirarane = Ibirarane.query.filter_by(department_id=current_user.email).all()
        imisanzu = Umusanzu.query.filter_by(department_id=current_user.email).all()
        umusaruro = Umusarurob(
                                RiceType = form.RiceType.data,
                                RiceAmount = int(form.RiceAmount.data) * form.Quantity.data,
                                UmusaruroGrade = form.UmusaruroGrade.data,
                                UwoAsigaranye = form.UwoAsigaranye.data,
                                UwoKugurisha = (form.Quantity.data) - (form.UwoAsigaranye.data),
                                GutonozaAmount = int(form.Gutonoza.data) * int(form.UwoAsigaranye.data),
                                AmafarangaUmusaruro1 =  (int(form.RiceAmount.data) * (int(form.Quantity.data) - \
                                                        int(form.UwoAsigaranye.data)) - (int(form.Gutonoza.data) * \
                                                        int(form.UwoAsigaranye.data))) - 10 * form.RiceAmount.data * form.Quantity.data / 100,
                                Asigaye     = 10 * form.RiceAmount.data * form.Quantity.data / 100,
                                member_id = memberid.id,
                                department_id = current_user.email
                             )

        umusaruro_resi = Umusaruro.query.filter_by(department_id=current_user.email).all()
        inyongera = InyongeraMusaruro.query.filter_by(department_id=current_user.email).all()
        #ibyakoze = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
        ibindi = Ibindi.query.all()
        ibihano = Ibihano.query.all()
        member_all = Employee.query.filter_by(department_id=current_user.email).all()
        ibirarane = Ibirarane.query.filter_by(department_id=current_user.email).all()
        imisanzu = Umusanzu.query.filter_by(department_id=current_user.email).all()
        umusaruro = Umusarurob.query.all()
        inyongeramusaruro = InyongeraMusaruro.query.all()

        ayishyurwa = Abishyuwe(
                amount_payed = 50000,
                member_id = member.id,
                member_name = member.izina_ribanza + " " + member.izina_rikurikira,
                ibiro = umusaruroId.UwoKugurisha,
                umusaruro_id = umusaruroId.id,
                department_id = current_user.email
                )

        ibyakoreshejwe = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
        imisanzu = Umusanzu.query.filter_by(department_id=current_user.email).all()



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
   
    def test_dashboard(self):
        """
        Test that dashboard page is inaccessible without login
        and redirects to login page then to dashboard page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = 'stock_dashboard.html'
        # redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_stock(self):
        """
        Test that stock page is inaccessible without login
        and redirects to login page then to stock page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = 'stock_manage.html'
        # redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    #     return render_template('stock_manage.html',ibihano=ibihano,
    #                                             imisanzu = imisanzu,
    #                                             ibirarane = ibirarane,
    #                                             ibindi=ibindi,
    #                                             umusaruro_resi=umusaruro_resi, 
    #                                             member_all=member_all, 
    #                                             employees=employees,
    #                                             umusaruro = umusaruro, 
    #                                             inyongera=inyongera,
    #                                             memberss=memberss,
    #                                             employee=employee,
    #                                             )


    def test_umusaruro(self):
        target_url = 'umusaruro.html'
        # redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)

    def test_ibindiUmusaruro(self):
        """
        Test that ibindiUmusaruro page is inaccessible without login
        and redirects to login page then to ibindiUmusaruro page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = 'ibindiUmusaruro.html'
        # redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_umunyamuryangoIshyura(self):
        """
        Test that umunyamuryangoIshyura page is inaccessible without login
        and redirects to login page then to umunyamuryangoIshyura page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = 'ishyuraByose.html'
        # redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_umusaruroIshyura(self):
        """
        Test that umusaruroIshyura page is inaccessible without login
        and redirects to login page then to umusaruroIshyura page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        # target_url = url_for('aicos_stock_managment.umusaruroIshyura',id=1)
        redirect_url = url_for('aicos_stock_managment.ibindiUmusaruro',id=1, next=target_url)
        response1 = self.client.get(redirect_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

        # ayishyurwa = Abishyuwe(
        #             amount_payed = 50000,
        #             member_id = member.id,
        #             member_name = member.izina_ribanza + " " + member.izina_rikurikira,
        #             ibiro = umusaruroId.UwoKugurisha,
        #             umusaruro_id = umusaruroId.id,
        #             department_id = current_user.email
        #             )

    def test_inyongeramusaruro(self):
        """
        Test that inyongeramusaruro page is inaccessible without login
        and redirects to login page then to inyongeramusaruro page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = 'inyongeramusaruro.html'
        # redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

        # check_admin()
        # check_coop_admin()
        # employee = Department.query.filter_by(email=current_user.email).first()
        # employees = employee.members
        # inyongera = InyongeraMusaruro.query.filter_by(department_id=current_user.email).all()
        # return render_template('inyongeramusaruro.html', inyongera=inyongera, employees=employees)


    def test_ibyakoreshejwe(self):
        """
        Test that ibyakoreshejwe page is inaccessible without login
        and redirects to login page then to ibyakoreshejwe page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = 'ibyakoreshejwe.html'
        # redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_imisanzu(self):
        """
        Test that imisanzu page is inaccessible without login
        and redirects to login page then to imisanzu page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = 'imisanzu.html'
        # redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_ibirarane(self):
        """
        Test that ibirarane page is inaccessible without login
        and redirects to login page then to ibirarane page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = 'ibirarane.html'
        # redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_ibihano(self):
        """
        Test that ibihano page is inaccessible without login
        and redirects to login page then to ibihano page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = 'ibihano.html'
        # redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def ibindi(self):
        """
        Test that ibindi page is inaccessible without login
        and redirects to login page then to ibindi page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = 'ibindi.html'
        # redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        # self.assertRedirects(response1, redirect_url)

    def test_injizaUmusaruro(self):
        """
        Test that injizaUmusaruro page is inaccessible without login
        and redirects to login page then to injizaUmusaruro page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = 'record_umusaruro.html'
        redirect_url = url_for('aicos_stock_managment.umusaruro',id=1, next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

        #     if form.UmusaruroGrade.data == 'good':
        #         umusaruro = Umusarurob(
        #                             RiceType = form.RiceType.data,
        #                             RiceAmount = int(form.RiceAmount.data) * form.Quantity.data,
        #                             UmusaruroGrade = form.UmusaruroGrade.data,
        #                             UwoAsigaranye = form.UwoAsigaranye.data,
        #                             UwoKugurisha = (form.Quantity.data) - (form.UwoAsigaranye.data),
        #                             GutonozaAmount = int(form.Gutonoza.data) * int(form.UwoAsigaranye.data),
        #                             AmafarangaUmusaruro1 =  (int(form.RiceAmount.data) * (int(form.Quantity.data) - \
        #                                                     int(form.UwoAsigaranye.data)) - (int(form.Gutonoza.data) * \
        #                                                     int(form.UwoAsigaranye.data))) + 10 * form.RiceAmount.data * form.Quantity.data / 100,
        #                             Asigaye     = 10 * form.RiceAmount.data * form.Quantity.data / 100,
        #                             member_id = memberid.id,
        #                             department_id = current_user.email
        #                         )


        #     elif form.UmusaruroGrade.data == 'normal':
        #         umusaruro = Umusarurob(
        #                             RiceType = form.RiceType.data,
        #                             RiceAmount = int(form.RiceAmount.data) * form.Quantity.data,
        #                             UmusaruroGrade = form.UmusaruroGrade.data,
        #                             UwoAsigaranye = form.UwoAsigaranye.data,
        #                             UwoKugurisha = (form.Quantity.data) - (form.UwoAsigaranye.data),
        #                             GutonozaAmount = int(form.Gutonoza.data) * int(form.UwoAsigaranye.data),
        #                             AmafarangaUmusaruro1 =  (int(form.RiceAmount.data) * (int(form.Quantity.data) - \
        #                                                     int(form.UwoAsigaranye.data)) - (int(form.Gutonoza.data) * \
        #                                                     int(form.UwoAsigaranye.data))) + 0,
        #                             Asigaye     = 0,
        #                             member_id = memberid.id,
        #                             department_id = current_user.email
        #                         )



        #     else:
        #         umusaruro = Umusarurob(
        #                             RiceType = form.RiceType.data,
        #                             RiceAmount = int(form.RiceAmount.data) * form.Quantity.data,
        #                             UmusaruroGrade = form.UmusaruroGrade.data,
        #                             UwoAsigaranye = form.UwoAsigaranye.data,
        #                             UwoKugurisha = (form.Quantity.data) - (form.UwoAsigaranye.data),
        #                             GutonozaAmount = int(form.Gutonoza.data) * int(form.UwoAsigaranye.data),
        #                             AmafarangaUmusaruro1 =  (int(form.RiceAmount.data) * (int(form.Quantity.data) - \
        #                                                     int(form.UwoAsigaranye.data)) - (int(form.Gutonoza.data) * \
        #                                                     int(form.UwoAsigaranye.data))) - 10 * form.RiceAmount.data * form.Quantity.data / 100,
        #                             Asigaye     = 10 * form.RiceAmount.data * form.Quantity.data / 100,
        #                             member_id = memberid.id,
        #                             department_id = current_user.email
        #                         )



        #     try:
        #         db.session.add(umusaruro)
        #         db.session.commit()
        #         flash(Markup("Umaze kwandika umusaruro wa " + "<b>" + member_name.izina_ribanza + " " + member_name.izina_rikurikira + "</b>"))
        #         return redirect(url_for('aicos_stock_managment.umusaruro'))
        #     except Exception:
        #         flash("Ntago amakuru watanze yashoboye kwakirwa neza!")
        #         return redirect(url_for('aicos_stock_managment.injizaUmusaruro', form=form, memberid=memberid, member_name=member_name, id=memberid.id))
        
        # return render_template('record_umusaruro.html', form=form, memberid=memberid, member_name=member_name)

    def test_injizaInyongeramusaruro(self):
        """
        Test that injizaInyongeramusaruro page is inaccessible without login
        and redirects to login page then to injizaInyongeramusaruro page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = '/record_inyongeramusaruro.html'
        redirect_url = url_for('aicos_stock_managment.inyongeramusaruro',id=1, next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(200, response1.status_code)
        self.assertRedirects(response1, redirect_url)

        #     inyongeramusaruro = InyongeraMusaruro(
        #                             NPKkg = form.NPKkg.data,
        #                             NPKPerUnity = form.NPKPerUnity.data,
        #                             UREA = form.UREA.data,
        #                             UREAPerUnity = form.UREAPerUnity.data,
        #                             DAP = form.DAP.data,
        #                             DAPPerUnity = form.DAPPerUnity.data,
        #                             KCL = form.KCL.data,
        #                             KCLPerUnity = form.KCLPerUnity.data,
        #                             Briquette = form.Briquette.data,
        #                             BriquettePerUnity = form.BriquettePerUnity.data,
        #                             Cypemetrine = form.Cypemetrine.data,
        #                             Beam = form.Beam.data,
        #                             ImbutoQuantity = form.ImbutoQuantity.data,
        #                             ImbutoAmount = form.ImbutoAmount.data,
        #                             Redevance = form.Redevance.data,
        #                             member_id = memberid.id,
        #                             department_id = current_user.email
        #                             )

    def test_injizaIbyakoreshejwe(self):
        target_url = '/record_ibyakoreshejwe.html'
        redirect_url = url_for('aicos_stock_managment.ibyakoreshejwe')
        response = self.client.post(target_url)
        self.assertEqual(200, response.status_code)
        self.assertRedirects(response, redirect_url)
        
        #     ibyakoreshejwe = Ibyakoreshejwe(
        #                             InyongeraMusaruroType = form.InyongeraMusaruroType.data,
        #                             Quantity = form.Quantity.data,
        #                             Amount = form.Amount.data,
        #                             Cypemetrine = form.Cypemetrine.data,
        #                             Beam = form.Beam.data,
        #                             ImbutoQuantity = form.ImbutoQuantity.data,
        #                             ImbutoAmount = form.ImbutoAmount.data,
        #                             Redevance = form.Redevance.data,
        #                             member_id = memberid.id,
        #                             department_id = current_user.email
        #                             )

    def test_konteZaBanki(self):
        target_url = '/bankiZacu.html'
        # redirect_url = url_for('aicos_stock_managment.imisanzu')
        response = self.client.post(target_url)
        self.assertEqual(200, response.status_code)
        # self.assertRedirects(response, redirect_url)

    def test_injizaKonte(self):
        target_url = '/record_bankAccount.html'
        redirect_url = url_for('aicos_stock_managment.konteZaBanki')
        response = self.client.post(target_url)
        self.assertEqual(200, response.status_code)
        self.assertRedirects(response, redirect_url)
                
    #         coopMemberBankAccounts = CoopMemberBankAccounts(
    #                                     memberName= form.izinaryaNyiriKonte.data,
    #                                     bankName= form.izanaRyaBank.data,
    #                                     bankAccountNumber= form.numeroYaKonte.data,
    #                                     department_id=current_user.email)

    def test_injizaImisanzu(self):
        target_url = '/record_imisanzu.html'
        redirect_url = url_for('aicos_stock_managment.imisanzu')
        response = self.client.post(target_url)
        self.assertEqual(200, response.status_code)
        self.assertRedirects(response, redirect_url)
        
    #         imisanzu = Umusanzu(
    #                             UmusoroWakarere = form.UmusoroWakarere.data,
    #                             UmusanzuCoop = form.UmusanzuCoop.data,
    #                             Umugabane = form.Umugabane.data,
    #                             Ikigega = form.Ikigega.data,
    #                             KuzibaIcyuho = form.KuzibaIcyuho.data,
    #                             member_id = memberid.id,
    #                             department_id = current_user.email
    #                     )

    def test_injizaIbirarane(self):
        target_url = '/record_ibirarane.html'
        redirect_url = url_for('aicos_stock_managment.ibirarane')
        response = self.client.post(target_url)
        self.assertEqual(200, response.status_code)
        self.assertRedirects(response, redirect_url)
        
    #         ibirarane = Ibirarane(
    #                             NPKkg = form.NPKkg.data,
    #                             NPKPerUnity = form.NPKPerUnity.data,
    #                             UREA = form.UREA.data,
    #                             UREAPerUnity = form.UREAPerUnity.data,
    #                             DAP = form.DAP.data,
    #                             DAPPerUnity = form.DAPPerUnity.data,
    #                             KCL = form.KCL.data,
    #                             KCLPerUnity = form.KCLPerUnity.data,
    #                             ImbutoQuantity = form.ImbutoQuantity.data,
    #                             ImbutoAmount = form.ImbutoAmount.data,
    #                             IdeniAmount = form.IdeniAmount.data,
    #                             Briquette = form.Briquette.data,
    #                             BriquettePerUnity = form.BriquettePerUnity.data,
    #                             member_id = memberid.id,
    #                             department_id = current_user.email
    #                         )

    def test_injizaIbihano(self):
        target_url = '/record_ibihano.html'
        redirect_url = url_for('aicos_stock_managment.ibihano')
        response = self.client.post(target_url)
        self.assertEqual(200, response.status_code)
        self.assertRedirects(response, redirect_url)
        
    #         ibihano = Ibihano(
    #                         AmandeC = form.AmandeC.data,
    #                         AmandeApII = form.AmandeApII.data,
    #                         comment = form.Comment.data,
    #                         member_id = memberid.id,
    #                         department_id = current_user.email
    #                     )


    def test_injizaIbindi(self):
        target_url = '/record_ibindi.html'
        redirect_url = url_for('aicos_stock_managment.ibindi')
        response = self.client.post(target_url)
        self.assertEqual(200, response.status_code)
        self.assertRedirects(response, redirect_url)


    #         ibindi = Ibindi(
    #                     ImifukaQuantity = form.ImifukaQuantity.data,
    #                     ImifukaAmount = int(form.ImifukaAmount.data) * int(form.ImifukaQuantity.data),
    #                     MituelleAmount = form.MituelleAmount.data,
    #                     UmuceriGrade   = form.UmuceriGrade.data,
    #                     UmuceriQuantity = form.UmuceriQuantity.data,
    #                     UmuceriAmountGrade = (form.UmuceriAmountGrade.data) * (form.UmuceriQuantity.data),
    #                     Avence = form.Avence.data,
    #                     member_id = memberid.id,
    #                     department_id = current_user.email
    #                     )

    def test_Imyishyurire(self):
        """
        Test that Imyishyurire page is inaccessible without login
        and redirects to login page then to Imyishyurire page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = 'imyishyurire.html'
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