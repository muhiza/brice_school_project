import pytest
from app.models import *
from app import create_app

# from /app import create_app

# @pytest.fixture
# def app():
#     app = create_app()
#     return app

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = app.test_client()
 
    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()
 
    yield testing_client  # this is where the testing happens!
 
    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()
 
    member = Member(sno='1000')
    department = Department(email='dep1@gmail.com')
    applytraining = applyTraining(namea='applytraining')
    notification = Notification(action='action',done_by='done_by')
    employee = Employee(email='emp1@gmail.com',password='pass@123', is_admin=True)
    federation = Federation(code='2000')
    training = Training(name='ingingo',trainer='trainer',about='about',
                                description='description',date='date')

    # db.session.add(member)
    db.session.add(department)
    db.session.add(applytraining)
    db.session.add(notification)
    db.session.add(employee)
    # db.session.add(federation)
    db.session.add(training)
 
    db.session.commit()
 
    yield db  # this is where the testing happens!
    
    with test_client:
            employee = employee

            response = test_client.post(url_for('auth.login'),data=dict(email="emp1@gmail.com",password="pass@123"))

            assert response.status_code == 200
            # self.assertEqual(current_user.first_name, 'joe')

            assert b"emp1" in response.data

            # self.assertTrue(employee.is_authenticated)  
            # self.assertTrue(employee.is_active)  
            # self.assertFalse(employee.is_anonymous)  
            # self.assertEqual(employee.id, int(employee.get_id()))

 
    db.drop_all()

@pytest.fixture(scope='module')
def training(init_database):
    # training = Training(name='ingingo',trainer='trainer',about='about',
                        # description='description',date='date')
    member = init_database.member
    department = init_database.Department
    applytraining = init_database.applyTraining
    notification = init_database.Notification
    employee = init_database.Employee
    # federation = init_database.Federation
    training = init_database.Training

    return training,member,department,applytraining,notification,employee,federation                   