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

        
        # create test department
        department = Department(email='department@gmail.com', name="IT", description="The IT Department")

        member = Member(sno='sno',izina_ribanza='izina_ribanza',izina_rikurikira='izina_rikurikira')#,
                    #   Ayandi ='Ayandi',zone ='zone',itsinda='itsinda',Igitsina='Igitsina',
                    #   Indangamuntu='Indangamuntu',tariki_yavukiye='tariki_yavukiye',Intara='Intara',
                    #   Akarere='Akarere',Umurenge='Umurenge',Akagari='Akagari',Umudugudu='Umudugudu',
                    #   tariki_yinjiriye='tariki_yinjiriye',umugabane_ukwezi='umugabane_ukwezi',Umukono='Umukono',
                    #   nomero_telephone='nomero_telephone',Amashuri='Amashuri',Ubumuga='Ubumuga',
                    #   Arubatse='Arubatse',umubare_abana='umubare_abana',icyiciro_ubudehe='icyiciro_ubudehe',
                    #   Ubwishingizi='Ubwishingizi',akazi_akora_muri_koperative='akazi_akora_muri_koperative',
                    #   akazi_akora_ahandi='akazi_akora_ahandi',ubuso_ahingaho='ubuso_ahingaho',
                    #   ubwoko_igihingwa='ubwoko_igihingwa',ubuso_ahingaho_ibindi='ubuso_ahingaho_ibindi',
                    #   ubwoko_igihingwa_kindi='ubwoko_igihingwa_kindi',ubuso_budakoreshwa='ubuso_budakoreshwa')

        amazina = member.izina_ribanza + " " + member.izina_rikurikira

        umusaruro = Umusaruro(amazina= amazina,resi = 1234,
                            zone = 'zone',umusaruro = 1000,
                            umuceriWoKurya = 500,igiciroCyaKimwe = 1000,
                            amafarangaYoGutonoza = 100 * int(umuceriWoKurya),
                            umusanzu = 2000 * int(umusaruro),member= member,
                            department = department,umwakaWisarura = 'umwakaWisarura',
                            umuceriWoKugurisha = int(umusaruro) - int(umuceriWoKurya),
                            amafarangaYose = (int(umusaruro) - int(umuceriWoKurya)) * int(igiciroCyaKimwe))

        inyongeramusaruro = Inyongeramusaruro(amazina = amazina,umusaruro_resi= 2000,
                            BriqueteUnity= float(395),BriquetePU= int(235),
                            DapAndNPKUnity= float(455),DapAndNPKpu= int(609),
                            KCLUnity= float(234),KCLpu= int(789),
                            ImbutoIngano= float(285),ImbutoPU= int(890),
                            RedevanceUbuso= float(558),RedevancePU= int(465),
                            ImifukaAgaciro= 2000000,ImifukaYishyuwe= int(1500000),
                            umwakaWisarura = 'umwakaWisarura',department=department)

        ibyakoreshejwe = Ibyakoreshejwe(umusaruro_resi= 1234,deamAndSup= 1000000,
                            ibihanoCoop= 50000,APKSAMAKIbihano= 30000,
                            ibiraraneNPKandUREA= 100000,umusoroWakarere= 40000,
                            kwishyuraItsinda= 70000,sheeting= 40000,
                            PandS= 20000,ibyoYagurijwe= 1000000,
                            ibindiYasbwe= 200000,department= department)

        coopMemberBankAccounts = CoopMemberBankAccounts(umusaruro_resi= 1234,
                            memberName= 'Kalima',
                            bankName= 'Equity',
                            bankAccountNumber= '44411177700072',
                            department=department
                            )


        # save models instances to database
        db.session.add(admin)
        db.session.add(member)
        db.session.add(employee)
        db.session.add(umusaruro)
        db.session.add(department)
        db.session.add(ibyakoreshejwe)
        db.session.add(inyongeramusaruro)
        db.session.add(coopMemberBankAccounts)

        db.session.commit()

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

    # def test_stock():
        # check_admin()
        # check_coop_admin()
        # employee = Department.query.filter_by(email=current_user.email).first()
        # employees = employee.members
        # all_member_idd = Umusaruro.member_id
        
        # umusaruro_resi = Umusaruro.query.filter_by(department_id=current_user.email).all()
        # inyongera = Inyongeramusaruro.query.filter_by(department_id=current_user.email).all()
        # ibyakoze = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
        # member_all = Employee.query.filter_by(department_id=current_user.email).all()

        # return render_template('stock_manage.html', umusaruro_resi=umusaruro_resi, member_all=member_all, employees=employees, inyongera=inyongera)

    # def test_umusaruro():
        # check_admin()
        # check_coop_admin()
        # employee = Department.query.filter_by(email=current_user.email).first()
        # employees = employee.members
        # all_member_idd = Umusaruro.member_id
        
        # umusaruro_resi = Umusaruro.query.filter_by(department_id=current_user.email).all()
        # member_all = Employee.query.filter_by(department_id=current_user.email).all()

        # return render_template('umusaruro.html', umusaruro_resi=umusaruro_resi, member_all=member_all, employees=employees)
        
    def test_inyongeramusaruro(self):
        """
        Test that inyongeramusaruro link is inaccessible without login
        and redirects to login page then to inyongeramusaruro
        """
        target_url = url_for('aicos_stock_managment.inyongeramusaruro')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

        # check_admin()
        # check_coop_admin()
        # employee = Department.query.filter_by(email=current_user.email).first()
        # employees = employee.members
        # inyongera = Inyongeramusaruro.query.filter_by(department_id=current_user.email).all()
        # return render_template('inyongeramusaruro.html', inyongera=inyongera, employees=employees)

    def test_ibyakoreshejwe(self):
        """
        Test that ibyakoreshejwe link is inaccessible without login
        and redirects to login page then to ibyakoreshejwe
        """
        target_url = url_for('aicos_stock_managment.ibyakoreshejwe')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

        # check_admin()
        # check_coop_admin()
        # employee = Department.query.filter_by(email=current_user.email).first()
        # employees = employee.members
        # ibyakoreshejwe = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
        # return render_template('ibyakoreshejwe.html', ibyakoreshejwe=ibyakoreshejwe, employees=employees)

    # def test_injizaUmusaruro(self):
    #     """
    #     Test that injizaUmusaruro link is inaccessible without login
    #     and redirects to login page then to injizaUmusaruro
    #     """
    #     target_url = url_for('aicos_stock_managment.injizaUmusaruro'id=1)
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, redirect_url)

        # check_admin()
        # memberid = Member.query.get_or_404(id)
        # member_name = Member.query.filter_by(id=memberid.id).first()


        # if memberid is None:
        #     return redirect(url_for('aicos_stock_managment.umusaruro'))
        # form = UmusaruroForm()


        # if form.validate_on_submit():
        #     amazina = member_name.izina_ribanza + " " + member_name.izina_rikurikira



        #     umusaruro = Umusaruro(
        #                         amazina= amazina,
        #                         resi = int(form.resi.data),
        #                         zone = form.zone.data,
        #                         umusaruro = int(form.umusaruro.data),
        #                         umuceriWoKurya = form.umuceriWoKurya.data,
        #                         igiciroCyaKimwe = int(form.igiciroCyaKimwe.data),
        #                         amafarangaYoGutonoza = int(form.amafrwYoGutonoza.data) * int(form.umuceriWoKurya.data),
        #                         umusanzu = int(form.umusanzu.data) * int(form.umusaruro.data),
        #                         member_id= member_name.id,
        #                         department_id = current_user.email,
        #                         umwakaWisarura = form.umwakaWisarura.data,
        #                         umuceriWoKugurisha = int(form.umusaruro.data) - int(form.umuceriWoKurya.data),
        #                         amafarangaYose = (int(form.umusaruro.data) - int(form.umuceriWoKurya.data)) * int(form.igiciroCyaKimwe.data)
        #                         )

        #     try:
        #         db.session.add(umusaruro)
        #         db.session.commit()
        #         flash("Umaze kwandika umusaruro wa" + member_name.izina_ribanza + " " + member_name.izina_rikurikira)
        #         return redirect(url_for('aicos_stock_managment.umusaruro'))
        #     except Exception:
        #         flash("Ntago amakuru watanze yashoboye kwakirwa neza!")
        #         return redirect(url_for('aicos_stock_managment.injizaUmusaruro', form=form, memberid=memberid, member_name=member_name))
        # return render_template('record_umusaruro.html', form=form, memberid=memberid, member_name=member_name)

    # def test_injizaInyongeramusaruro(self,id):
        # check_admin()
        # memberid = Member.query.get_or_404(id)
        # member_name = Member.query.filter_by(id=memberid.id).first()
        # inyongera = Inyongeramusaruro.query.filter_by(department_id=current_user.email).all()


        # if memberid is None:
        #     return redirect(url_for('aicos_stock_managment.umusaruro'))
        # form = InyongeramusaruroForm()
        # if form.validate_on_submit():

        #     amazina = member_name.izina_ribanza + " " + member_name.izina_rikurikira

        #     inyongeramusaruro = Inyongeramusaruro(
        #                                 amazina = amazina,
        #                                 umusaruro_resi= int(form.resi.data),
        #                                 BriqueteUnity= float(form.briquetteKg.data),
        #                                 BriquetePU= int(form.briquettePU.data),
        #                                 DapAndNPKUnity= float(form.DAPandNPKkg.data),
        #                                 DapAndNPKpu= int(form.DAPandNPKpu.data),
        #                                 KCLUnity= float(form.KCLkg.data),
        #                                 KCLpu= int(form.KCLpu.data),
        #                                 ImbutoIngano= float(form.ImbutoKg.data),
        #                                 ImbutoPU= int(form.ImbutoPU.data),
        #                                 RedevanceUbuso= float(form.redevenceUbuso.data),
        #                                 RedevancePU= int(form.redevencePU.data),
        #                                 ImifukaAgaciro= form.ImifukaKg.data,
        #                                 ImifukaYishyuwe= int(form.ImifukaPU.data),
        #                                 member_id = member_name.id,
        #                                 umwakaWisarura = form.umwakaWisarura.data,
        #                                 department_id=current_user.email
        #                                 )

        #     try:
        #         db.session.add(inyongeramusaruro)
        #         db.session.commit()
        #         flash("Umaze kwinjiza neza inyongeramusaruro!")
        #         return redirect(url_for('aicos_stock_managment.inyongeramusaruro'))
        #     except:
        #         flash("Resi Winjije nta musaruro wayo wabonetse!")
        #         return redirect(url_for('aicos_stock_managment.injizaInyongeramusaruro', form=form, id=memberid.id, memberid=memberid.id, member_name=member_name))

        # return render_template('/record_inyongeramusaruro.html', form=form, memberid=memberid, member_name=member_name)

    # def test_injizaIbyakoreshejwe(self):
        # check_admin()
        # check_coop_admin()
        # form = IbyakoreshejweForm()
        # if form.validate_on_submit():
        #     ibyakoreshejwe = Ibyakoreshejwe(
        #                             umusaruro_resi= form.resi.data,
        #                             deamAndSup= form.beamSup.data,
        #                             ibihanoCoop= form.ibihanoCoop.data,
        #                             APKSAMAKIbihano= form.APIISAMAKIbihano.data,
        #                             ibiraraneNPKandUREA= form.ibiraraneNPKandUREA.data,
        #                             umusoroWakarere= form.umusoro.data,
        #                             kwishyuraItsinda= form.kwishyuraItsinda.data,
        #                             sheeting= form.Sheeting.data,
        #                             PandS= form.PIS.data,
        #                             ibyoYagurijwe= form.umuceriYagurijweUmwakaKUshize.data,
        #                             ibindiYasbwe= form.ibindi.data,
        #                             department_id= current_user.email
        #                             )

        #     try:
        #         db.session.add(ibyakoreshejwe)
        #         db.session.commit()

        #         flash("Winjije neza ibyakoreshejwe uyu mwaka!")
        #         return redirect(url_for('aicos_stock_managment.ibyakoreshejwe'))
        #     except Exception:
        #         flash("Ibyo mumaze gukora Ntabwo byakunze neza Ongera ugerageze!")
        #         return redirect(url_for('aicos_stock_managment.injizaIbyakoreshejwe'))

        # return render_template('/record_ibyakoreshejwe.html', form=form)


    # def test_konteZaBanki(self):
        # check_admin
        # check_coop_admin()
        # konte = CoopMemberBankAccounts.query.filter_by(department_id=current_user.email).all()
        # return render_template("/bankiZacu.html", konte=konte)  

    # def test_injizaKonte(self):
        # check_admin()
        # form = KonteZaBankForm()
        # if form.validate_on_submit():
        #     coopMemberBankAccounts = CoopMemberBankAccounts(
        #                                 umusaruro_resi= form.resi.data,
        #                                 memberName= form.izinaryaNyiriKonte.data,
        #                                 bankName= form.izanaRyaBank.data,
        #                                 bankAccountNumber= form.numeroYaKonte.data,
        #                                 department_id=current_user.email
        #                                 )

        #     try:
        #         db.session.add(coopMemberBankAccounts)
        #         db.session.commit()
        #         flash("Winjije neza nimero ya banki")
        #         return redirect(url_for('aicos_stock_managment.konteZaBanki'))
        #     except Exception:
        #         flash("Ibyo wemeje ntabwo bimeze neza Ongera ugerageze!")
        #         return redirect(url_for('aicos_stock_managment.injizaKonte'))

        # return render_template("/record_bankAccount.html", form=form))



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