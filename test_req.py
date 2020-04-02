# import os
import sys
import unittest

from flask_testing import TestCase
from app import create_app, db
 
from app.models import *

from datetime import datetime
import datetime
from flask import Flask, abort, url_for
from flask_login import current_user,login_user,login_manager

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

        application = Application(emailaa='emailaa',firstNameaa='firstNameaa',secondNameaa='secondNameaa',
                      othersaa='othersaa',Districtaa='Districtaa',Sectoraa='Sectoraa',
                      Cellaa='Cellaa',nIdaa='nIdaa',entryDateaa='entryDateaa',shareaa='shareaa',
                      exitDateaa='exitDateaa',umuzunguraaa='umuzunguraaa',umukonoaa='umukonoaa',genderaa='genderaa',
                      dobaa='dobaa',phoneaa='phoneaa',Amashuriaa='Amashuriaa',Ubumugaaa='Ubumugaaa')

        member = Member(sno=11001)

        inama = inamaUbuyobozi(status='status',decision='decision',owner = 'owner',
                stakeholders='stakeholders',due_date='due_date',background = 'background')

        notif = Notification(action="Made decision",done_time = "frank",
                            done_to="tapayi",effect = "system upgraded")

        inamaUbugenzuzi = Ubugenzuzi(status='status',decision='decision',owner = 'owner',
                        stakeholders='stakeholders',due_date='due_date',
                        background = 'background')

        isanduku = Isanduku(no=6788,done_date='done_date',action='action',
                        income   = 300000,expense   = 200000,
                        remain   = 100000,done_by   = 'done_by',
                        done_to   = 'done_to')

        umusaruro = Umusaruro(umusaruro=11000)

        inteko = intekoRusange(status1='ibyizweho',decision1='decision1',owner1='owner1',
                            stakeholders1='stakeholders1',due_date1='due_date1',
                            background1 = 'background1')

        ibitabo = ibitaboByaBank(no = 3000,date = 'Date',igikorwa = 'Igikorwa',debit= 200000,
                        credit = 40000,solde = 6000)

        itsinda = Itsinda(itsinda_name = 'name',description = 'description',
                        purpose = 'purpose')

        rukomatanyo = Rukomatanyo(description = 'description',piyesi = 'piyesi')
        inguzanyo_zatanzwe = InguzanyoZatanzwe(ayinjiye = 10000,ayasohotse = 4000,asigaye = 6000)
        ibicuruzwa = Ibicuruzwa(ayinjiye = 10000,ayasohotse = 4000,asigaye = 6000)
        ikoreshwa = IkoreshwaRyimari(ayinjiye = 10000,ayasohotse = 4000,asigaye = 6000)
        isanduku = IsandukuNshya(ayinjiye = 10000,ayasohotse = 4000,asigaye = 6000)
        bank = BankModel(ayinjiye = 10000,ayasohotse = 4000,asigaye = 6000)
        ibiramba = Ibiramba(ayinjiye = 10000,ayasohotse = 4000,asigaye = 6000)
        ububiko = Ububiko(ayinjiye = 10000,ayasohotse = 4000,asigaye = 6000)
        umugabane = UmugabaneShingiro(ayinjiye = 10000,ayasohotse = 4000,asigaye = 6000)
        inkunga = Inkunga(ayinjiye = 10000,ayasohotse = 4000,asigaye = 6000)
        inguzanyo_abandi = InguzanyoZabandi(ayinjiye = 10000,ayasohotse = 4000,asigaye = 6000)
        ibindi_rukomatanyi = IbindiRukomatanyi(ayinjiye = 10000,ayasohotse = 4000,asigaye = 6000)

        ubwisazurex = UbwisazureEnter(
                                    AssetDescription = 'AssetDescriptionx',
                                    cost = 2099,YearOfPurchase = 'YearOfPurchasex',
                                    SalvageValue = 5778,UsefulLife = 677,Method = 'Methodx')

        db.session.add(admin)

        db.session.add(coop_admin)
        db.session.add(overall)
        db.session.add(accountant)

        db.session.add(application)
        db.session.add(member)
        db.session.add(inama)

        db.session.add(notif)
        db.session.add(inamaUbugenzuzi)
        db.session.add(isanduku)
        db.session.add(umusaruro)
        db.session.add(inteko)

        db.session.add(ibitabo)
        db.session.add(itsinda)
        db.session.add(rukomatanyo)
        db.session.add(inguzanyo_zatanzwe)
        db.session.add(ibicuruzwa)

        db.session.add(ikoreshwa)
        db.session.add(isanduku)
        db.session.add(bank)
        db.session.add(ibiramba)
        db.session.add(ububiko)

        db.session.add(umugabane)
        db.session.add(inkunga)
        db.session.add(inguzanyo_abandi)
        db.session.add(ibindi_rukomatanyi)
        db.session.add(ubwisazurex)


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
        Test number of records in models
        """
        self.assertEqual(Employee.query.count(), 4)
        self.assertEqual(Application.query.count(), 1)
        self.assertEqual(Member.query.count(), 1)
        self.assertEqual(inamaUbuyobozi.query.count(), 1)

        self.assertEqual(Notification.query.count(), 1)
        self.assertEqual(Ubugenzuzi.query.count(), 1)
        self.assertEqual(IsandukuNshya.query.count(), 1)
        self.assertEqual(Umusaruro.query.count(), 1)
        self.assertEqual(intekoRusange.query.count(), 1)

        self.assertEqual(ibitaboByaBank.query.count(), 1)
        self.assertEqual(Itsinda.query.count(), 1)
        self.assertEqual(Rukomatanyo.query.count(), 1)
        self.assertEqual(InguzanyoZatanzwe.query.count(), 1)
        self.assertEqual(Ibicuruzwa.query.count(), 1)

        self.assertEqual(IkoreshwaRyimari.query.count(), 1)
        self.assertEqual(IsandukuNshya.query.count(), 1)
        self.assertEqual(BankModel.query.count(), 1)
        self.assertEqual(Ibiramba.query.count(), 1)
        self.assertEqual(Ububiko.query.count(), 1)

        self.assertEqual(UmugabaneShingiro.query.count(), 1)
        self.assertEqual(Inkunga.query.count(), 1)
        self.assertEqual(InguzanyoZabandi.query.count(), 1)
        self.assertEqual(IbindiRukomatanyi.query.count(), 1)
        self.assertEqual(UbwisazureEnter.query.count(), 1)


class TestViews(TestBase):
    def test_intekoRusangeAdd(self):

        #check_admin()
        # form = intekoRusangeForm()
        # if validate_on_submit():
        #     inteko = intekoRusange(
        #                     status1=ibyizweho,
        #                     decision1=decision1,
        #                     owner1   = owner1,
        #                     stakeholders1=stakeholders1,
        #                     due_date1=due_date1,
        #                     background1 = background1,
        #                     department_id = current_user.email
        #                     )

        #     try:
        #         db.session.add(inteko)
        #         #db.session.add(notif)
        #         db.session.commit()
        #         flash("Umaze kubika neza ibyemezo by'inama")
        #     except:
        #         flash("Habayeho ikibazo mu makuru watanze!")
            #return redirect(url_for('aicos_req.intekoRusangeList'))
            target_url = url_for('aicos_req.intekoRusangeAdd')
            redirect_url = url_for('aicos_req.intekoRusangeList')
            with self.client:
                response = self.client.get(target_url)
                self.assertEqual(response.status_code, 200)
        #return render_template("governanceBooks/intekoRusange.html", form=form, title="Create")


    def test_inamaUbuyoboziAdd(self):


        # check_admin()
        # form = inamaUbuyoboziForm()
        # if validate_on_submit():
        #     inama = inamaUbuyobozi(status=status,
        #                     decision=decision,
        #                     owner   = owner,
        #                     stakeholders=stakeholders,
        #                     due_date=due_date,
        #                     background = background,
        #                     department_id = current_user.email)

        #     notif = Notification(action="Made decision",
        #                         done_by=current_user.username,
        #                         done_from=IP,
        #                         done_time = "frank",
        #                         done_to="tapayi",
        #                         effect = "system upgraded",
        #                         department_id = current_user.email)
        #     try:
        #         db.session.add(inama)
        #         db.session.add(notif)
        #         db.session.commit()
        #         flash("Umaze kubika neza ibyemezo by'inama")
        #     except:
        #         flash("Habayeho ikibazo mu makuru watanze!")
            target_url = url_for('aicos_req.inamaUbuyoboziAdd')
            redirect_url = url_for('aicos_req.inamaUbuyoboziList')
            with self.client:
                response = self.client.get(target_url)
                self.assertEqual(response.status_code, 200)
            #return redirect(url_for('aicos_req.inamaUbuyoboziList'))
        #return render_template("governanceBooks/inamaUbuyobozi.html", form=form, title="Create")

    def test_ubugenzuziAdd(self,*args, **kwargs):
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        

        # check_admin()
        # form = ubugenzuziForm()
        # if validate_on_submit():
        #     inamaUbugenzuzi = Ubugenzuzi(status=status,
        #                     decision=decision,
        #                     owner   = owner,
        #                     stakeholders=stakeholders,
        #                     due_date=due_date,
        #                     background = background,
        #                     department_id = current_user.email)

        #     notif = Notification(action="Made decision",
        #                         done_by=current_user.username,
        #                         done_from=IP,
        #                         done_time = "frank",
        #                         done_to="tapayi",
        #                         effect = "system upgraded",
        #                         department_id = current_user.email)
        #     try:
        #         db.session.add(inamaUbugenzuzi)
        #         db.session.add(notif)
        #         db.session.commit()
        #         flash("Umaze kubika neza ibyemezo by'inama")
        #     except:
        #         flash("Habayeho ikibazo mu makuru watanze!")
        target_url = url_for('aicos_req.ubugenzuziAdd')
        redirect_url = url_for('aicos_req.ubugenzuziList')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
            #return redirect(url_for('aicos_req.ubugenzuziList'))
        #return render_template("governanceBooks/ubugenzuzi.html", form=form, title="Create")




    # Views which are going to be dealing with Accounting Book.
    def test_abanyamuryangoImigabane(self):
        target_url = url_for('aicos_req.abanyamuryangoImigabane')
        redirect_url = url_for('aicos_req.abanyamuryangoImigabane')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_abanyamuryangoDetails(self):
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        
        target_url = url_for('aicos_req.abanyamuryangoDetails',id=1)
        redirect_url = url_for('aicos_req.abanyamuryangoImigabane')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_edit_umugabane(self):
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        
        target_url = url_for('aicos_req.edit_umugabane',id=1)
        redirect_url = url_for('aicos_req.abanyamuryangoImigabane')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

        # """
        # Edit a role
        # """
        # check_admin()
        # #add_role = False
        # member = Member.query.get_or_404(id)
        # form = MemberForm(obj=member)
        # if validate_on_submit():
        #     member.firstName = firstName
        #     member.nId = nId
        #     db.session.add(member)
        #     db.session.commit()
        #     flash('Umaze kongera umugabane.')
        #     # redirect to the roles pagess
            #return redirect(url_for('aicos_req.abanyamuryangoImigabane'))
        # firstName = member.firstName
        # nId = member.nId
        #return render_template('accountingBooks/imigabane/addUmugabane.html', form=form, title="Edit Umugabane")








    # Isanguku views are here.
    def test_isandukuList(self):
        target_url = url_for('aicos_req.isandukuList')
        redirect_url = url_for('aicos_req.isandukuList')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
    #     isanduku = Isanduku()
        #return render_template("accountingBooks/isanduku/isandukuList.html", isanduku=isanduku, title="List y'ibyemezo by'inteko rusange")



    # @aicos_req.route('/cooperative/add/Isanduku', methods=['GET', 'POST'])
    # @login_required
    def test_isandukuAdd(self):
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        

        # check_admin()
        # form = isandukuForm()
        # if validate_on_submit():
        #     isanduku = Isanduku(

        #                     no=no,
        #                     done_date=done_date,
        #                     action=action,
        #                     income   = income,
        #                     expense   = expense,
        #                     remain   = remain,
        #                     done_by   = done_by,
        #                     done_to   = done_to,
        #                     department_id = current_user.email
        #                     )

        #     notif = Notification(action="Communication",
        #                         done_by=current_user.username,
        #                         done_from=IP,
        #                         done_time = "frank",
        #                         done_to="tapayi",
        #                         effect = "system upgraded",
        #                         department_id = current_user.email)
        #     try:
        #         """
        #         to_number = '+250786012383'
        #         message = current_user.email + ' Decision has made and you are concerned'
        #         response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
        #         response_text = response['messages'][0]
        #         """

        #         db.session.add(isanduku)
        #         db.session.add(notif)
        #         db.session.commit()
        #         flash("Wongereye amakuru mu isanduku neza")
        #     except:
        #         flash("Error! Invalid information")
        target_url = url_for('aicos_req.isandukuAdd')
        redirect_url = url_for('aicos_req.isandukuList')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
        #return redirect(url_for('aicos_req.isandukuList'))
        #return render_template("accountingBooks/isanduku/isanduku.html", form=form, title="Kongera mu Isanduku.")





    # Umusaruro views are here.
    def test_umusaruroList(self):
        target_url = url_for('aicos_req.umusaruroList')
        redirect_url = url_for('aicos_req.umusaruroList')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
    #     umusaruro = Umusaruro.query
        #return render_template("accountingBooks/umusaruro/umusaruroList.html", umusaruro=umusaruro, title="List y'umusaruro winjiye")



    # @aicos_req.route('/cooperative/add/Umusaruro', methods=['GET', 'POST'])
    # @login_required
    def test_umusaruroAdd(self):
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        
        
        # form = umusaruroForm()
        # if validate_on_submit():
        #     umusaruro = Umusaruro(
        #                     Amazina=Amazina,
        #                     Taliki=Taliki,
        #                     Uwagemuye=Uwagemuye,
        #                     Ibiro   = Ibiro,
        #                     Igiciro   = Igiciro,
        #                     IkiguziCyose   = IkiguziCyose,
        #                     amafarangaYishyuweKuKiro   = amafarangaYishyuweKuKiro,
        #                     done_by   = done_by,
        #                     done_to   = done_to,
        #                     department_id = current_user.email
        #                     )



        #     notif = Notification(action="Communication",
        #                         done_by=current_user.username,
        #                         done_from=IP,
        #                         done_time = "frank",
        #                         done_to="tapayi",
        #                         effect = "system upgraded",
        #                         department_id = current_user.email)
        #     try:
        #         """
        #         to_number = '+250786012383'
        #         message = current_user.email + ' Decision has made and you are concerned'
        #         response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
        #         response_text = response['messages'][0]
        #         """

        #         db.session.add(umusaruro)
        #         db.session.add(notif)
        #         db.session.commit()
        #         flash("Winjije neza umusaruro muri Cooperative")
        #     except:
        #         flash("Error! Invalid information")
        target_url = url_for('aicos_req.umusaruroAdd')
        redirect_url = url_for('aicos_req.umusaruroList')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
        #return redirect(url_for('aicos_req.umusaruroList'))
        #return render_template("accountingBooks/umusaruro/umusaruro.html", form=form, title="Kongera umusaruro muri Cooperative.")








    # Views for the Wide Cooperative Market.
    def test_wcmIndex(self):
        target_url = url_for('aicos_req.wcmIndex')
        redirect_url = url_for('aicos_req.wcmIndex')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
    #     umusaruro = Umusaruro.query
        #return render_template('accountingBooks/wcm/index.html', umusaruro=umusaruro)

    def test_abishyuye(self):
        target_url = url_for('aicos_req.abishyuye')
        redirect_url = url_for('aicos_req.abishyuye')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_bankIbitabo(self):
        target_url = url_for('aicos_req.bankIbitabo')
        redirect_url = url_for('aicos_req.bankIbitabo')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_ibitaboBank(self):
    #     form = ibitaboBankForm()
    #     if validate_on_submit():
    #         ibitabo = ibitaboBank(
    #                                 no = No,
    #                                 date = Date,
    #                                 igikorwa = Igikorwa,
    #                                 debt     = Debit,
    #                                 credit   = Credit,
    #                                 solde    = Solde,
    #                                 department_id = current_user.email)
    #         try:
    #             db.session.add(ibitabo)
    #             db.session.commit()
        target_url = url_for('aicos_req.ibitaboBank')
        redirect_url = url_for('aicos_req.ibitaboBankList')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
    #             flash("Umaze kwinjize igitabo cya bank neza!")
                #return redirect(url_for('aicos_req.ibitaboBankList'))
    #         except:
    #             flash("Ntago igitabo cyabashije kwinjira neza!")
        #return render_template('accountingBooks/ibitaboBank/ibitaboBank.html', form=form, title="List y'ibitabo bya banks!")


    def test_bankHistory(self):
        target_url = url_for('aicos_req.bankHistory')
        redirect_url = url_for('aicos_req.bankHistory')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_signatories(self):
        target_url = url_for('aicos_req.signatories')
        redirect_url = url_for('aicos_req.signatories')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_amatsinda(self):
        target_url = url_for('aicos_req.amatsinda')
        redirect_url = url_for('aicos_req.amatsinda')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_koraItsinda(self):

    #     form = amatsindaForm()

    #     if validate_on_submit():

    #         itsinda = Itsinda(
    #                             itsinda_name = name,
    #                             description = description,
    #                             purpose = purpose,
    #                             department_id = current_user.email
    #                             )

    #         try:
    #             db.session.add(itsinda)
    #             db.session.commit()
        target_url = url_for('aicos_req.koraItsinda')
        redirect_url = url_for('aicos_req.amatsinda')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
    #             flash("Umaze kwandika neza itsinda")
                #return redirect(url_for('aicos_req.amatsinda'))
    #         except:
    #             flash("ntabwo itsinda ryanditse neza ongera ugerageze")
                #return redirect(url_for('aicos_req.koraItsinda'))

        #return render_template('/amatsinda/koraItsinda.html', form=form)


    def test_amatsindaMembers(self):
        target_url = url_for('aicos_req.amatsindaMembers',id=1)
        # redirect_url = url_for('aicos_req.amatsindaMembers')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
    #     itsinda = Itsinda.query.get_or_404(id)
    #     itsindaName = Itsinda(id=itsinda.id).first()
    #     members = Member.query
    #     itsindamember = ItsindaMember(itsinda_id=itsinda.id)
        #return render_template('/amatsinda/all_itsinda_members.html', members=members, itsindaName=itsindaName, itsindamember=itsindamember)



    def test_add_members(self):
        target_url = url_for('aicos_req.add_members',id=1)
        # redirect_url = url_for('aicos_req.add_members')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
    #     itsinda = Itsinda.query.get_or_404(id)
    #     itsindaName = Itsinda(id=itsinda.id).first()
    #     members = Member.query
    #     itsindamember = ItsindaMember.query
        #return render_template('/amatsinda/add_itsinda_members.html', members=members, itsindaName=itsindaName, itsindamember=itsindamember)

    def test_ongeramo_member(self):
    #     memberId = Member.query.get_or_404(a)
    #     itsindaId = Itsinda.query.get_or_404(b)
    #     itsindaName = Itsinda(id=itsindaId.id).first()
    #     member = Member(id=memberId.id).first()
    #     members = Member.query
    #     itsinda = Itsinda(id=itsindaId.id).first()

    #     itsindamember = ItsindaMember(
    #                                 member_id=member.id,
    #                                 itsinda_id=itsinda.id,
    #                                 member_firstname=member.izina_ribanza,
    #                                 member_secondname=member.izina_rikurikira,
    #                                 itsinda_name=itsinda.itsinda_name,
    #                                 
    #                                 )
    #     try:
    #         db.session.add(itsindamember)
    #         db.session.commit()
        target_url = url_for('aicos_req.ongeramo_member')
        redirect_url = url_for('aicos_req.add_members')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
    #         flash("Umunyamuryango yinjiye neza mwitsinda " + "\"" + itsindaName.itsinda_name + "\"")
            #return redirect(url_for('aicos_req.add_members', id=itsinda.id))
    #     except:
    #         db.session.rollback()
    #         flash("Umunyamuryango asanzwe arimo")
            #return render_template('/amatsinda/add_itsinda_members.html', members=members, itsindaName=itsindaName)
        #return render_template('/amatsinda/add_itsinda_members.html', members=members, itsindaName=itsindaName)
        


    def test_rukomatanyi(self):
        target_url = url_for('aicos_req.rukomatanyi')
        redirect_url = url_for('aicos_req.rukomatanyi')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_isanduku(self):
        target_url = url_for('aicos_req.isanduku')
        redirect_url = url_for('aicos_req.isanduku')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_hinduraIsanduku(self):
    #     isanduku_id = IsandukuNshya.query.get_or_404(id)
    #     ibihinduka = IsandukuNshya(id=isanduku_id.id).first()
    #     form = IsandukuForm()
    #     if validate_on_submit():
    #         ibihinduka.ayinjiye = ayinjiye
    #         ibihinduka.ayasohotse = ayasohotse
    #         try:
    #             db.session.commit()
        target_url = url_for('aicos_req.hinduraIsanduku',id=1)
        redirect_url = url_for('aicos_req.isanduku')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                #return redirect(url_for('aicos_req.isanduku'))
    #         except:
                #return redirect(url_for('aicos_req.hinduraIsanduku'))
    #     ayinjiye.default = ibihinduka.ayinjiye
    #     ayasohotse.default = ibihinduka.ayasohotse
    #     process()
        #return render_template('accountingBooks/rukomatanyi/rukomatanyi_form/hindura_isanduku.html', form=form)


    def test_bank(self):
        target_url = url_for('aicos_req.bank')
        redirect_url = url_for('aicos_req.bank')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_hinduraBank(self):
    #     bankId = BankModel.query.get_or_404(id)
    #     bank = BankModel(id=bankId.id).first()
    #     form = BankForm()
    #     if validate_on_submit():
    #         bank.ayinjiye = ayinjiye
    #         bank.ayasohotse = ayasohotse
    #         try:
    #             db.session.commit()
        target_url = url_for('aicos_req.hinduraBank',id=1)
        redirect_url = url_for('aicos_req.bank')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                #return redirect(url_for('aicos_req.bank'))
    #         except:
                # #return redirect(url_for('aicos_req.hinduraBank', form=form))
    #     ayinjiye.default = bank.ayinjiye
    #     ayasohotse.default = bank.ayasohotse
    #     process()
        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_bank.html', form=form)


    def test_inguzanyo_zatanzwe(self):
        target_url = url_for('aicos_req.inguzanyo_zatanzwe')
        redirect_url = url_for('aicos_req.inguzanyo_zatanzwe')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
    #     inguzanyo_zatanzwe = InguzanyoZatanzwe()
    #     rukomatanyo = Rukomatanyo.query
        #return render_template('/accountingBooks/rukomatanyi/inguzanyo_zatanzwe.html', inguzanyo_zatanzwe=inguzanyo_zatanzwe, rukomatanyo=rukomatanyo)

    def test_hinduraInguzanyoZatanzwe(self):
    #     inguzanyoId = InguzanyoZatanzwe.query.get_or_404(id)
    #     inguzanyo = InguzanyoZatanzwe(id=inguzanyoId.id).first()
    #     form = InguzanyoZatanzweForm()
    #     if validate_on_submit():
    #         inguzanyo.ayinjiye = ayinjiye
    #         inguzanyo.ayasohotse = ayasohotse
    #         try:
    #             db.session.commit()
        target_url = url_for('aicos_req.hinduraInguzanyoZatanzwe',id=1)
        redirect_url = url_for('aicos_req.inguzanyo_zatanzwe')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.inguzanyo_zatanzwe'))
    #         except:
                # #return redirect(url_for('aicos_req.hinduraInguzanyoZatanzwe', form=form))
    #     ayinjiye.default = inguzanyo.ayinjiye
    #     ayasohotse.default = inguzanyo.ayasohotse
    #     process()
        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_inguzanyo_zatanzwe.html', form=form)


    def test_ibiramba(self):
        target_url = url_for('aicos_req.ibiramba')
        redirect_url = url_for('aicos_req.ibiramba')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_hinduraIbiramba(self):
    #     ibirambaId = Ibiramba.query.get_or_404(id)
    #     ibiramba = Ibiramba(id=ibirambaId.id).first()
    #     form = IbirambaForm()
    #     if validate_on_submit():
    #         ibiramba.ayinjiye = ayinjiye
    #         ibiramba.ayasohotse = ayasohotse
    #         try:
    #             db.session.commit()
        target_url = url_for('aicos_req.hinduraIbiramba',id=1)
        redirect_url = url_for('aicos_req.ibiramba')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.ibiramba'))
    #         except:
                # #return redirect(url_for('aicos_req.hinduraIbiramba'))
    #     ayinjiye.default = ibiramba.ayinjiye
    #     ayasohotse.default = ibiramba.ayasohotse
    #     process()
        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ibaramba.html', form=form)


    def test_ububiko(self):
        target_url = url_for('aicos_req.ububiko')
        redirect_url = url_for('aicos_req.ububiko')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_hinduraUbubiko(self):
    #     ububikoId = Ububiko.query.get_or_404(id)
    #     ububiko = Ububiko(id=ububikoId.id).first()
    #     form = UbubikoForm()
    #     if validate_on_submit():
    #         ububiko.ayinjiye = ayinjiye
    #         ububiko.ayasohotse = ayasohotse
    #         try:
    #             db.session.commit()
        target_url = url_for('aicos_req.hinduraUbubiko',id=1)
        redirect_url = url_for('aicos_req.ububiko')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.ububiko'))
    #         except:
                # #return redirect(url_for('aicos_req.hinduraUbubiko', form=form))
    #     ayinjiye.default = ububiko.ayinjiye
    #     ayasohotse.default = ububiko.ayasohotse
    #     process()
        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ububiko.html', form=form)

    def test_umugabane_shingiro(self):
        target_url = url_for('aicos_req.umugabane_shingiro')
        redirect_url = url_for('aicos_req.umugabane_shingiro')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_hinduraUmugabaneShingiro(self):
    #     umugabaneId = UmugabaneShingiro.query.get_or_404(id)
    #     umugabane = UmugabaneShingiro(id=umugabaneId.id).first()
    #     form = UmugabaneShingiroForm()
    #     if validate_on_submit():
    #         umugabane.ayinjiye = ayinjiye
    #         umugabane.ayasohotse = ayasohotse
    #         try:
    #             db.session.commit()
        target_url = url_for('aicos_req.hinduraUmugabaneShingiro',id=1)
        redirect_url = url_for('aicos_req.umugabane_shingiro')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.umugabane_shingiro'))
    #         except:
                # #return redirect(url_for('aicos_req.hinduraUmugabaneShingiro', form=form))
    #     ayinjiye.default = umugabane.ayinjiye
    #     ayasohotse.default = umugabane.ayasohotse
    #     process()
        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_umugabane_shingiro.html', form=form)

    def test_inkunga(self):
        target_url = url_for('aicos_req.inkunga')
        redirect_url = url_for('aicos_req.inkunga')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_hindura_inkunga(self):
    #     inkungaId = Inkunga.query.get_or_404(id)
    #     inkunga = Inkunga(id=inkungaId.id).first()
    #     form = InkungaForm()
    #     if validate_on_submit():
    #         inkunga.ayinjiye = ayinjiye
    #         inkunga.ayasohotse = ayasohotse
    #         try:
    #             db.session.commit()
        target_url = url_for('aicos_req.hindura_inkunga',id=1)
        redirect_url = url_for('aicos_req.inkunga')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.inkunga'))
    #         except:
                # #return redirect(url_for('aicos_req.hindura_inkunga', form=form))
    #     ayinjiye.default = inkunga.ayinjiye
    #     ayasohotse.default = inkunga.ayasohotse
    #     process()
        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_inkunga.html', form=form)

    def test_inguzanyo_abandi(self):
        target_url = url_for('aicos_req.inguzanyo_abandi')
        redirect_url = url_for('aicos_req.inguzanyo_abandi')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_hinduraInguzanyoZabandi(self):
    #     inguzanyoId = InguzanyoZabandi.query.get_or_404(id)
    #     inguzanyo = InguzanyoZabandi(id=inguzanyoId.id).first()
    #     form = InguzanyoZabandiForm()
    #     if validate_on_submit():
    #         inguzanyo.ayinjiye = ayinjiye
    #         inguzanyo.ayasohotse = ayasohotse
    #         try:
    #             db.session.commit()
        target_url = url_for('aicos_req.hinduraInguzanyoZabandi',id=1)
        redirect_url = url_for('aicos_req.inguzanyo_abandi')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.inguzanyo_abandi'))
    #         except:
                # redirect(url_for('aicos_req.hinduraInguzanyoZabandi', form=form))
    #     ayinjiye.default = inguzanyo.ayinjiye
    #     ayasohotse.default = inguzanyo.ayasohotse
    #     process()
        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_inguzanyo_zabandi.html', form=form)



    def test_ibicuruzwa(self):
        target_url = url_for('aicos_req.ibicuruzwa')
        redirect_url = url_for('aicos_req.ibicuruzwa')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_hindura_ibicuruzwa(self):
    #     ibicuruzwaId = Ibicuruzwa.query.get_or_404(id)
    #     ibicuruzwa = Ibicuruzwa(id=ibicuruzwaId.id).first()
    #     form = IbicuruzwaForm()

    #     if validate_on_submit():
    #         ibicuruzwa.ayinjiye = ayinjiye
    #         ibicuruzwa.ayasohotse = ayasohotse
    #         try:
    #             db.session.commit()
        target_url = url_for('aicos_req.hindura_ibicuruzwa',id=1)
        redirect_url = url_for('aicos_req.ibicuruzwa')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.ibicuruzwa'))
    #         except:
                # #return redirect(url_for('aicos_req.hindura_ibicuruzwa', form=form))
    #     ayinjiye.default = ibicuruzwa.ayinjiye
    #     ayasohotse.default = ibicuruzwa.ayasohotse
    #     process()
        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ibicuruzwa.html', form=form)


    def test_ikoreshwa_ryimari(self):
        target_url = url_for('aicos_req.ikoreshwa_ryimari')
        redirect_url = url_for('aicos_req.ikoreshwa_ryimari')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_hinduraIkoreshwaRyimari(self):
    #     ikoreshwaId = IkoreshwaRyimari.query.get_or_404(id)
    #     ikoreshwa = IkoreshwaRyimari(id=ikoreshwaId.id).first()
    #     form = IkoreshwaRyimariForm()

    #     if validate_on_submit():
    #         ikoreshwa.ayinjiye = ayinjiye
    #         ikoreshwa.ayasohotse = ayasohotse
    #         try:
    #             db.session.commit()
        target_url = url_for('aicos_req.hinduraIkoreshwaRyimari',id=1)
        redirect_url = url_for('aicos_req.ikoreshwa_ryimari')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.ikoreshwa_ryimari'))
    #         except:
                # #return redirect(url_for('aicos_req.hinduraIkoreshwaRyimari', form=form))
    #     ayinjiye.default = ikoreshwa.ayinjiye
    #     ayasohotse.default = ikoreshwa.ayasohotse
    #     process()
        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ikoreshwa_ryimari.html', form=form)

    def test_ibindi_rukomatanyi(self):
        target_url = url_for('aicos_req.ibindi_rukomatanyi')
        redirect_url = url_for('aicos_req.ibindi_rukomatanyi')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)

    def test_hindura_ibindi(self):
    #     ibindiId= IbindiRukomatanyi.query.get_or_404(id)
    #     ibindi = IbindiRukomatanyi(id=ibindiId.id).first()
    #     form = IbindiForm()

    #     if validate_on_submit():
    #         ibindi.ayinjiye = ayinjiye
    #         ibindi.ayasohotse = ayasohotse
    #         try:
    #             db.session.commit()
        target_url = url_for('aicos_req.hindura_ibindi',id=1)
        redirect_url = url_for('aicos_req.ibindi_rukomatanyi')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.ibindi_rukomatanyi'))
    #         except:
                # #return redirect(url_for('aicos_req.hindura_ibindi', form=form))
    #     ayinjiye.default = ibindi.ayinjiye
    #     ayasohotse.default = ibindi.ayasohotse
    #     process()
        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ibindi.html', form=form)


    def test_injiza_isanduku(self):
    #     form = IsandukuForm()

    #     if validate_on_submit():
    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = itariki,
    #                             description = impamvu,
    #                             piyesi = piyesi
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
                # #return redirect(url_for('aicos_req.injiza_isanduku'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
                # #return redirect(url_for('aicos_req.injiza_isanduku'))

    #         isanduku = IsandukuNshya(
    #                             ayinjiye = ayinjiye,
    #                             ayasohotse = ayasohotse,
    #                             asigaye = asigaye,
    #                             department_id = current_user.email,
    #                             rukomatanyo_id = rukomatanyo_id.id
    #                             )

    #         try:
    #             db.session.add(isanduku)
    #             db.session.commit()
        target_url = url_for('aicos_req.injiza_isanduku')
        redirect_url = url_for('aicos_req.isanduku')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.isanduku'))
    #         except:
                # #return redirect(url_for('aicos_req.injiza_isanduku', form=form))
        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_isanduku.html', form=form)


    def test_injizaBank(self):
    #     form = BankForm()

    #     if validate_on_submit():
    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = itariki,
    #                             description = impamvu,
    #                             piyesi = piyesi
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
                # #return redirect(url_for('aicos_req.injizaBank'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
                # #return redirect(url_for('aicos_req.injizaBank'))

    #         bank = BankModel(
    #                         ayinjiye = ayinjiye,
    #                         ayasohotse = ayasohotse,
    #                         department_id = current_user.email,
    #                         rukomatanyo_id=rukomatanyo_id.id
    #                         )

    #         try:
    #             db.session.add(bank)
    #             db.session.commit()
        target_url = url_for('aicos_req.injizaBank')
        redirect_url = url_for('aicos_req.bank')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.bank'))
    #         except:
                # #return redirect(url_for('aicos_req.injizaBank', form=form))
        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_bank.html', form=form)

    def test_InjizaIzatanzwe(self):
    #     form = InguzanyoZatanzweForm()

    #     if validate_on_submit():

    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = itariki,
    #                             description = impamvu,
    #                             piyesi = piyesi,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
                # #return redirect(url_for('aicos_req.InjizaIzatanzwe'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
                # #return redirect(url_for('aicos_req.InjizaIzatanzwe'))

    #         inguzanyo = InguzanyoZatanzwe(
    #                                     ayinjiye = ayinjiye,
    #                                     ayasohotse = ayasohotse,
    #                                     department_id = current_user.email,
    #                                     rukomatanyo_id = rukomatanyo_id.id
    #                                     )
    #         try:
    #             db.session.add(inguzanyo)
    #             db.session.commit()
        target_url = url_for('aicos_req.InjizaIzatanzwe')
        redirect_url = url_for('aicos_req.inguzanyo_zatanzwe')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.inguzanyo_zatanzwe'))
    #         except:
                # #return redirect(url_for('aicos_req.InjizaIzatanzwe', form=form))
        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/InjizaIzatanzwe.html', form=form)


    def test_record_ibiramba(self):
    #     form = IbirambaForm()

    #     if validate_on_submit():

    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = itariki,
    #                             description = impamvu,
    #                             piyesi = piyesi,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
                # #return redirect(url_for('aicos_req.record_ibiramba'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
                # #return redirect(url_for('aicos_req.record_ibiramba'))

    #         iramba = Ibiramba(
    #                         ayinjiye = ayinjiye,
    #                         ayasohotse = ayasohotse,
    #                         department_id = current_user.email,
    #                         rukomatanyo_id = rukomatanyo_id.id
    #                         )
    #         try:
    #             db.session.add(iramba)
    #             db.session.commit()
        target_url = url_for('aicos_req.record_ibiramba')
        redirect_url = url_for('aicos_req.ibiramba')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.ibiramba'))
    #         except:
                # #return redirect(url_for('aicos_req.record_ibiramba', form=form))

        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ibiramba.html', form=form)

    def test_record_ububiko(self):
    #     form = UbubikoForm()

    #     if validate_on_submit():

    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = itariki,
    #                             description = impamvu,
    #                             piyesi = piyesi,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
                # #return redirect(url_for('aicos_req.record_ububiko'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
                # #return redirect(url_for('aicos_req.record_ububiko'))

    #         ububiko = Ububiko(
    #                         ayinjiye = ayinjiye,
    #                         ayasohotse = ayasohotse,
    #                         department_id = current_user.email,
    #                         rukomatanyo_id = rukomatanyo_id.id
    #                         )

    #         try:
    #             db.session.add(ububiko)
    #             db.session.commit()
        target_url = url_for('aicos_req.record_ububiko')
        redirect_url = url_for('aicos_req.ububiko')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.ububiko'))
    #         except:
                # #return redirect(url_for('aicos_req.record_ububiko', form=form))

        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ububiko.html', form=form)


    def test_record_umugabane_shingiro(self):
    #     form = UmugabaneShingiroForm()

    #     if validate_on_submit():

    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = itariki,
    #                             description = impamvu,
    #                             piyesi = piyesi,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
                # #return redirect(url_for('aicos_req.record_umugabane_shingiro'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
                # #return redirect(url_for('aicos_req.record_umugabane_shingiro'))

    #         umugabane = UmugabaneShingiro(
    #                                 ayinjiye = ayinjiye,
    #                                 ayasohotse = ayasohotse,
    #                                 department_id = current_user.email,
    #                                 rukomatanyo_id = rukomatanyo_id.id
    #                                 )
    #         try:
    #             db.session.add(umugabane)
    #             db.session.commit()
        target_url = url_for('aicos_req.record_umugabane_shingiro')
        redirect_url = url_for('aicos_req.umugabane_shingiro')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.umugabane_shingiro'))
    #         except:
                # #return redirect(url_for('aicos_req.record_umugabane_shingiro', form=form))

        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_umugabane_shingiro.html', form=form)


    def test_record_inkunga(self):
    #     form = InkungaForm()

    #     if validate_on_submit():

    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = itariki,
    #                             description = impamvu,
    #                             piyesi = piyesi,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
                # #return redirect(url_for('aicos_req.record_inkunga'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
                # #return redirect(url_for('aicos_req.record_inkunga'))

    #         inkunga = Inkunga(
    #                         ayinjiye = ayinjiye,
    #                         ayasohotse = ayasohotse,
    #                         department_id = current_user.email,
    #                         rukomatanyo_id = rukomatanyo_id.id
    #                         )
    #         try:
    #             db.session.add(inkunga)
    #             db.session.commit()
        target_url = url_for('aicos_req.record_inkunga')
        redirect_url = url_for('aicos_req.inkunga')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.inkunga'))
    #         except:
                # #return redirect(url_for('aicos_req.record_inkunga'))

        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_inkunga.html', form=form)


    def test_record_inguzanyo_abandi(self):
    #     form = InguzanyoZabandiForm()

    #     if validate_on_submit():

    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = itariki,
    #                             description = impamvu,
    #                             piyesi = piyesi,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
                # #return redirect(url_for('aicos_req.record_inkunga'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
                # #return redirect(url_for('aicos_req.record_inkunga'))

    #         inguzanyo = InguzanyoZabandi(
    #                                 ayinjiye = ayinjiye,
    #                                 ayasohotse = ayasohotse,
    #                                 department_id = current_user.email,
    #                                 rukomatanyo_id = rukomatanyo_id.id 
    #                                 )
    #         try:
    #             db.session.add(inguzanyo)
    #             db.session.commit()
        target_url = url_for('aicos_req.record_inguzanyo_abandi')
        redirect_url = url_for('aicos_req.inguzanyo_abandi')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.inguzanyo_abandi'))
    #         except:
                # #return redirect(url_for('aicos_req.record_inguzanyo_abandi'))

        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_inguzanyo_abandi.html', form=form)

    def test_record_ibicuruzwa(self):
    #     form = IbicuruzwaForm()

    #     if validate_on_submit():


            
    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = itariki,
    #                             description = impamvu,
    #                             piyesi = piyesi,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
                # #return redirect(url_for('aicos_req.record_ibicuruzwa'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
                # #return redirect(url_for('aicos_req.record_ibicuruzwa'))

    #         ibicuruzwa = Ibicuruzwa(
    #                                 ayinjiye = ayinjiye,
    #                                 ayasohotse = ayasohotse,
    #                                 department_id = current_user.email,
    #                                 rukomatanyo_id = rukomatanyo_id.id
    #                                 )
    #         try:
    #             db.session.add(ibicuruzwa)
    #             db.session.commit()
        target_url = url_for('aicos_req.record_ibicuruzwa')
        redirect_url = url_for('aicos_req.ibicuruzwa')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.ibicuruzwa'))
    #         except:
                # #return redirect(url_for('aicos_req.record_ibicuruzwa', form=form))

        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ibicuruzwa.html', form=form)


    def test_record_ikoreshwa_ryimari(self):
    #     form = IkoreshwaRyimariForm()

    #     if validate_on_submit():


    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = itariki,
    #                             description = impamvu,
    #                             piyesi = piyesi,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
                # #return redirect(url_for('aicos_req.record_ikoreshwa_ryimari'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
                # #return redirect(url_for('aicos_req.record_ikoreshwa_ryimari'))

    #         ikoreshwa = IkoreshwaRyimari(
    #                                     ayinjiye = ayinjiye,
    #                                     ayasohotse = ayasohotse,
    #                                     department_id = current_user.email,
    #                                     rukomatanyo_id = rukomatanyo_id.id 
    #                                     )
    #         try:
    #             db.session.add(ikoreshwa)
    #             db.session.commit()
        target_url = url_for('aicos_req.record_ikoreshwa_ryimari')
        redirect_url = url_for('aicos_req.ikoreshwa_ryimari')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.ikoreshwa_ryimari'))
    #         except:
                # #return redirect(url_for('aicos_req.record_ikoreshwa_ryimari'))

        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ikoreshwa_ryimari.html', form=form)
            


    def test_record_ibindi(self):
    #     form = IbindiForm()

    #     if validate_on_submit():


    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = itariki,
    #                             description = impamvu,
    #                             piyesi = piyesi,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
                # #return redirect(url_for('aicos_req.record_ibindi'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
                # #return redirect(url_for('aicos_req.record_ibindi'))

    #         ibindi = IbindiRukomatanyi(
    #                                 ayinjiye = ayinjiye,
    #                                 ayasohotse = ayasohotse,
    #                                 department_id = current_user.email,
    #                                 rukomatanyo_id = rukomatanyo_id.id 
    #                                 )
    #         try:
    #             db.session.add(ibindi)
    #             db.session.commit()
        target_url = url_for('aicos_req.record_ibindi')
        redirect_url = url_for('aicos_req.ibindi_rukomatanyi')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
                # #return redirect(url_for('aicos_req.ibindi_rukomatanyi'))
    #         except:
                # #return redirect(url_for('aicos_req.record_ibindi'))

        #return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ibindi.html', form=form)

    def test_UbwisazureList(self):
    #     ubwisazurexx = UbwisazureEnter.query
        #return render_template('accountingBooks/ubwisazure/ubwisazure_list.html',
    #                             ubwisazurexx=ubwisazurexx, title='Ubwisazure ku mutungo wa cooperative!!')
    # ibitabo bya banks.
    # def UbwisazureBwose():
    #     form = UbwisazureForm()
    #     if validate_on_submit():
    #         ubwisazurex = UbwisazureEnter(
    #                                 AssetDescription = AssetDescriptionx,
    #                                 cost = costx,
    #                                 YearOfPurchase = YearOfPurchasex,
    #                                 SalvageValue = SalvageValuex,
    #                                 UsefulLife = UsefulLifex,
    #                                 Method = Methodx,
    #                                 department_id = current_user.email
    #                                 )

    #         try:
    #             db.session.add(ubwisazurex)
    #             db.session.commit()
    #             flash("Umaze kwinjize umutungo neza!")
        target_url = url_for('aicos_req.UbwisazureList')
        # redirect_url = url_for('aicos_req.UbwisanzureList')
        with self.client:
            response = self.client.get(target_url)
            self.assertEqual(response.status_code, 200)
    #         except:
    #             flash("Ntago umutungo wabashije kwinjira neza!")
        #return render_template('accountingBooks/ubwisazure/ubwisazure_html', form=form, title="List y'ubwisazure bw'umutungo!")


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