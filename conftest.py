import pytest
from app.models import *
from app import create_app,app,api
from flask import Flask, abort, url_for
from app.aicos_members import views

# @pytest.fixture
# def app():
#     app = create_app()
#     return app

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    test_client = app.test_client()
 
    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()
 
    yield test_client  # this is where the testing happens!
 
    ctx.pop()

@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.drop_all()
    db.create_all()
 
    member = Member(sno='311')
#     department = Department(email='depa201@gmail.com')
    applytraining = applyTraining(namea='applytraining')
    notification = Notification(action='action',done_by='done_by')
#     employee = Employee(email='empl201@gmail.com',password='pass@123', is_admin=True)
    federation = Federation(code='211')
    training = Training(name='ingingo',trainer='trainer',about='about',
                                description='description',date='date')

    
    admin = Employee(username="admin", email='admin@gmail.com',password="admin2016", is_admin=True)

# create test non-admin user
    employee = Employee(username="test_user", password="test2016", is_admin=True)

    department = Department(email='paritoma10001@gmail.com', name="IT", description="The IT Department")

    goal = Goal(name='name10001',Description='description',Amount='amount',startingDate='startingDate',endingDate='endingDate')
    staff = Staff(first_name='firstName',last_name='lastName',nid='Nid',district='District',sector='Sector',
                sex='Sex',yob='Yob',position='Position',education='Education',telephone='Telephone',
                email='Email',monthly_net_salary='monthlyNetSalary')
    committee = Committee(first_name='firstName',last_name='lastName',nid='Nid',district='District',
                sector='Sector',sex='Sex',yob='Yob',committee='Committee',position='Position',
                education='Education',telephone='Telephone',email='Email',
                monthly_net_salary='monthlyNetSalary')
    activity = Activity(name='name10001',description='description2')
    asset = Asset(asset_type='assetType',asset_location='assetLocation',asset_value='assetValue',
                description='description')
    role = Role(name="CEO 10001", description="Run the whole company")
    payment = Payment(reason='name10001',amount='amount',date='date')
    howto = Howto(name='name10001',labels='labels',description='description',steps='steps',file='file')
    link = Link(link='link',title='title',labels='labels',sharewith='sharewith',comment='comment')
    report = Report(status='status',description='description')
    dec = Decision(status='status',decision='decision',owner='owner',stakeholders='stakeholders',
                due_date='due_date',background='background')
    # contr = Contribution()
    com = Communication(ms_from='ms_from',to='to',message='message',comment='comment')
    notif = Notification(action="Communication",done_by=employee.username,done_from='IP',
                done_time = "frank",done_to="tapayi",effect = "system upgraded")
    app = Application(emailaa='emailaa',firstNameaa='firstNameaa',secondNameaa='secondNameaa',
                othersaa='othersaa',Districtaa='Districtaa',Sectoraa='Sectoraa',
                Cellaa='Cellaa',nIdaa='nIdaa',entryDateaa='entryDateaa',shareaa='shareaa',
                exitDateaa='exitDateaa',umuzunguraaa='umuzunguraaa',umukonoaa='umukonoaa',genderaa='genderaa',
                dobaa='dobaa',phoneaa='phoneaa',Amashuriaa='Amashuriaa',Ubumugaaa='Ubumugaaa')
                
    member = Member(sno=110001
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
    # db.session.add(contr)
    db.session.add(com)
    db.session.add(notif)
    db.session.add(app)
    db.session.add(member)
    # db.session.add(subs)
    db.session.add(zone)


    
    db.session.add(member)
    db.session.add(department)
    db.session.add(applytraining)
    db.session.add(notification)
    db.session.add(employee)
    db.session.add(federation)
    db.session.add(training)
 
    db.session.commit()
 
    yield db  # this is where the testing happens!
    
    response = test_client.post(url_for('auth.login'),data=dict(email="admin@gmail.com",password="admin2016"))

    assert response.status_code == 200

    app.login_manager._current_user = admin

    # self.assertEqual(current_user.first_name, 'joe')

#     assert b"emp1" in response.data

    # self.assertTrue(employee.is_authenticated)  
    # self.assertTrue(employee.is_active)  
    # self.assertFalse(employee.is_anonymous)  
    # self.assertEqual(employee.id, int(employee.get_id()))

 
    db.drop_all()

# @pytest.fixture(scope='module')
# def training(init_database):
#     # training = Training(name='ingingo',trainer='trainer',about='about',
#                         # description='description',date='date')
#     member = init_database.member
#     department = init_database.Department
#     applytraining = init_database.applyTraining
#     notification = init_database.Notification
#     employee = init_database.Employee
#     # federation = init_database.Federation
#     training = init_database.Training

#     return training,member,department,applytraining,notification,employee,federation                   