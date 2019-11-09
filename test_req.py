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

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home.homepage'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        """
        Test that login page is accessible without login
        """
        response = self.client.get(url_for('auth.login'))
        self.assertEqual(response.status_code, 200)

    def test_login_fn(self):
        employee = Employee(first_name='Joe', email='joe@joes.com', password='12345')
        with self.client:
            response = self.client.post(url_for('auth.login',{'email': 'joe@joes.com', 'password': '12345'}))

            self.assertTrue(employee.is_authenticated)
            self.assertTrue(employee.is_active)
            self.assertFalse(employee.is_anonymous)
            self.assertEqual(employee.id, int(response.get_id()))

    def test_logout_view_redirects(self):
        """
        Test that logout link is inaccessible without login
        and redirects to login page then to logout
        """
        target_url = url_for('auth.logout')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_logout_view(self):
        """
        Test that logout works as expected
        """
        Employee(first_name="Joe", email="joe@joes.com", password="12345")
        with self.client:
            target_url = url_for("auth.login",data={Employee:{"email": "joe@joes.com","password": "12345"}})
            self.client.post(target_url)
            self.assertTrue(current_user.first_name == 'Joe')
            self.assertFalse(current_user.is_anonymous())

            self.client.get(url_for("auth.logout"))
            self.assertTrue(current_user.is_anonymous())

    def test_dashboard_view(self):
        """
        Test that dashboard is inaccessible without login
        and redirects to login page then to dashboard
        """
        target_url = url_for('home.dashboard')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_admin_dashboard_view(self):
        """
        Test that dashboard is inaccessible without login
        and redirects to login page then to dashboard
        """
        target_url = url_for('home.admin_dashboard')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    # def test_departments_view(self):
    #     """
    #     Test that departments page is inaccessible without login
    #     and redirects to login page then to departments page
    #     """
    #     target_url = url_for('admin.list_departments')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, redirect_url)

    def test_roles_view(self):
        """
        Test that roles page is inaccessible without login
        and redirects to login page then to roles page
        """
        target_url = url_for('aicos_members.list_roles')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_employees_view(self):
        """
        Test that employees page is inaccessible without login
        and redirects to login page then to employees page
        """
        target_url = url_for('aicos_members.list_employees')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)





    def test_CRM_items_table_view(self):
        """
        Test that crm_items_table page is inaccessible without login
        and redirects to login page then to crm_items_table page
        """        
        target_url = url_for('aicos_crm.table')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

        response2 = self.client.get(target_url,follow_redirects=True)
        self.assertEqual(response2.status_code, 200)

    def test_add_CRM_item_view(self):
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        
        target_url = url_for('aicos_crm.add_item')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_add_CRM_item_view_redirects(self):
        """
        Test that new_crm_item_add page redirects to table page
        """ 
        target_url = url_for('aicos_crm.add_item')
        redirect_url2 = url_for('aicos_crm.table', next=target_url)
        response2 = self.client.post(target_url,follow_redirects=True)
        self.assertEqual(response2.status_code, 200)
        # self.assertRedirects(response2, redirect_url2)
        # self.assertIn(b'Thanks for registering!', response2.data)

    def test_edit_CRM_item_view_redirects(self):
        """
        Test that crm_item_edit page is inaccessible without login
        and redirects to login page then to crm_item_edit page
        """
        target_url = url_for('aicos_crm.edit_item', id=1, employee_id=2)
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_edit_CRM_item_view(self):
        """
        Test that crm_item_edit view works as expected
        """
        crm_item = CRM.query.filter_by(id=1).first()
        crm_item.tag = 'secondtag'

        target_url = url_for('aicos_crm.edit_item', id=1, employee_id=2)
        response2 = self.client.post(target_url)
        self.assertEqual(response2.status_code, 200)

        self.assertIs(crm_item.tag,'secondtag')
        # self.assertRedirects(response2, redirect_url2)
        # self.assertIn(b'Thanks for registering!', response2.data)

    def test_remove_CRM_item_view_redirects(self):
        """
        Test that crm_item_remove page is inaccessible without login
        and redirects to login page then to crm_item_remove page
        """
        # crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_crm.remove_item', id=1)
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)

    def test_remove_CRM_item_view(self):
        """
        Test that crm_item_remove view works as expected
        """
        crm_item = CRM.query.filter_by(id=1).first()
        target_url = url_for('aicos_crm.remove_item', id=1)
        # redirect_url2 = url_for('aicos_crm.table', next=target_url)
        # response2 = self.client.get('aicos_crm.add_item',follow_redirects=True)
        response3 = self.client.get(target_url)
        self.assertEqual(response3.status_code, 200)
        # self.assertRedirects(response3, redirect_url2)
        # self.assertIn(b'Thanks for registering!', response3.data)

        self.assertIsNone(crm_item)

    @aicos_req.route('/cooperative/ibyemezo_byinama', methods=['GET', 'POST'])
    @login_required
    def intekoRusangeAdd():
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        
        target_url = url_for('aicos_crm.add_item')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)


        #check_admin()
        # form = intekoRusangeForm()
        # if form.validate_on_submit():
        #     inteko = intekoRusange(
        #                     status1=form.ibyizweho.data,
        #                     decision1=form.decision1.data,
        #                     owner1   = form.owner1.data,
        #                     stakeholders1=form.stakeholders1.data,
        #                     due_date1=form.due_date1.data,
        #                     background1 = form.background1.data,
        #                     department_id = current_user.email
        #                     )

        #     try:
        #         db.session.add(inteko)
        #         #db.session.add(notif)
        #         db.session.commit()
        #         flash("Umaze kubika neza ibyemezo by'inama")
        #     except:
        #         flash("Habayeho ikibazo mu makuru watanze!")
        #     return redirect(url_for('aicos_req.intekoRusangeList'))
        # return render_template("governanceBooks/intekoRusange.html", form=form, title="Create")


    # This is the views for adding new inama y'ubuyobozi meeting notes
    @aicos_req.route('/cooperative/ibyemezoByinamaUbuyobozi', methods=['GET', 'POST'])
    @login_required
    def inamaUbuyoboziAdd():
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        
        target_url = url_for('aicos_crm.add_item')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)


        # check_admin()
        # form = inamaUbuyoboziForm()
        # if form.validate_on_submit():
        #     inama = inamaUbuyobozi(status=form.status.data,
        #                     decision=form.decision.data,
        #                     owner   = form.owner.data,
        #                     stakeholders=form.stakeholders.data,
        #                     due_date=form.due_date.data,
        #                     background = form.background.data,
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
        #     return redirect(url_for('aicos_req.inamaUbuyoboziList'))
        # return render_template("governanceBooks/inamaUbuyobozi.html", form=form, title="Create")





    # This is the views for adding new inama y'ubugenzuzi meeting notes
    @aicos_req.route('/cooperative/ibyemezoByinamaUbugenzuzi', methods=['GET', 'POST'])
    @login_required
    def ubugenzuziAdd(*args, **kwargs):
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        
        target_url = url_for('aicos_crm.add_item')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)


        # check_admin()
        # form = ubugenzuziForm()
        # if form.validate_on_submit():
        #     inamaUbugenzuzi = Ubugenzuzi(status=form.status.data,
        #                     decision=form.decision.data,
        #                     owner   = form.owner.data,
        #                     stakeholders=form.stakeholders.data,
        #                     due_date=form.due_date.data,
        #                     background = form.background.data,
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
        #     return redirect(url_for('aicos_req.ubugenzuziList'))
        # return render_template("governanceBooks/ubugenzuzi.html", form=form, title="Create")




    # Views which are going to be dealing with Accounting Book.
    # def abanyamuryangoImigabane():
    #     """
    #     List all employees
    #     """
    #     check_admin()
    #     check_coop_admin()
    #     #form = LoginForm()
    #     # if form.validate_on_submit():
    #         # check whether employee exists in the database and whether
    #         # the password entered matches the password in the database
    #     #apps = Department.query.filter_by(email=current_user.email).first()
    #     #applications = apps.applications
    #     employee = Department.query.filter_by(email=current_user.email).first()
    #     employees = employee.members
    #     employees_count = employee.members.count()

    #     notes = Notification.query.filter_by(department_id=current_user.email)
    #     #if employees is not None:
    #     #employees = Employee.query.filter_by(email=form.email.data)
    #     return render_template('accountingBooks/imigabane/abanyamuryangoImigabane.html',
    #                         employees=employees,
    #                         employee=employee,
    #                         employees_count=employees_count,
    #                         notes = notes,
    #                         title='Employees')


    @aicos_req.route('/abanyamuryangoImigabaneDetails/<int:id>', methods=['GET', 'POST'])
    @login_required
    def abanyamuryangoDetails(id):
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        
        target_url = url_for('aicos_crm.add_item')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)


        # check_admin()
        # employee = Member.query.get_or_404(id)
        # if employee is not None:
        #     return render_template("accountingBooks/imigabane/abanyamuryangoImigabaneDetails.html", employee=employee)
        # return redirect(url_for('aicos_req.abanyamuryangoImigabane'))






    # Kongera umugabane ku munyamuryango.
    @aicos_req.route('/cooperative/umugabane/add/<int:id>', methods=['GET', 'POST'])
    @login_required
    def edit_umugabane(id):
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        
        target_url = url_for('aicos_crm.add_item')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)


        # """
        # Edit a role
        # """
        # check_admin()
        # #add_role = False
        # member = Member.query.get_or_404(id)
        # form = MemberForm(obj=member)
        # if form.validate_on_submit():
        #     member.firstName = form.firstName.data
        #     member.nId = form.nId.data
        #     db.session.add(member)
        #     db.session.commit()
        #     flash('Umaze kongera umugabane.')
        #     # redirect to the roles pagess
        #     return redirect(url_for('aicos_req.abanyamuryangoImigabane'))
        # form.firstName.data = member.firstName
        # form.nId.data = member.nId
        # return render_template('accountingBooks/imigabane/addUmugabane.html', form=form, title="Edit Umugabane")








    # Isanguku views are here.
    # def isandukuList():
    #     isanduku = Isanduku.query.filter_by().all()
    #     return render_template("accountingBooks/isanduku/isandukuList.html", isanduku=isanduku, title="List y'ibyemezo by'inteko rusange")



    @aicos_req.route('/cooperative/add/Isanduku', methods=['GET', 'POST'])
    @login_required
    def isandukuAdd():
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        
        target_url = url_for('aicos_crm.add_item')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)


        # check_admin()
        # form = isandukuForm()
        # if form.validate_on_submit():
        #     isanduku = Isanduku(

        #                     no=form.no.data,
        #                     done_date=form.done_date.data,
        #                     action=form.action.data,
        #                     income   = form.income.data,
        #                     expense   = form.expense.data,
        #                     remain   = form.remain.data,
        #                     done_by   = form.done_by.data,
        #                     done_to   = form.done_to.data,
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
        #     return redirect(url_for('aicos_req.isandukuList'))
        # return render_template("accountingBooks/isanduku/isanduku.html", form=form, title="Kongera mu Isanduku.")





    # Umusaruro views are here.
    # def umusaruroList():
    #     umusaruro = Umusaruro.query.all()
    #     return render_template("accountingBooks/umusaruro/umusaruroList.html", umusaruro=umusaruro, title="List y'umusaruro winjiye")



    @aicos_req.route('/cooperative/add/Umusaruro', methods=['GET', 'POST'])
    @login_required
    def umusaruroAdd():
        """
        Test that new_crm_item_add page is inaccessible without login
        and redirects to login page then to new_crm_item_add page
        """        
        target_url = url_for('aicos_crm.add_item')
        redirect_url = url_for('auth.login', next=target_url)
        response1 = self.client.get(target_url)
        self.assertEqual(302, response1.status_code)
        self.assertRedirects(response1, redirect_url)


        # check_admin()
        # form = umusaruroForm()
        # if form.validate_on_submit():
        #     umusaruro = Umusaruro(
        #                     Amazina=form.Amazina.data,
        #                     Taliki=form.Taliki.data,
        #                     Uwagemuye=form.Uwagemuye.data,
        #                     Ibiro   = form.Ibiro.data,
        #                     Igiciro   = form.Igiciro.data,
        #                     IkiguziCyose   = form.IkiguziCyose.data,
        #                     amafarangaYishyuweKuKiro   = form.amafarangaYishyuweKuKiro.data,
        #                     done_by   = form.done_by.data,
        #                     done_to   = form.done_to.data,
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
        #     return redirect(url_for('aicos_req.umusaruroList'))
        # return render_template("accountingBooks/umusaruro/umusaruro.html", form=form, title="Kongera umusaruro muri Cooperative.")








    # Views for the Wide Cooperative Market.
    # def wcmIndex():
    #     umusaruro = Umusaruro.query.all()
    #     return render_template('accountingBooks/wcm/index.html', umusaruro=umusaruro)

    # def abishyuye():

    #     employee = Department.query.filter_by(email=current_user.email).first()
    #     employees = employee.members
    #     employees_count = employee.members.count()


    #     return render_template('accountingBooks/abishyuye/abishyuyeList.html',
                                # employees=employees, title='List yabanyamuryango bishyuye!')









    # Views for the Wide Cooperative Market.
    # def bankIbitabo():
    #     bankIbitaboList = ibitaboByaBank.query.all()
    #     return render_template('accountingBooks/ibitaboBank/ibitaboBankList.html', bankIbitaboList=bankIbitaboList)






    # ibitabo bya banks.
    # def ibitaboBank():
    #     form = ibitaboBankForm()
    #     if form.validate_on_submit():
    #         ibitabo = ibitaboBank(
    #                                 no = form.No.data,
    #                                 date = form.Date.data,
    #                                 igikorwa = form.Igikorwa.data,
    #                                 debt     = form.Debit.data,
    #                                 credit   = form.Credit.data,
    #                                 solde    = form.Solde.data,
    #                                 department_id = current_user.email)
    #         try:
    #             db.session.add(ibitabo)
    #             db.session.commit()
    #             flash("Umaze kwinjize igitabo cya bank neza!")
    #             return redirect(url_for('aicos_req.ibitaboBankList'))
    #         except:
    #             flash("Ntago igitabo cyabashije kwinjira neza!")
    #     return render_template('accountingBooks/ibitaboBank/ibitaboBank.html', form=form, title="List y'ibitabo bya banks!")


    # def bankHistory():
    #     return render_template('accountingBooks/bankHistory/bankHistory.html')


    # def signatories():
    #     return render_template('accountingBooks/bankHistory/signatories.html')

    # def amatsinda():
    #     amatsinda = Itsinda.query.all()
    #     member = ItsindaMember.query.all()
    #     return render_template('amatsinda/amatsinda.html', amatsinda=amatsinda, member=member)


    # def koraItsinda():

    #     form = amatsindaForm()

    #     if form.validate_on_submit():

    #         itsinda = Itsinda(
    #                             itsinda_name = form.name.data,
    #                             description = form.description.data,
    #                             purpose = form.purpose.data,
    #                             department_id = current_user.email
    #                             )

    #         try:
    #             db.session.add(itsinda)
    #             db.session.commit()
    #             flash("Umaze kwandika neza itsinda")
    #             return redirect(url_for('aicos_req.amatsinda'))
    #         except:
    #             flash("ntabwo itsinda ryanditse neza ongera ugerageze")
    #             return redirect(url_for('aicos_req.koraItsinda'))

    #     return render_template('/amatsinda/koraItsinda.html', form=form)


    # def amatsindaMembers(id):
    #     itsinda = Itsinda.query.get_or_404(id)
    #     itsindaName = Itsinda.query.filter_by(id=itsinda.id).first()
    #     members = Member.query.all()
    #     itsindamember = ItsindaMember.query.filter_by(itsinda_id=itsinda.id).all()
    #     return render_template('/amatsinda/all_itsinda_members.html', members=members, itsindaName=itsindaName, itsindamember=itsindamember)



    # def add_members(id):
    #     itsinda = Itsinda.query.get_or_404(id)
    #     itsindaName = Itsinda.query.filter_by(id=itsinda.id).first()
    #     members = Member.query.all()
    #     itsindamember = ItsindaMember.query.all()
    #     return render_template('/amatsinda/add_itsinda_members.html', members=members, itsindaName=itsindaName, itsindamember=itsindamember)

    # def ongeramo_member(a, b):
    #     memberId = Member.query.get_or_404(a)
    #     itsindaId = Itsinda.query.get_or_404(b)
    #     itsindaName = Itsinda.query.filter_by(id=itsindaId.id).first()
    #     member = Member.query.filter_by(id=memberId.id).first()
    #     members = Member.query.all()
    #     itsinda = Itsinda.query.filter_by(id=itsindaId.id).first()

    #     itsindamember = ItsindaMember(
    #                                 member_id=member.id,
    #                                 itsinda_id=itsinda.id,
    #                                 member_firstname=member.izina_ribanza,
    #                                 member_secondname=member.izina_rikurikira,
    #                                 itsinda_name=itsinda.itsinda_name,
    #                                 department_id=current_user.email
    #                                 )
    #     try:
    #         db.session.add(itsindamember)
    #         db.session.commit()
    #         flash("Umunyamuryango yinjiye neza mwitsinda " + "\"" + itsindaName.itsinda_name + "\"")
    #         return redirect(url_for('aicos_req.add_members', id=itsinda.id))
    #     except:
    #         db.session.rollback()
    #         flash("Umunyamuryango asanzwe arimo")
    #         return render_template('/amatsinda/add_itsinda_members.html', members=members, itsindaName=itsindaName)
    #     return render_template('/amatsinda/add_itsinda_members.html', members=members, itsindaName=itsindaName)
        


    # def rukomatanyi():
    #     rukomatanyo = Rukomatanyo.query.all()
    #     isanduku = IsandukuNshya.query.filter_by(department_id=current_user.email).all()
    #     bank = BankModel.query.filter_by(department_id=current_user.email).all()
    #     inguzanyo_zatanzwe = InguzanyoZatanzwe.query.filter_by(department_id=current_user.email).all()
    #     ibiramba = Ibiramba.query.filter_by(department_id=current_user.email).all()
    #     ububiko = Ububiko.query.filter_by(department_id=current_user.email).all()
    #     umugabane_shingiro = UmugabaneShingiro.query.filter_by(department_id=current_user.email).all()
    #     inkunga = Inkunga.query.filter_by(department_id=current_user.email).all()
    #     inguzanyo_abandi = InguzanyoZabandi.query.filter_by(department_id=current_user.email).all()
    #     ibicuruzwa = Ibicuruzwa.query.filter_by(department_id=current_user.email).all()
    #     ikoreshwa = IkoreshwaRyimari.query.filter_by(department_id=current_user.email).all()
    #     isanduku_cr_sum = db.session.query(func.sum(IsandukuNshya.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    #     isanduku_db_sum = db.session.query(func.sum(IsandukuNshya.asigaye)).filter_by(department_id=current_user.email).scalar()
    #     bank_cr_sum = db.session.query(func.sum(BankModel.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    #     bank_db_sum = db.session.query(func.sum(BankModel.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    #     inguzanyo_db_sum = db.session.query(func.sum(InguzanyoZabandi.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    #     inguzanyo_cr_sum = db.session.query(func.sum(InguzanyoZabandi.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    #     ibiramba_cr_sum = db.session.query(func.sum(Ibiramba.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    #     ibiramba_db_sum = db.session.query(func.sum(Ibiramba.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    #     ububiko_cr_sum = db.session.query(func.sum(Ububiko.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    #     ububiko_db_sum = db.session.query(func.sum(Ububiko.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    #     umugabane_cr_sum = db.session.query(func.sum(UmugabaneShingiro.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    #     umugabane_db_sum = db.session.query(func.sum(UmugabaneShingiro.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    #     inkunga_db_sum = db.session.query(func.sum(Inkunga.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    #     inkunga_cr_sum = db.session.query(func.sum(Inkunga.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    #     inguzanyo_abandi_cr_sum = db.session.query(func.sum(InguzanyoZabandi.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    #     inguzanyo_abandi_db_sum = db.session.query(func.sum(InguzanyoZabandi.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    #     ibindi_cr_sum = db.session.query(func.sum(IbindiRukomatanyi.ayasohotse)).filter_by(department_id=current_user.email).scalar()
    #     ibindi_db_sum = db.session.query(func.sum(IbindiRukomatanyi.ayinjiye)).filter_by(department_id=current_user.email).scalar()
    #     return render_template('/accountingBooks/rukomatanyi/index.html', 
    #                                                                 isanduku=isanduku,
    #                                                                 bank=bank,
    #                                                                 isanduku_cr_sum=isanduku_cr_sum,
    #                                                                 isanduku_db_sum=isanduku_db_sum,
    #                                                                 bank_cr_sum = bank_cr_sum,
    #                                                                 bank_db_sum = bank_db_sum,
    #                                                                 inguzanyo_abandi_cr_sum = inguzanyo_abandi_cr_sum,
    #                                                                 inguzanyo_abandi_db_sum = inguzanyo_abandi_db_sum,
    #                                                                 inguzanyo_cr_sum = inguzanyo_cr_sum,
    #                                                                 inguzanyo_db_sum = inguzanyo_db_sum,
    #                                                                 inguzanyo_zatanzwe=inguzanyo_zatanzwe,
    #                                                                 ibiramba_cr_sum = ibiramba_cr_sum,
    #                                                                 ibiramba_db_sum = ibiramba_db_sum,
    #                                                                 ibindi_cr_sum = ibindi_cr_sum,
    #                                                                 ibindi_db_sum = ibindi_db_sum,
    #                                                                 ububiko_db_sum = ububiko_db_sum,
    #                                                                 ububiko_cr_sum = ububiko_cr_sum ,
    #                                                                 inkunga_cr_sum = inkunga_cr_sum,
    #                                                                 inkunga_db_sum = inkunga_db_sum,
    #                                                                 umugabane_cr_sum = umugabane_cr_sum,
    #                                                                 umugabane_db_sum = umugabane_db_sum,
    #                                                                 ibiramba=ibiramba,
    #                                                                 ububiko=ububiko,
    #                                                                 umugabane_shingiro=umugabane_shingiro,
    #                                                                 inkunga=inkunga,
    #                                                                 inguzanyo_abandi=inguzanyo_abandi,
    #                                                                 ibicuruzwa=ibicuruzwa,
    #                                                                 ikoreshwa=ikoreshwa,
    #                                                                 rukomatanyo = rukomatanyo
    #                                                                 )


    # def isanduku():
    #     isanduku = IsandukuNshya.query.filter_by(department_id=current_user.email).all()
    #     rukomatanyo = Rukomatanyo.query.all()
    #     return render_template('/accountingBooks/rukomatanyi/isanduku.html', isanduku=isanduku, rukomatanyo=rukomatanyo)

    # def hinduraIsanduku(id):
    #     isanduku_id = IsandukuNshya.query.get_or_404(id)
    #     ibihinduka = IsandukuNshya.query.filter_by(id=isanduku_id.id).first()
    #     form = IsandukuForm()
    #     if form.validate_on_submit():
    #         ibihinduka.ayinjiye = form.ayinjiye.data
    #         ibihinduka.ayasohotse = form.ayasohotse.data
    #         try:
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.isanduku'))
    #         except:
    #             return redirect(url_for('aicos_req.hinduraIsanduku'))
    #     form.ayinjiye.default = ibihinduka.ayinjiye
    #     form.ayasohotse.default = ibihinduka.ayasohotse
    #     form.process()
    #     return render_template('accountingBooks/rukomatanyi/rukomatanyi_form/hindura_isanduku.html', form=form)


    # def bank():
    #     bank = BankModel.query.filter_by(department_id=current_user.email).all()
    #     rukomatanyo = Rukomatanyo.query.all()
    #     return render_template('/accountingBooks/rukomatanyi/bank.html', bank=bank, rukomatanyo=rukomatanyo)

    # def hinduraBank(id):
    #     bankId = BankModel.query.get_or_404(id)
    #     bank = BankModel.query.filter_by(id=bankId.id).first()
    #     form = BankForm()
    #     if form.validate_on_submit():
    #         bank.ayinjiye = form.ayinjiye.data
    #         bank.ayasohotse = form.ayasohotse.data
    #         try:
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.bank'))
    #         except:
    #             return redirect(url_for('aicos_req.hinduraBank', form=form))
    #     form.ayinjiye.default = bank.ayinjiye
    #     form.ayasohotse.default = bank.ayasohotse
    #     form.process()
    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_bank.html', form=form)


    # def inguzanyo_zatanzwe():
    #     inguzanyo_zatanzwe = InguzanyoZatanzwe.query.filter_by(department_id=current_user.email).all()
    #     rukomatanyo = Rukomatanyo.query.all()
    #     return render_template('/accountingBooks/rukomatanyi/inguzanyo_zatanzwe.html', inguzanyo_zatanzwe=inguzanyo_zatanzwe, rukomatanyo=rukomatanyo)

    # def hinduraInguzanyoZatanzwe(id):
    #     inguzanyoId = InguzanyoZatanzwe.query.get_or_404(id)
    #     inguzanyo = InguzanyoZatanzwe.query.filter_by(id=inguzanyoId.id).first()
    #     form = InguzanyoZatanzweForm()
    #     if form.validate_on_submit():
    #         inguzanyo.ayinjiye = form.ayinjiye.data
    #         inguzanyo.ayasohotse = form.ayasohotse.data
    #         try:
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.inguzanyo_zatanzwe'))
    #         except:
    #             return redirect(url_for('aicos_req.hinduraInguzanyoZatanzwe', form=form))
    #     form.ayinjiye.default = inguzanyo.ayinjiye
    #     form.ayasohotse.default = inguzanyo.ayasohotse
    #     form.process()
    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_inguzanyo_zatanzwe.html', form=form)


    # def ibiramba():
    #     ibiramba = Ibiramba.query.filter_by(department_id=current_user.email).all()
    #     rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    #     return render_template('/accountingBooks/rukomatanyi/ibiramba.html', ibiramba=ibiramba, rukomatanyo=rukomatanyo)

    # def hinduraIbiramba(id):
    #     ibirambaId = Ibiramba.query.get_or_404(id)
    #     ibiramba = Ibiramba.query.filter_by(id=ibirambaId.id).first()
    #     form = IbirambaForm()
    #     if form.validate_on_submit():
    #         ibiramba.ayinjiye = form.ayinjiye.data
    #         ibiramba.ayasohotse = form.ayasohotse.data
    #         try:
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.ibiramba'))
    #         except:
    #             return redirect(url_for('aicos_req.hinduraIbiramba'))
    #     form.ayinjiye.default = ibiramba.ayinjiye
    #     form.ayasohotse.default = ibiramba.ayasohotse
    #     form.process()
    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ibaramba.html', form=form)


    # def ububiko():
    #     ububiko = Ububiko.query.filter_by(department_id=current_user.email).all()
    #     rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    #     return render_template('/accountingBooks/rukomatanyi/ububiko.html', ububiko=ububiko, rukomatanyo=rukomatanyo)

    # def hinduraUbubiko(id):
    #     ububikoId = Ububiko.query.get_or_404(id)
    #     ububiko = Ububiko.query.filter_by(id=ububikoId.id).first()
    #     form = UbubikoForm()
    #     if form.validate_on_submit():
    #         ububiko.ayinjiye = form.ayinjiye.data
    #         ububiko.ayasohotse = form.ayasohotse.data
    #         try:
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.ububiko'))
    #         except:
    #             return redirect(url_for('aicos_req.hinduraUbubiko', form=form))
    #     form.ayinjiye.default = ububiko.ayinjiye
    #     form.ayasohotse.default = ububiko.ayasohotse
    #     form.process()
    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ububiko.html', form=form)

    # def umugabane_shingiro():
    #     umugabane_shingiro = UmugabaneShingiro.query.filter_by(department_id=current_user.email).all()
    #     rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    #     return render_template('/accountingBooks/rukomatanyi/umugabane_shingiro.html', umugabane_shingiro=umugabane_shingiro, rukomatanyo=rukomatanyo)

    # def hinduraUmugabaneShingiro(id):
    #     umugabaneId = UmugabaneShingiro.query.get_or_404(id)
    #     umugabane = UmugabaneShingiro.query.filter_by(id=umugabaneId.id).first()
    #     form = UmugabaneShingiroForm()
    #     if form.validate_on_submit():
    #         umugabane.ayinjiye = form.ayinjiye.data
    #         umugabane.ayasohotse = form.ayasohotse.data
    #         try:
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.umugabane_shingiro'))
    #         except:
    #             return redirect(url_for('aicos_req.hinduraUmugabaneShingiro', form=form))
    #     form.ayinjiye.default = umugabane.ayinjiye
    #     form.ayasohotse.default = umugabane.ayasohotse
    #     form.process()
    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_umugabane_shingiro.html', form=form)

    # def inkunga():
    #     inkunga = Inkunga.query.filter_by(department_id=current_user.email).all()
    #     rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    #     return render_template('/accountingBooks/rukomatanyi/inkunga.html', inkunga=inkunga, rukomatanyo = rukomatanyo)

    # def hindura_inkunga(id):
    #     inkungaId = Inkunga.query.get_or_404(id)
    #     inkunga = Inkunga.query.filter_by(id=inkungaId.id).first()
    #     form = InkungaForm()
    #     if form.validate_on_submit():
    #         inkunga.ayinjiye = form.ayinjiye.data
    #         inkunga.ayasohotse = form.ayasohotse.data
    #         try:
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.inkunga'))
    #         except:
    #             return redirect(url_for('aicos_req.hindura_inkunga', form=form))
    #     form.ayinjiye.default = inkunga.ayinjiye
    #     form.ayasohotse.default = inkunga.ayasohotse
    #     form.process()
    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_inkunga.html', form=form)

    # def inguzanyo_abandi():
    #     inguzanyo_abandi = InguzanyoZabandi.query.filter_by(department_id=current_user.email).all()
    #     rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    #     return render_template('accountingBooks/rukomatanyi/inguzanyo_abandi.html', inguzanyo_abandi=inguzanyo_abandi, rukomatanyo=rukomatanyo)


    # def hinduraInguzanyoZabandi(id):
    #     inguzanyoId = InguzanyoZabandi.query.get_or_404(id)
    #     inguzanyo = InguzanyoZabandi.query.filter_by(id=inguzanyoId.id).first()
    #     form = InguzanyoZabandiForm()
    #     if form.validate_on_submit():
    #         inguzanyo.ayinjiye = form.ayinjiye.data
    #         inguzanyo.ayasohotse = form.ayasohotse.data
    #         try:
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.inguzanyo_abandi'))
    #         except:
    #             redirect(url_for('aicos_req.hinduraInguzanyoZabandi', form=form))
    #     form.ayinjiye.default = inguzanyo.ayinjiye
    #     form.ayasohotse.default = inguzanyo.ayasohotse
    #     form.process()
    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_inguzanyo_zabandi.html', form=form)



    # def ibicuruzwa():
    #     ibicuruzwa = Ibicuruzwa.query.filter_by(department_id=current_user.email).all()
    #     rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    #     return render_template('/accountingBooks/rukomatanyi/ibicuruzwa.html', ibicuruzwa=ibicuruzwa, rukomatanyo=rukomatanyo)

    # def hindura_ibicuruzwa(id):
    #     ibicuruzwaId = Ibicuruzwa.query.get_or_404(id)
    #     ibicuruzwa = Ibicuruzwa.query.filter_by(id=ibicuruzwaId.id).first()
    #     form = IbicuruzwaForm()

    #     if form.validate_on_submit():
    #         ibicuruzwa.ayinjiye = form.ayinjiye.data
    #         ibicuruzwa.ayasohotse = form.ayasohotse.data
    #         try:
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.ibicuruzwa'))
    #         except:
    #             return redirect(url_for('aicos_req.hindura_ibicuruzwa', form=form))
    #     form.ayinjiye.default = ibicuruzwa.ayinjiye
    #     form.ayasohotse.default = ibicuruzwa.ayasohotse
    #     form.process()
    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ibicuruzwa.html', form=form)


    # def ikoreshwa_ryimari():
    #     ikoreshwa = IkoreshwaRyimari.query.filter_by(department_id=current_user.email).all()
    #     rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()
    #     return render_template('/accountingBooks/rukomatanyi/ikoreshwa_ryimari.html', ikoreshwa=ikoreshwa, rukomatanyo=rukomatanyo)

    # def hinduraIkoreshwaRyimari(id):
    #     ikoreshwaId = IkoreshwaRyimari.query.get_or_404(id)
    #     ikoreshwa = IkoreshwaRyimari.query.filter_by(id=ikoreshwaId.id).first()
    #     form = IkoreshwaRyimariForm()

    #     if form.validate_on_submit():
    #         ikoreshwa.ayinjiye = form.ayinjiye.data
    #         ikoreshwa.ayasohotse = form.ayasohotse.data
    #         try:
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.ikoreshwa_ryimari'))
    #         except:
    #             return redirect(url_for('aicos_req.hinduraIkoreshwaRyimari', form=form))
    #     form.ayinjiye.default = ikoreshwa.ayinjiye
    #     form.ayasohotse.default = ikoreshwa.ayasohotse
    #     form.process()
    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ikoreshwa_ryimari.html', form=form)

    # def ibindi_rukomatanyi():
    #     ibindi = IbindiRukomatanyi.query.filter_by(department_id=current_user.email).all()
    #     rukomatanyo = Rukomatanyo.query.filter_by(department_id=current_user.email).all()   
    #     return render_template('/accountingBooks/rukomatanyi/ibindi_rukomatanyi.html', ibindi=ibindi, rukomatanyo=rukomatanyo)

    # def hindura_ibindi(id):
    #     ibindiId= IbindiRukomatanyi.query.get_or_404(id)
    #     ibindi = IbindiRukomatanyi.query.filter_by(id=ibindiId.id).first()
    #     form = IbindiForm()

    #     if form.validate_on_submit():
    #         ibindi.ayinjiye = form.ayinjiye.data
    #         ibindi.ayasohotse = form.ayasohotse.data
    #         try:
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.ibindi_rukomatanyi'))
    #         except:
    #             return redirect(url_for('aicos_req.hindura_ibindi', form=form))
    #     form.ayinjiye.default = ibindi.ayinjiye
    #     form.ayasohotse.default = ibindi.ayasohotse
    #     form.process()
    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/hindura_ibindi.html', form=form)


    # def injiza_isanduku():
    #     form = IsandukuForm()

    #     if form.validate_on_submit():
    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = form.itariki.data,
    #                             description = form.impamvu.data,
    #                             piyesi = form.piyesi.data
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
    #             return redirect(url_for('aicos_req.injiza_isanduku'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
    #             return redirect(url_for('aicos_req.injiza_isanduku'))

    #         isanduku = IsandukuNshya(
    #                             ayinjiye = form.ayinjiye.data,
    #                             ayasohotse = form.ayasohotse.data,
    #                             asigaye = form.asigaye.data,
    #                             department_id = current_user.email,
    #                             rukomatanyo_id = rukomatanyo_id.id
    #                             )

    #         try:
    #             db.session.add(isanduku)
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.isanduku'))
    #         except:
    #             return redirect(url_for('aicos_req.injiza_isanduku', form=form))
    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_isanduku.html', form=form)


    # def injizaBank():
    #     form = BankForm()

    #     if form.validate_on_submit():
    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = form.itariki.data,
    #                             description = form.impamvu.data,
    #                             piyesi = form.piyesi.data
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
    #             return redirect(url_for('aicos_req.injizaBank'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
    #             return redirect(url_for('aicos_req.injizaBank'))

    #         bank = BankModel(
    #                         ayinjiye = form.ayinjiye.data,
    #                         ayasohotse = form.ayasohotse.data,
    #                         department_id = current_user.email,
    #                         rukomatanyo_id=rukomatanyo_id.id
    #                         )

    #         try:
    #             db.session.add(bank)
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.bank'))
    #         except:
    #             return redirect(url_for('aicos_req.injizaBank', form=form))
    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_bank.html', form=form)

    # def InjizaIzatanzwe():
    #     form = InguzanyoZatanzweForm()

    #     if form.validate_on_submit():

    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = form.itariki.data,
    #                             description = form.impamvu.data,
    #                             piyesi = form.piyesi.data,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
    #             return redirect(url_for('aicos_req.InjizaIzatanzwe'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
    #             return redirect(url_for('aicos_req.InjizaIzatanzwe'))

    #         inguzanyo = InguzanyoZatanzwe(
    #                                     ayinjiye = form.ayinjiye.data,
    #                                     ayasohotse = form.ayasohotse.data,
    #                                     department_id = current_user.email,
    #                                     rukomatanyo_id = rukomatanyo_id.id
    #                                     )
    #         try:
    #             db.session.add(inguzanyo)
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.inguzanyo_zatanzwe'))
    #         except:
    #             return redirect(url_for('aicos_req.InjizaIzatanzwe', form=form))
    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/InjizaIzatanzwe.html', form=form)


    # def record_ibiramba():
    #     form = IbirambaForm()

    #     if form.validate_on_submit():

    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = form.itariki.data,
    #                             description = form.impamvu.data,
    #                             piyesi = form.piyesi.data,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
    #             return redirect(url_for('aicos_req.record_ibiramba'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
    #             return redirect(url_for('aicos_req.record_ibiramba'))

    #         iramba = Ibiramba(
    #                         ayinjiye = form.ayinjiye.data,
    #                         ayasohotse = form.ayasohotse.data,
    #                         department_id = current_user.email,
    #                         rukomatanyo_id = rukomatanyo_id.id
    #                         )
    #         try:
    #             db.session.add(iramba)
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.ibiramba'))
    #         except:
    #             return redirect(url_for('aicos_req.record_ibiramba', form=form))

    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ibiramba.html', form=form)

    # def record_ububiko():
    #     form = UbubikoForm()

    #     if form.validate_on_submit():

    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = form.itariki.data,
    #                             description = form.impamvu.data,
    #                             piyesi = form.piyesi.data,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
    #             return redirect(url_for('aicos_req.record_ububiko'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
    #             return redirect(url_for('aicos_req.record_ububiko'))

    #         ububiko = Ububiko(
    #                         ayinjiye = form.ayinjiye.data,
    #                         ayasohotse = form.ayasohotse.data,
    #                         department_id = current_user.email,
    #                         rukomatanyo_id = rukomatanyo_id.id
    #                         )

    #         try:
    #             db.session.add(ububiko)
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.ububiko'))
    #         except:
    #             return redirect(url_for('aicos_req.record_ububiko', form=form))

    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ububiko.html', form=form)


    # def record_umugabane_shingiro():
    #     form = UmugabaneShingiroForm()

    #     if form.validate_on_submit():

    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = form.itariki.data,
    #                             description = form.impamvu.data,
    #                             piyesi = form.piyesi.data,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
    #             return redirect(url_for('aicos_req.record_umugabane_shingiro'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
    #             return redirect(url_for('aicos_req.record_umugabane_shingiro'))

    #         umugabane = UmugabaneShingiro(
    #                                 ayinjiye = form.ayinjiye.data,
    #                                 ayasohotse = form.ayasohotse.data,
    #                                 department_id = current_user.email,
    #                                 rukomatanyo_id = rukomatanyo_id.id
    #                                 )
    #         try:
    #             db.session.add(umugabane)
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.umugabane_shingiro'))
    #         except:
    #             return redirect(url_for('aicos_req.record_umugabane_shingiro', form=form))

    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_umugabane_shingiro.html', form=form)


    # def record_inkunga():
    #     form = InkungaForm()

    #     if form.validate_on_submit():

    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = form.itariki.data,
    #                             description = form.impamvu.data,
    #                             piyesi = form.piyesi.data,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
    #             return redirect(url_for('aicos_req.record_inkunga'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
    #             return redirect(url_for('aicos_req.record_inkunga'))

    #         inkunga = Inkunga(
    #                         ayinjiye = form.ayinjiye.data,
    #                         ayasohotse = form.ayasohotse.data,
    #                         department_id = current_user.email,
    #                         rukomatanyo_id = rukomatanyo_id.id
    #                         )
    #         try:
    #             db.session.add(inkunga)
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.inkunga'))
    #         except:
    #             return redirect(url_for('aicos_req.record_inkunga'))

    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_inkunga.html', form=form)


    # def record_inguzanyo_abandi():
    #     form = InguzanyoZabandiForm()

    #     if form.validate_on_submit():

    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = form.itariki.data,
    #                             description = form.impamvu.data,
    #                             piyesi = form.piyesi.data,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
    #             return redirect(url_for('aicos_req.record_inkunga'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
    #             return redirect(url_for('aicos_req.record_inkunga'))

    #         inguzanyo = InguzanyoZabandi(
    #                                 ayinjiye = form.ayinjiye.data,
    #                                 ayasohotse = form.ayasohotse.data,
    #                                 department_id = current_user.email,
    #                                 rukomatanyo_id = rukomatanyo_id.id 
    #                                 )
    #         try:
    #             db.session.add(inguzanyo)
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.inguzanyo_abandi'))
    #         except:
    #             return redirect(url_for('aicos_req.record_inguzanyo_abandi'))

    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_inguzanyo_abandi.html', form=form)

    # def record_ibicuruzwa():
    #     form = IbicuruzwaForm()

    #     if form.validate_on_submit():


            
    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = form.itariki.data,
    #                             description = form.impamvu.data,
    #                             piyesi = form.piyesi.data,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
    #             return redirect(url_for('aicos_req.record_ibicuruzwa'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
    #             return redirect(url_for('aicos_req.record_ibicuruzwa'))

    #         ibicuruzwa = Ibicuruzwa(
    #                                 ayinjiye = form.ayinjiye.data,
    #                                 ayasohotse = form.ayasohotse.data,
    #                                 department_id = current_user.email,
    #                                 rukomatanyo_id = rukomatanyo_id.id
    #                                 )
    #         try:
    #             db.session.add(ibicuruzwa)
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.ibicuruzwa'))
    #         except:
    #             return redirect(url_for('aicos_req.record_ibicuruzwa', form=form))

    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ibicuruzwa.html', form=form)


    # def record_ikoreshwa_ryimari():
    #     form = IkoreshwaRyimariForm()

    #     if form.validate_on_submit():


    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = form.itariki.data,
    #                             description = form.impamvu.data,
    #                             piyesi = form.piyesi.data,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
    #             return redirect(url_for('aicos_req.record_ikoreshwa_ryimari'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
    #             return redirect(url_for('aicos_req.record_ikoreshwa_ryimari'))

    #         ikoreshwa = IkoreshwaRyimari(
    #                                     ayinjiye = form.ayinjiye.data,
    #                                     ayasohotse = form.ayasohotse.data,
    #                                     department_id = current_user.email,
    #                                     rukomatanyo_id = rukomatanyo_id.id 
    #                                     )
    #         try:
    #             db.session.add(ikoreshwa)
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.ikoreshwa_ryimari'))
    #         except:
    #             return redirect(url_for('aicos_req.record_ikoreshwa_ryimari'))

    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ikoreshwa_ryimari.html', form=form)
            


    # def record_ibindi():
    #     form = IbindiForm()

    #     if form.validate_on_submit():


    #         rukomatanyo = Rukomatanyo(
    #                             tariki_byakozwe = form.itariki.data,
    #                             description = form.impamvu.data,
    #                             piyesi = form.piyesi.data,
    #                             department_id = current_user.email
    #                             )
    #         try:
    #             db.session.add(rukomatanyo)
    #             db.session.commit()
    #         except:
    #             flash("Ntabwo byakunze neza")
    #             return redirect(url_for('aicos_req.record_ibindi'))

    #         rukomatanyo_id = Rukomatanyo.query.order_by('-id').first()

    #         if rukomatanyo_id is None:
    #             return redirect(url_for('aicos_req.record_ibindi'))

    #         ibindi = IbindiRukomatanyi(
    #                                 ayinjiye = form.ayinjiye.data,
    #                                 ayasohotse = form.ayasohotse.data,
    #                                 department_id = current_user.email,
    #                                 rukomatanyo_id = rukomatanyo_id.id 
    #                                 )
    #         try:
    #             db.session.add(ibindi)
    #             db.session.commit()
    #             return redirect(url_for('aicos_req.ibindi_rukomatanyi'))
    #         except:
    #             return redirect(url_for('aicos_req.record_ibindi'))

    #     return render_template('/accountingBooks/rukomatanyi/rukomatanyi_form/record_ibindi.html', form=form)






    # def UbwisazureList():
    #     ubwisazurexx = UbwisazureEnter.query.all()
    #     return render_template('accountingBooks/ubwisazure/ubwisazure_list.html',
    #                             ubwisazurexx=ubwisazurexx, title='Ubwisazure ku mutungo wa cooperative!!')






    # ibitabo bya banks.
    # def UbwisazureBwose():
    #     form = UbwisazureForm()
    #     if form.validate_on_submit():
    #         ubwisazurex = UbwisazureEnter(
    #                                 AssetDescription = form.AssetDescriptionx.data,
    #                                 cost = form.costx.data,
    #                                 YearOfPurchase = form.YearOfPurchasex.data,
    #                                 SalvageValue = form.SalvageValuex.data,
    #                                 UsefulLife = form.UsefulLifex.data,
    #                                 Method = form.Methodx.data,
    #                                 department_id = current_user.email
    #                                 )

    #         try:
    #             db.session.add(ubwisazurex)
    #             db.session.commit()
    #             flash("Umaze kwinjize umutungo neza!")
    #             return redirect(url_for('aicos_req.UbwisanzureList'))
    #         except:
    #             flash("Ntago umutungo wabashije kwinjira neza!")
    #     return render_template('accountingBooks/ubwisazure/ubwisazure_form.html', form=form, title="List y'ubwisazure bw'umutungo!")





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