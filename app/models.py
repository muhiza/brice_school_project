#################################
#########   models      #########
#################################

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from datetime import datetime


import datetime
from sqlalchemy import DateTime


class Cooperative(UserMixin, db.Model):
    """
    Creating the cooperative database here.
    """
    __tablename__ = "cooperatives"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(200))
    employees = db.relationship(
        'Employee', backref='cooperative', lazy='dynamic')

    def __repr__(self):
        return '<Cooperative: {}>'.format(self.name)

    """
    subs = db.Table('subs',
        db.Column('employee_id', db.Integer, db.ForeignKey('employees.id')),
        db.Column('department_id', db.String(399), db.ForeignKey('departments.email'))
        )
    """


class Employee(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True)
    username = db.Column(db.String(60), index=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    phone_number = db.Column(db.String(200), index=True)
    password_hash = db.Column(db.String(128))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    cooperative_id = db.Column(db.Integer, db.ForeignKey('cooperatives.id'))
    profile = db.relationship('Profile', uselist=False,
                              back_populates="employee")
    CRMs = db.relationship('CRM', backref='employee', lazy='dynamic')
    #user_id        = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    #activity_id   = db.relationship('Activity', backref='employee', lazy='dynamic')
    #membership = db.relationship('Department', secondary=subs, backref=db.backref('members', lazy='dynamic'))
    is_admin = db.Column(db.Boolean, default=True)
    is_coop_admin = db.Column(db.Boolean, default=False)
    is_overall = db.Column(db.Boolean, default=False)
    is_invited = db.Column(db.Boolean, default=False)
    is_union = db.Column(db.Boolean, default=False)
    is_ferwacotamo = db.Column(db.Boolean, default=False)
    is_confederation = db.Column(db.Boolean, default=False)
    is_rca = db.Column(db.Boolean, default=False)
    is_manager = db.Column(db.Boolean, default=False)
    is_accountant = db.Column(db.Boolean, default=False)
    is_production_manager = db.Column(db.Boolean, default=False)
    is_super_user = db.Column(db.Boolean, default=False)
    invited_by = db.Column(db.String(200))
    district = db.Column(db.String(200))

    def __repr__(self):
        return '{}'.format(self.username)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


class Product(db.Model):
    """
        Creating a product table..
    """
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(200))
    quantity = db.Column(db.String(200))
    in_date = db.Column(db.String(200))
    status = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Product: {}>'.format(self.name)


class Order(db.Model):
    """
        Creating an orders table.
    """

    __tablename__ = "ordes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    product = db.Column(db.String(200))
    description = db.Column(db.String(200))
    quantity = db.Column(db.String(200))
    in_date = db.Column(db.String(200))
    status = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Order: {}>'.format(self.name)


class Federation(db.Model):
    """
        Creating a federation table.
    """

    __tablename__ = 'federations'

    id = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.String(200))
    code = db.Column(db.String(200))
    name = db.Column(db.String(200))
    certificate = db.Column(db.String(200))
    reg_date = db.Column(db.String(200))
    province = db.Column(db.String(200))
    district = db.Column(db.String(200))
    sector = db.Column(db.String(200))
    activity = db.Column(db.String(200))
    unions = db.relationship('Union', backref="federation", lazy="dynamic")

    def __repr__(self):
        return '<Federation: {}>'.format(self.name)

    """ 
        We will always use this __init__ function to upload excel file 
    """

    def __init__(self, code):
        self.id = id
        self.code = code


class Union(db.Model):
    """
        Creating an union table
    """

    __tablename__ = 'unions'

    id = db.Column(db.Integer, autoincrement=True, nullable=True)
    sno = db.Column(db.String(200))
    code = db.Column(db.String(200))
    name = db.Column(db.String(200))
    certificate = db.Column(db.String(200))
    reg_date = db.Column(db.String(200))
    province = db.Column(db.String(200))
    district = db.Column(db.String(200))
    sector = db.Column(db.String(200))
    activity = db.Column(db.String(200))
    #cooperatives = db.relationship('Department', backref="union", lazy="dynamic")
    federation_id = db.Column(db.Integer, db.ForeignKey('federations.id'))
    email = db.Column(db.String(200), primary_key=True)

    def __repr__(self):
        return '<Union: {}>'.format(self.name)

        """ 
            We will always use this __init__ function to upload excel file  
        """

    def __init__(self, code):
        self.id = id
        self.code = code


class Department(db.Model):
    """
        Create a Department table
    """
    __tablename__ = 'departments'

    id = db.Column(db.Integer, autoincrement=True, nullable=True)
    # General information
    no = db.Column(db.Integer)
    code = db.Column(db.String(200))
    email = db.Column(db.String(200), primary_key=True, unique=True)
    name = db.Column(db.String(200))
    regdate = db.Column(db.String(200))
    certificate = db.Column(db.String(200))
    description = db.Column(db.String(200))
    province = db.Column(db.String(200))
    district = db.Column(db.String(200))
    sector = db.Column(db.String(200))
    cell = db.Column(db.String(200))
    Activity = db.Column(db.String(200))
    coop_type = db.Column(db.String(200))
    category = db.Column(db.String(200))
    field = db.Column(db.String(200))
    # federation_id = db.Column(db.Integer, db.ForeignKey('federations.id'))
    # union_id     = db.Column(db.String(200), db.ForeignKey('unions.email'))
    # Professional information
    started_data = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    starting_share = db.Column(db.Integer)
    share_per_person = db.Column(db.String(200))
    male_members = db.Column(db.String(200))
    female_members = db.Column(db.String(200))
    #email       = db.Column(db.String(200))
    applications = db.relationship(
        'Application', backref='department', lazy='dynamic')
    employees = db.relationship(
        'Employee', backref='department', lazy='dynamic')
    staffs = db.relationship('Staff', backref='department', lazy='dynamic')
    activities = db.relationship(
        'Activity', backref='department', lazy='dynamic')
    roles = db.relationship('Role', backref='department', lazy='dynamic')
    products = db.relationship('Product', backref='department', lazy='dynamic')
    orders = db.relationship('Order', backref='department', lazy='dynamic')
    members = db.relationship('Member', backref='department', lazy='dynamic')
    motos = db.relationship('Moto', backref='motos', lazy='dynamic')
    decisions = db.relationship(
        'Decision', backref='department', lazy='dynamic')
    communications = db.relationship(
        'Communication', backref='department', lazy='dynamic')
    contributions = db.relationship(
        'Contribution', backref='department', lazy='dynamic')
    reports = db.relationship('Report', backref='department', lazy='dynamic')
    howtos = db.relationship('Howto', backref='department', lazy='dynamic')
    links = db.relationship('Link', backref='department', lazy='dynamic')
    trainings = db.relationship(
        'Training', backref='department', lazy='dynamic')
    applytrainings = db.relationship(
        'applyTraining', backref='department', lazy='dynamic')
    files = db.relationship('File', backref='department', lazy='dynamic')
    BankAccounts = db.relationship(
        'BankAccount', backref='department', lazy='dynamic')
    loans = db.relationship('Loan', backref='department', lazy='dynamic')
    notifications = db.relationship(
        'Notification', backref='department', lazy='dynamic')
    intekoRusange = db.relationship(
        'intekoRusange', backref='department', lazy='dynamic')
    inamaUbuyobozi = db.relationship(
        'inamaUbuyobozi', backref='department', lazy='dynamic')
    ubugenzuzi = db.relationship(
        'Ubugenzuzi', backref='department', lazy='dynamic')
    isanduku = db.relationship(
        'Isanduku', backref='department', lazy='dynamic')
    itsinda = db.relationship('Itsinda', backref='amatsinda', lazy='dynamic')
    ubwisazure = db.relationship(
        'UbwisazureEnter', backref='ubwisazure', lazy='dynamic')
    incomecategory = db.relationship(
        'IncomeCategory', backref='incomecategory', lazy='dynamic')
    expensecategory = db.relationship(
        'ExpenseCategory', backref='expensecategory', lazy='dynamic')
    expense = db.relationship('Expense', backref='expense', lazy='dynamic')
    income = db.relationship('Expense', backref='income', lazy='dynamic')
    budget = db.relationship('Budget', backref='budget', lazy='dynamic')
    assetsAccounting = db.relationship(
        'assetsAccounting', backref='assetsaccounting', lazy='dynamic')
    account = db.relationship('Account', backref='account', lazy='dynamic')
    abishyuwe = db.relationship(
        'Abishyuwe', backref='abishyuwe', lazy='dynamic')
    is_active = db.Column(db.Boolean, default=False)

    # Dealing with excel staff here.
    """ We will always use this __init__ function to upload excel file
    def __init__(self, email):
        self.id = id
        self.email = email
    """
    """ That in btn """
    #self.description = description
    #self.employees   = employees

    def __repr__(self):
        return self.email

    """
    Dealing with excel staffs here.

    def __init__(self, no, code, name, certificate, regdate, province, district, sector, activity):
        self.no = no
        self.code = code
        self.name = name
        self.certificate = certificate
        self.regdate = regdate
        self.province = province
        self.district = district
        self.sector = sector
        self.activity = activity

    def __repr__(self):
        return '<Role %r>' % self.name

    """


class Role(db.Model):
    """
        Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role', lazy='dynamic')
    members = db.relationship('Member', backref='role', lazy='dynamic')
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    """
    #Dealing with excel staff here.
    def __init__(self,name):
        self.id = id
        self.name = name
        #self.description = description
        #self.employees   = employees
    """

    def __repr__(self):
        return self.name


class Staff(db.Model):
    """
        Create a Staff table
    """

    __tablename__ = 'staffs'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    nid = db.Column(db.String(60))
    district = db.Column(db.String(60))
    sector = db.Column(db.String(60))
    sex = db.Column(db.String(60))
    yob = db.Column(db.String(60))
    position = db.Column(db.String(60))
    education = db.Column(db.String(60))
    telephone = db.Column(db.String(60))
    email = db.Column(db.String(60))
    monthly_net_salary = db.Column(db.String(60))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    """
    #Dealing with excel staff here.
    def __init__(self,name):
        self.id = id
        self.name = name
        #self.description = description
        #self.employees   = employees
    """

    def __repr__(self):
        return self.first_name + " " + self.last_name


class Activity(db.Model):
    """
        Create an Activity table
    """
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))


class Asset(db.Model):
    """
    Create an Asset table
    """
    __tablename__ = 'Assets'
    id = db.Column(db.Integer, primary_key=True)
    asset_type = db.Column(db.String(60))
    asset_location = db.Column(db.String(60))
    asset_value = db.Column(db.String(60))
    description = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))


# Table for the projects in the cooperative are here.
class Project(db.Model):
    """
    Create a Project table.
    """

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(200))
    starting_date = db.Column(db.String(200))
    ending_date = db.Column(db.String(200))
    description = db.Column(db.String(200))
    duration = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='project', lazy='dynamic')

    def __repr__(self):
        return '<Project: {}>'.format(self.name)


"""
#Table for all products we are having in our cooperative are here.
class Product(db.Model):
        Renaming the table to be plural here
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(200))
    image       = db.String(db.String(200))
    price       = db.Column(db.String(200))
    client_id   = db.Column(db.Integer, db.ForeignKey('clients.id'))

    def __repr__(self):
        return '<Product: {}>'.format(self.name)
"""


class Client(db.Model):
    """
    Create a Client table.
    """

    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    location = db.Column(db.String(200))
    business = db.Column(db.String(200))
    #product  = db.relationship('Product', backref='client', lazy='dynamic')

    def __repr__(self):
        return '<Client: {}>'.format(self.name)


class Application(db.Model):
    """
    Creating an Application table
    """

    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    emailaa = db.Column(db.String(200))
    firstNameaa = db.Column(db.String(200))
    secondNameaa = db.Column(db.String(200))
    othersaa = db.Column(db.String(200))
    Districtaa = db.Column(db.String(200))
    Sectoraa = db.Column(db.String(200))
    Cellaa = db.Column(db.String(200))
    nIdaa = db.Column(db.String(200))
    entryDateaa = db.Column(db.String(200))
    shareaa = db.Column(db.String(200))
    exitDateaa = db.Column(db.String(200))
    umuzunguraaa = db.Column(db.String(200))
    umukonoaa = db.Column(db.String(200))
    genderaa = db.Column(db.String(200))
    dobaa = db.Column(db.String(200))
    phoneaa = db.Column(db.String(200))
    Amashuriaa = db.Column(db.String(200))
    Ubumugaaa = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Application: {}>'.format(self.emailaa)


class Post(db.Model):
    """
    Create a Post table
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship(
        'Category', backref=db.backref('posts', lazy='dynamic'))

    def __repr__(self):
        return '<Post %r>' % self.title

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    """
    Create a Category.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Category %r>' % self.name

    def __init__(self, name):
        self.name = name


class Profile(db.Model):
    """
    Create a Profile table.
    """

    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    # Education columns.
    primary_school = db.Column(db.String(200))
    secondary_school = db.Column(db.String(200))
    university_school = db.Column(db.String(200))
    vocational_school = db.Column(db.String(200))
    # Eperiances.
    exp1 = db.Column(db.String(200))
    exp2 = db.Column(db.String(200))
    exp3 = db.Column(db.String(200))
    # Strengths.
    strn1 = db.Column(db.String(200))
    strn2 = db.Column(db.String(200))
    strn3 = db.Column(db.String(200))
    # Careers.
    car1 = db.Column(db.String(200))
    car2 = db.Column(db.String(200))
    car3 = db.Column(db.String(200))
    # Interest.
    inter1 = db.Column(db.String(200))
    inter2 = db.Column(db.String(200))
    inter3 = db.Column(db.String(200))
    # Location
    district = db.Column(db.String(200))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    employee = db.relationship('Employee', back_populates="profile")

    def __repr__(self):
        return '<Profile: {}>'.format(self.id)

    """
        #Class to create the table of members who located in all coperatives which found in ferwacotamo.
    Email
    Rejected or not? = 1 or 0
    Martuel status
    Province
    Insurance_type
    Ubudehe
    Children
    Language
    nationality (Discuss)
    rular_or_urban
    member_source
    job
    occupation
    """


class Member(db.Model):
    """
    Create a Member table/
    """

    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    sno = db.Column(db.String(200))
    email = db.Column(db.String(200))
    izina_ribanza = db.Column(db.String(200))
    izina_rikurikira = db.Column(db.String(200))
    Ayandi = db.Column(db.String(200))
    zone = db.Column(db.String(200))
    itsinda = db.Column(db.String(200))
    Igitsina = db.Column(db.String(200))
    Indangamuntu = db.Column(db.Integer)
    tariki_yavukiye = db.Column(db.String(200))
    Intara = db.Column(db.String(200))
    Akarere = db.Column(db.String(200))
    Umurenge = db.Column(db.String(200))
    Akagari = db.Column(db.String(200))
    Umudugudu = db.Column(db.String(200))
    tariki_yinjiriye = db.Column(db.String(200))
    umugabane = db.Column(db.Integer)
    Umukono = db.Column(db.String(200))
    nomero_telephone = db.Column(db.String(200))
    Amashuri = db.Column(db.String(200))
    Ubumuga = db.Column(db.String(200))
    Arubatse = db.Column(db.String(200))
    umubare_abana = db.Column(db.String(200))
    icyiciro_ubudehe = db.Column(db.String(200))
    Ubwishingizi = db.Column(db.String(200))
    akazi_akora_muri_koperative = db.Column(db.String(200))
    akazi_akora_ahandi = db.Column(db.String(200))
    ubuso_ahingaho = db.Column(db.String(200))
    ubwoko_igihingwa = db.Column(db.String(200))
    ubuso_ahingaho_ibindi = db.Column(db.String(200))
    ubwoko_igihingwa_kindi = db.Column(db.String(200))
    ubuso_budakoreshwa = db.Column(db.String(200))
    sector = db.Column(db.String(200))
    bank = db.Column(db.String(200))
    
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    #department_union = db.Column(db.String(200), db.ForeignKey('unions.email'))
    users = db.relationship('Umusaruro', backref='member', lazy=True)
    umusarurob = db.relationship(
        'Umusarurob', backref='member', lazy='dynamic')
    inyongeramusaruro = db.relationship(
        'InyongeraMusaruro', backref='member', lazy='dynamic')
    imisanzu = db.relationship('Umusanzu', backref='member', lazy='dynamic')
    ibirarane = db.relationship('Ibirarane', backref='member', lazy='dynamic')
    ibihano = db.relationship('Ibihano', backref='member', lazy='dynamic')
    ibindi = db.relationship('Ibindi', backref='member', lazy='dynamic')
    itsindamember = db.relationship(
        'ItsindaMember', backref='member', lazy='dynamic')
    """ We will always use this __init__ function to upload excel file  """

    def __init__(self, sno):
        self.id = id
        self.sno = sno




    """
    Importing data using this views.
    ================================
    def __init__(self, firstName, secondName, others, District, Sector, Cell, nId, entryDate, share,
                        exitDate, umuzungura, umukono, gender, dob, phone, Amashuri, Ubumuga,
                        dl, plate, owner, ownerPhone,
                        department_id):
        #self.id = id
        self.firstName = firstName
        self.secondName = secondName
        self.others = others
        #if pub_date is None:
            #pub_date = datetime.utcnow()
        #self.pub_date = pub_date
        self.District = District
        self.Sector = Sector
        self.Cell = Cell
        self.nId = nId
        #self.cooperative = cooperative
        self.entryDate = entryDate
        self.share = share
        self.exitDate = exitDate
        self.umuzungura = umuzungura
        self.umukono = umukono
        self.gender = gender
        self.dob = dob
        self.phone = phone
        self.Amashuri = Amashuri
        self.Ubumuga = Ubumuga
        self.dl = dl
        self.plate = plate
        self.owner = owner
        self.ownerPhone = ownerPhone
        self.department_id = department_id
    """

    def __repr__(self):
        return '<Member: {}>'.format(self.id) or u'None'


class Moto(db.Model):
    """
    Create a Moto table.
    """

    __tablename__ = 'motos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    plate = db.Column(db.String(200))
    owner = db.Column(db.String(200))
    owner_tel = db.Column(db.String(200))
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Moto: {}>'.format(self.name)


# Class / Table for notifications to all changes in the database
class Notification(db.Model):
    """
    Create a Notification table for storing all the logs in the system.
    """

    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    action = db.Column(db.String(200))
    done_by = db.Column(db.String(200))
    done_from = db.Column(db.String(200))
    done_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    done_time = db.Column(db.String(200))
    done_to = db.Column(db.String(200))
    effect = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Notification: {}>'.format(self.id)


class Committee(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'committees'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    nid = db.Column(db.String(60))
    district = db.Column(db.String(60))
    sector = db.Column(db.String(60))
    sex = db.Column(db.String(60))
    yob = db.Column(db.String(60))
    committee = db.Column(db.String(60))
    position = db.Column(db.String(60))
    education = db.Column(db.String(60))
    telephone = db.Column(db.String(60))
    email = db.Column(db.String(60))
    monthly_net_salary = db.Column(db.String(60))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    """
    #Dealing with excel staff here.
    def __init__(self,name):
        self.id = id
        self.name = name
        #self.description = description
        #self.employees   = employees
    """

    def __repr__(self):
        return '<Committee: {}>'.format(self.first_name)


class Decision(db.Model):
    """
    Create a Decision table
    """

    __tablename__ = "decisions"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    status = db.Column(db.String(200))
    decision = db.Column(db.String(200))
    owner = db.Column(db.String(200))
    stakeholders = db.Column(db.String(200))
    due_date = db.Column(db.String(200))
    background = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Decision: {}>'.format(self.status)

    def __repr__(self):
        return '<Decision: {}>'.format(self.owner)


class Report(db.Model):
    """
    Create a Report table.
    """
    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    status = db.Column(db.String(200))
    project = db.Column(db.String(200))
    task = db.Column(db.String(200))
    description = db.Column(db.String(200))
    notes = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Report: {}>'.format(self.name)


class Howto(db.Model):
    """
    Create a howto table
    """
    __tablename__ = "howtos"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(200))
    labels = db.Column(db.String(200))
    description = db.Column(db.String(200))
    steps = db.Column(db.String(200))
    file = db.Column(db.String(200))
    #background      = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Howto: {}>'.format(self.name)


class Link(db.Model):
    """
    Create a Link table.
    """

    __tablename__ = "links"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    link = db.Column(db.String(200))
    title = db.Column(db.String(200))
    labels = db.Column(db.String(200))
    sharewith = db.Column(db.String(200))
    comment = db.Column(db.String(200))
    #background      = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Link: {}>'.format(self.title)


class File(db.Model):
    """
        Create a File table.
    """

    __tablename__ = "files"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(200))
    #background      = db.Column(db.String(200))
    image_filename = db.Column(db.String(200), default=None, nullable=True)
    image_url = db.Column(db.String(200), default=None, nullable=True)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Link: {}>'.format(self.title)


# All the tables (models) for the coop admin's activities.
# Table for the decisions
class Communication(db.Model):
    """
    Create communication table.
    """

    __tablename__ = "communications"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    message = db.Column(db.String(200))
    ms_from = db.Column(db.String(200))
    comment = db.Column(db.String(200))
    to = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Communication: {}>'.format(self.message)


class Contribution(db.Model):
    """
    Create a Contribution table.
    """

    __tablename__ = "contributions"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    owner = db.Column(db.String(200))
    contributionFor = db.Column(db.String(200))
    amount = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    comment = db.Column(db.String(200))
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Contribution: {}>'.format(self.owner)


class BankAccount(db.Model):
    """
    Create a BankAccount table.
    """

    __tablename__ = "bankaccounts"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    memberId = db.Column(db.String(200))
    memberName = db.Column(db.String(200))
    bankAccountNumber = db.Column(db.String(200))
    accountType = db.Column(db.String(200))
    amount = db.Column(db.String(200))
    date = db.Column(db.String(200))
    #background      = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<BankAccount: {}>'.format(self.memberName)


class Loan(db.Model):
    """
    Create a Loan table
    """

    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    memberId = db.Column(db.String(200))
    memberName = db.Column(db.String(200))
    introducer1Id = db.Column(db.String(200))
    introducer1Name = db.Column(db.String(200))
    introducer1BankAccountBalance = db.Column(db.String(200))
    introducer1Share = db.Column(db.String(200))
    introducer2Id = db.Column(db.String(200))
    introducer2Name = db.Column(db.String(200))
    introducer2BankAccountBalance = db.Column(db.String(200))
    introducer2Share = db.Column(db.String(200))
    loanAmount = db.Column(db.String(200))
    interestRate = db.Column(db.String(200))
    durationInDay = db.Column(db.String(200))
    remarksIfAny = db.Column(db.String(200))
    loanType = db.Column(db.String(200))
    totalLoanWithInterest = db.Column(db.String(200))
    activedBy = db.Column(db.String(200))
    loanIssueDate = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Loan: {}>'.format(self.memberName)


class fixedDepositAccount(db.Model):
    """
    Class to create the table of members who located in all 
    coperatives which found in ferwacotamo.
    """
    __tablename__ = "fixeddepositaccounts"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    memberId = db.Column(db.String(200))
    memberName = db.Column(db.String(200))
    fixedDepositAmount = db.Column(db.String(200))
    durationInDay = db.Column(db.String(200))
    fixedDepositInterest = db.Column(db.String(200))
    maturityDate = db.Column(db.String(200))
    matureAmount = db.Column(db.String(200))
    createdBy = db.Column(db.String(200))
    date = db.Column(db.String(200))
    #department_id = db.Column(db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<fixedDepositAccount: {}>'.format(self.memberName)


class Transaction(db.Model):
    """
    Class to create the table of members who located in all 
    coperatives which found in ferwacotamo.
    """

    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    bankAccountNumber = db.Column(db.String(200))
    memberName = db.Column(db.String(200))
    accountType = db.Column(db.String(200))
    depositOrWithdraw = db.Column(db.String(200))
    cashOrCheque = db.Column(db.String(200))
    amount = db.Column(db.String(200))
    balance = db.Column(db.String(200))
    date = db.Column(db.String(200))
    #department_id = db.Column(db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Transaction: {}>'.format(self.memberName)


class Share(db.Model):
    """
    Model of table for Share Account Transaction
    """

    __tablename__ = "shares"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    memberId = db.Column(db.String(200))
    shareAccNo = db.Column(db.String(200))
    memberName = db.Column(db.String(200))
    depositOrWithdraw = db.Column(db.String(200))
    shareAmount = db.Column(db.String(200))
    balanceShare = db.Column(db.String(200))
    date = db.Column(db.String(200))
    #department_id = db.Column(db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Share: {}>'.format(self.memberName)


class Installment(db.Model):
    """
    Model for table of Installememt payments transactions.
    """

    __tablename__ = "installments"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    memberId = db.Column(db.String(200))
    loanId = db.Column(db.String(200))
    memberName = db.Column(db.String(200))
    lastInstallmentPay = db.Column(db.String(200))
    lastInstallmentPayDate = db.Column(db.String(200))
    cashOrCheque = db.Column(db.String(200))
    payLoanInstallment = db.Column(db.String(200))
    balance = db.Column(db.String(200))
    date = db.Column(db.String(200))
    remarksIfAny = db.Column(db.String(200))
    #department_id = db.Column(db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Installment: {}>'.format(self.memberName)


class Payment(db.Model):
    """
    Create a Payment table to store all the finished payments for members
    """

    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    reason = db.Column(db.String(200))
    amount = db.Column(db.String(200))
    date = db.Column(db.String(200))

    def __repr__(self):
        return '<Payment: {}>'.format(self.reason)


class intekoRusange(db.Model):
    """
    Creating table for recording all general 
    assembly meetings' resolutions.
    """

    __tablename__ = "intekorusange"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    status1 = db.Column(db.String(200))
    decision1 = db.Column(db.String(200))
    owner1 = db.Column(db.String(200))
    stakeholders1 = db.Column(db.String(200))
    due_date1 = db.Column(db.String(200))
    background1 = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<intekoRusange: {}>'.format(self.status)

    def __repr__(self):
        return '<intekoRusange: {}>'.format(self.owner)


class inamaUbuyobozi(db.Model):
    """
    Creating a table for recording all 
    the committee's meeting resolutions.
    """

    __tablename__ = "inamaubuyobozi"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    status = db.Column(db.String(200))
    decision = db.Column(db.String(200))
    owner = db.Column(db.String(200))
    stakeholders = db.Column(db.String(200))
    due_date = db.Column(db.String(200))
    background = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<inamaUbuyobozi: {}>'.format(self.status)

    def __repr__(self):
        return '<inamaUbuyobozi: {}>'.format(self.owner)


class Ubugenzuzi(db.Model):
    """
    Creating a table for auditing 
    committee meeting resolutions.
    """

    __tablename__ = "ubugenzuzi"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    status = db.Column(db.String(200))
    decision = db.Column(db.String(200))
    owner = db.Column(db.String(200))
    stakeholders = db.Column(db.String(200))
    due_date = db.Column(db.String(200))
    background = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Ubugenzuzi: {}>'.format(self.status)

    def __repr__(self):
        return '<Ubugenzuzi: {}>'.format(self.owner)


# Isanduku model.
class Isanduku(db.Model):
    """
    Creating a table for cooperative internal 
    box for petty cash.
    """
    __tablename__ = "isanduku"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    no = db.Column(db.Integer)
    done_date = db.Column(db.String(200))
    action = db.Column(db.String(200))
    income = db.Column(db.Integer)
    expense = db.Column(db.Integer)
    remain = db.Column(db.String(200))
    done_by = db.Column(db.String(200))
    done_to = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Isanduku: {}>'.format(self.action)

    def __repr__(self):
        return '<Isanduku: {}>'.format(self.action)


"""
class Umusaruro(db.Model):
    # Creating table for recording the cooperative's harvest.

    __tablename__ = "umusaruro"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    Amazina = db.Column(db.String(200))
    Taliki = db.Column(db.String(200))
    Uwagemuye = db.Column(db.String(200))
    Ibiro    = db.Column(db.String(200))
    Igiciro = db.Column(db.String(200))
    IkiguziCyose = db.Column(db.String(200))
    amafarangaYishyuweKuKiro   = db.Column(db.String(200))
    done_by   = db.Column(db.String(200))
    done_to   = db.Column(db.String(200))
    on_market = db.Column(db.Boolean, default=False)
    department_id = db.Column(db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Umusaruro: {}>'.format(self.Amazina)
"""


class Goal(db.Model):
    """
    Creating a table for goals/plans of cooperative in a given time
    """

    __tablename__ = "goals"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(200))
    Description = db.Column(db.String(200))
    Amount = db.Column(db.String(200))
    startingDate = db.Column(db.String(200))
    endingDate = db.Column(db.String(200))
    paidMembers = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Goal: {}>'.format(self.name)


# Umusaruro models.
class ibitaboByaBank(db.Model):
    """
    Creating a table for all accounting books 
    related to Bank within a cooperative.
    """

    __tablename__ = "ibitabobyabanks"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    no = db.Column(db.String(200))
    date = db.Column(db.String(200))
    igikorwa = db.Column(db.String(200))
    debit = db.Column(db.String(200))
    credit = db.Column(db.String(200))
    solde = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<ibitaboBank: {}>'.format(self.igikorwa)


class Training(db.Model):
    """
    Creating a table for recording all contents that is 
    to provided as training to cooperative's staff or members.
    """

    __tablename__ = "trainings"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    trainer = db.Column(db.String(200))
    about = db.Column(db.String(200))
    description = db.Column(db.String(200))
    date = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=False)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__():
        return '<Training: {}>'.format(self.name)


class applyTraining(db.Model):
    """
    Creating a table that allow members or staff of the cooperative
    to apply for the training about any topic they need.
    """

    __tablename__ = "applytrainings"

    id = db.Column(db.Integer, primary_key=True)
    namea = db.Column(db.String(200))
    abouta = db.Column(db.String(200))
    descriptiona = db.Column(db.String(200))
    datea = db.Column(db.String(200))
    is_activea = db.Column(db.Boolean, default=False)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__():
        return '<applyTraining: {}>'.format(self.name)


class Umusaruro(db.Model):
    """ 
    Createing a table to track and record all the harvest
    of members within the cooperative on the daily basis.
    """

    __tablename__ = "umusaruro"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    amazina = db.Column(db.String(100))
    resi = db.Column(db.Integer)
    zone = db.Column(db.String(100))
    group = db.Column(db.String(100))
    umusaruro = db.Column(db.Integer)
    umuceriYagurijwe = db.Column(db.Integer)
    umuceriWoKurya = db.Column(db.Float)
    umuceriWoKugurisha = db.Column(db.Integer)
    igiciroCyaKimwe = db.Column(db.Integer)
    umusanzu = db.Column(db.Integer)
    amafarangaYose = db.Column(db.Integer)
    amafarangaYoGutonoza = db.Column(db.Integer)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    umwakaWisarura = db.Column(db.String(50))

    def __repr__(self):
        return '<Umusaruro: {}>'.format(self.amazina)


"""
class Inyongeramusaruro(db.Model):
    # Creating a table to track and record all the
    # Imputs that are being used by members within
    # The cooperative, periodically.

    docstring for Inyongeramusaruro
    __tablename__ = "inyongeramusaruro"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amazina = db.Column(db.String(200))
    BriqueteUnity = db.Column(db.Float)
    BriquetePU = db.Column(db.Integer)
    DapAndNPKUnity = db.Column(db.Float)
    DapAndNPKpu = db.Column(db.Integer)
    KCLUnity = db.Column(db.Float)
    KCLpu = db.Column(db.Integer)
    ImbutoIngano = db.Column(db.Float)
    ImbutoPU = db.Column(db.Integer)
    RedevanceUbuso = db.Column(db.Float)
    RedevancePU = db.Column(db.Integer)
    ImifukaAgaciro = db.Column(db.Integer)
    ImifukaYishyuwe = db.Column(db.Integer)
    umusaruro_resi = db.Column(db.Integer, unique=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    department_id = db.Column(db.String(200), db.ForeignKey('departments.email'))
    umwakaWisarura = db.Column(db.String(50))

    def __repr__(self):
        return '<Inyongeramusaruro: {}>'.format(self.id)
"""


class Ibyakoreshejwe(db.Model):
    """
    Creating a table for recording all the investments that were
    made by the members to grow their products or to
    generate any other income in a given timeframe.
    """

    __tablename__ = "ibyakoreshejwe"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amazina = db.Column(db.String(200))
    deamAndSup = db.Column(db.Integer)
    ibihanoCoop = db.Column(db.Integer)
    APKSAMAKIbihano = db.Column(db.Integer)
    ibiraraneNPKandUREA = db.Column(db.Integer)
    umusoroWakarere = db.Column(db.Integer)
    kwishyuraItsinda = db.Column(db.Integer)
    sheeting = db.Column(db.Integer)
    PandS = db.Column(db.Integer)
    ibyoYagurijwe = db.Column(db.Integer)
    ibindiYasbwe = db.Column(db.Integer)
    umusaruro_resi = db.Column(db.Integer)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Ibyakoreshejwe: {}>'.format(self.id)


class CoopMemberBankAccounts(db.Model):
    """
    Creating a teble of members of the cooperative to store
    their bank account numbers so that they can be used in case
    of any transaction that concern them.
    """

    __tablename__ = "coopMemberBankAccounts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    memberName = db.Column(db.String(100))
    bankName = db.Column(db.String(50), unique=True)
    bankAccountNumber = db.Column(db.String(50), unique=True)
    umusaruro_resi = db.Column(db.Integer)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<CoopMemberBankAccounts: {}>'.format(self.id)


# New models related to the stack of rice cooperatives.
# We have already done with this table in the database, we just need to add the relevant information
class Umusarurob(db.Model):
    """ 
    Creating a table to track the hardvest that is sent
    to the cooperative by members on the daily basis.
    """

    __tablename__ = "umusarurob"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    RiceType = db.Column(db.String(100))
    UmusaruroGrade = db.Column(db.String(200))
    RicePrice      = db.Column(db.Float)
    RiceAmount = db.Column(db.Integer)
    UwoAsigaranye = db.Column(db.Float)
    UwoKugurisha = db.Column(db.Integer)  # Quantity - Umu asigaranye
    GutonozaAmount = db.Column(db.Integer)
    # (RiceAmount * Quantity) - Uwogutonoza
    AmafarangaUmusaruro1 = db.Column(db.Integer)
    Asigaye = db.Column(db.Float)
    Ibikase = db.Column(db.Integer)
    Ibisigaye = db.Column(db.Integer)

    Musa = db.Column(db.Integer)
    Carnet = db.Column(db.Integer)
    Avance = db.Column(db.Integer)
    


    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    done_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    abishyuwe = db.relationship(
        'Abishyuwe', backref='abishyuwee', lazy='dynamic')

    def __repr__(self):
        return '<Umusarurob: {}>'.format(self.id)


#
class InyongeraMusaruro(db.Model):
    """
    Creating the table which will record all the information 
    related to the fertilizers used to grow the rice by the farmer
    """
    __tablename__ = "inyongeramusaruro"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NPKkg = db.Column(db.Integer)
    NPKPerUnity = db.Column(db.Integer)
    UREA = db.Column(db.Integer)
    UREAPerUnity = db.Column(db.Integer)
    DAP = db.Column(db.Integer)
    DAPPerUnity = db.Column(db.Integer)
    KCL = db.Column(db.Integer)
    KCLPerUnity = db.Column(db.Integer)
    Briquette = db.Column(db.Integer)
    BriquettePerUnity = db.Column(db.Integer)
    Cypemetrine = db.Column(db.Float)
    Beam = db.Column(db.Integer)
    ImbutoQuantity = db.Column(db.Float)
    ImbutoAmount = db.Column(db.Integer)
    Redevance = db.Column(db.Float)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    #umwakaWisarura = db.Column(db.String(50))
    done_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<InyongeraMusaruro: {}>'.format(self.id)


class Umusanzu(db.Model):
    """
    Creating the table which will record all the information related 
    to the contributions that membes give to their cooperative after
    any given season.
    """

    __tablename__ = "umusanzu"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UmusoroWakarere = db.Column(db.Integer)
    UmusanzuCoop = db.Column(db.Integer)
    Umugabane = db.Column(db.Integer)
    Ikigega = db.Column(db.Integer)
    KuzibaIcyuho = db.Column(db.Integer)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    done_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Umusanzu: {}>'.format(self.id)


class Ibirarane(db.Model):
    """
    Creating the table which will record all the information related 
    to the loans that membes had took from their cooperative during
    the growing season.
    """

    __tablename__ = "ibirarane"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NPKkg = db.Column(db.Integer)
    NPKPerUnity = db.Column(db.Integer)
    UREA = db.Column(db.Integer)
    UREAPerUnity = db.Column(db.Integer)
    DAP = db.Column(db.Integer)
    DAPPerUnity = db.Column(db.Integer)
    KCL = db.Column(db.Integer)
    KCLPerUnity = db.Column(db.Integer)
    ImbutoQuantity = db.Column(db.Float)
    ImbutoAmount = db.Column(db.Integer)
    IdeniAmount = db.Column(db.Integer)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    done_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    Briquette = db.Column(db.Integer)
    BriquettePerUnity = db.Column(db.Integer)

    def __repr__(self):
        return '<Ibirarane: {}>'.format(self.id)


class Ibihano(db.Model):
    """
    Creating the table which will record all the information related 
    to the penalties that membes were given by their cooperative for
    for different misconducts.
    """
    __tablename__ = "ibihano"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    AmandeC = db.Column(db.String(200))
    AmandeApII = db.Column(db.Integer)
    comment = db.Column(db.String(200))
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    done_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Ibihano: {}>'.format(self.id)


class Ibindi(db.Model):
    """
    Creating the table which will record all other different information about
    the items that were used by members of coopeative during the season.
    """

    __tablename__ = "ibindi"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ImifukaQuantity = db.Column(db.Integer)
    ImifukaAmount = db.Column(db.Integer)

    rpf = db.Column(db.Integer)
    ejo_heza = db.Column(db.Integer)
    mituelle_amount = db.Column(db.Integer)
    carnet = db.Column(db.Integer)
    avance = db.Column(db.Integer)
    loan = db.Column(db.Integer)



    UmuceriGrade = db.Column(db.String(200))
    UmuceriQuantity = db.Column(db.Integer)
    UmuceriAmountGrade = db.Column(db.Integer)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    done_date = db.Column(db.DateTime)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Ibindi: {}>'.format(self.id)


class Itsinda(db.Model):
    """
    Creating the table which will allow the cooperative management
    to create different groups and zones within the members of 
    the cooperative and arrange them through those zone and groups.
    """

    __tablename__ = "amatsinda"

    id = db.Column(db.Integer, primary_key=True)
    itsinda_name = db.Column(db.String(200))
    description = db.Column(db.String(200))
    purpose = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    itsindamember = db.relationship(
        'ItsindaMember', backref='Itsinda', lazy='dynamic')

    def __repr__(self):
        return '<Itsinda: {}>'.format(self.id)


class ItsindaMember(db.Model):
    """
    Creating the table which will allow the cooperative management
    to add members and manage them with their zones and groups, respectively.
    """

    __tablename__ = "itsindamember"

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(
        db.Integer, db.ForeignKey('members.id'), unique=False)
    itsinda_id = db.Column(db.Integer, db.ForeignKey('amatsinda.id'))
    member_firstname = db.Column(db.String(200))
    member_secondname = db.Column(db.String(200))
    itsinda_name = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<ItsindaMember: {}>'.format(self.id)


class IsandukuNshya(db.Model):
    """
    Creating the table which will allow the cooperative management
    to create internal account for managing financials.
    """

    __tablename__ = "isandukunshya"

    id = db.Column(db.Integer, primary_key=True)
    ayinjiye = db.Column(db.Integer)
    ayasohotse = db.Column(db.Integer)
    asigaye = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    rukomatanyo_id = db.Column(db.Integer, db.ForeignKey('rukomatanyo.id'))

    def __repr__(self):
        return '<IsandukuNshya: {}>'.format(self.id)


class BankModel(db.Model):
    """
    Creating the table which allow the cooperative management
    to create bank account for managing financial transactions
    with the cooperative.
    """

    __tablename__ = "bank"

    id = db.Column(db.Integer, primary_key=True)
    ayinjiye = db.Column(db.Integer)
    ayasohotse = db.Column(db.Integer)
    asigaye = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    rukomatanyo_id = db.Column(db.Integer, db.ForeignKey('rukomatanyo.id'))

    def __repr__(self):
        return '<BankModel: {}>'.format(self.id)


class InguzanyoZatanzwe(db.Model):
    """
    Creating the table which allow the cooperative management
    to record and track all the loans that were given to the
    members of the cooperative in any given time.
    """

    __tablename__ = "InguzanyoZatanzwe"

    id = db.Column(db.Integer, primary_key=True)
    ayinjiye = db.Column(db.Integer)
    ayasohotse = db.Column(db.Integer)
    asigaye = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    rukomatanyo_id = db.Column(db.Integer, db.ForeignKey('rukomatanyo.id'))

    def __repr__(self):
        return '<InguzanyoZatanzwe: {}>'.format(self.id)


class Ibiramba(db.Model):
    """
    Creating the table which allow the cooperative management
    to record all the fixed assets of the cooperative and keep
    them on track.
    """

    __tablename__ = "ibiramba"

    id = db.Column(db.Integer, primary_key=True)
    ayinjiye = db.Column(db.Integer)
    ayasohotse = db.Column(db.Integer)
    asigaye = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    rukomatanyo_id = db.Column(db.Integer, db.ForeignKey('rukomatanyo.id'))

    def __repr__(self):
        return '<Ibiramba: {}>'.format(self.id)


class Ububiko(db.Model):
    """
    Creating the table which allow the cooperative management
    to create the internal stock of the cooperatives for managing
    different transactions.
    """

    __tablename__ = "ububiko"

    id = db.Column(db.Integer, primary_key=True)
    ayinjiye = db.Column(db.Integer)
    ayasohotse = db.Column(db.Integer)
    asigaye = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    rukomatanyo_id = db.Column(db.Integer, db.ForeignKey('rukomatanyo.id'))

    def __repr__(self):
        return '<Ububiko: {}>'.format(self.id)


class UmugabaneShingiro(db.Model):
    """
    Creating the table which will allow the cooperative
    to collect and track the payment of the share capital from members.
    """

    __tablename__ = "umugabaneShingiro"

    id = db.Column(db.Integer, primary_key=True)
    ayinjiye = db.Column(db.Integer)
    ayasohotse = db.Column(db.Integer)
    asigaye = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    rukomatanyo_id = db.Column(db.Integer, db.ForeignKey('rukomatanyo.id'))

    def __repr__(self):
        return '<UmugabaneShingiro: {}'.format(self.id)


class Inkunga(db.Model):
    """
    Creating the table which allow the cooperative to collect 
    and track the grants or funds that are coming from different
    stakeholders.
    """

    __tablename__ = "inkunga"

    id = db.Column(db.Integer, primary_key=True)
    ayinjiye = db.Column(db.Integer)
    ayasohotse = db.Column(db.Integer)
    asigaye = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    rukomatanyo_id = db.Column(db.Integer, db.ForeignKey('rukomatanyo.id'))

    def __repr__(self):
        return '<Inkunga: {}'.format(self.id)


class InguzanyoZabandi(db.Model):
    """
    Creating the table which allow the cooperative
    to record all the loans that it owe other people
    or institutions like banks or factories / processors.
    """

    __tablename__ = "inguzanyozabandi"

    id = db.Column(db.Integer, primary_key=True)
    ayinjiye = db.Column(db.Integer)
    ayasohotse = db.Column(db.Integer)
    asigaye = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    rukomatanyo_id = db.Column(db.Integer, db.ForeignKey('rukomatanyo.id'))

    def __repr__(self):
        return '<InguzanyoZabandi: {}'.format(self.id)


class Ibicuruzwa(db.Model):
    """
    Creating the table which allow the cooperative to record
    all information related to the products it has or it is
    selling.
    """

    __tablename__ = "ibicuruzwa"

    id = db.Column(db.Integer, primary_key=True)
    ayinjiye = db.Column(db.Integer)
    ayasohotse = db.Column(db.Integer)
    asigaye = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    rukomatanyo_id = db.Column(db.Integer, db.ForeignKey('rukomatanyo.id'))

    def __repr__(self):
        return '<Ibicuruzwa: {}'.format(self.id)


class IkoreshwaRyimari(db.Model):
    """
    Creating the table which allow the cooperative
    to record and manage how the fund is being used
    with the cooperative periodically.
    """

    __tablename__ = "ikoreshwaRyimari"

    id = db.Column(db.Integer, primary_key=True)
    ayinjiye = db.Column(db.Integer)
    ayasohotse = db.Column(db.Integer)
    asigaye = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    rukomatanyo_id = db.Column(db.Integer, db.ForeignKey('rukomatanyo.id'))

    def __repr__(self):
        return '<IkoreshwaRyimari: {}'.format(self.id)


class IbindiRukomatanyi(db.Model):
    """
    Creating the table which allow the cooperative
    to record all other different financial transactions
    with the cooperative, unexpectedly.
    """

    __tablename__ = "ibindiRukomatanya"

    id = db.Column(db.Integer, primary_key=True)
    ayinjiye = db.Column(db.Integer)
    ayasohotse = db.Column(db.Integer)
    asigaye = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    rukomatanyo_id = db.Column(db.Integer, db.ForeignKey('rukomatanyo.id'))

    def __repr__(self):
        return '<IbindiRukomatanyi: {}'.format(self.id)


class Zone(db.Model):
    """
    Creating the table which allow the cooperative
    to create and manage members within different zones.
    """

    __tablename__ = "zones"

    id = db.Column(db.Integer, primary_key=True)
    izina = db.Column(db.String(100))
    ubusobanuro = db.Column(db.String(200))
    impamvu = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))
    rukomatanyo_id = db.Column(db.Integer, db.ForeignKey('rukomatanyo.id'))

    def __repr__(self):
        return '<Zone: {}>'.format(self.id)


class Rukomatanyo(db.Model):
    """
    Creating the table which combine all other tables
    that record all the different accounts within the
    cooperative and balance them in one table.
    """

    __tablename__ = "rukomatanyo"

    id = db.Column(db.Integer, primary_key=True)
    tariki_byakozwe = db.Column(db.Date, default=datetime.datetime.utcnow())
    description = db.Column(db.String(200))
    piyesi = db.Column(db.String(200))
    zone = db.relationship('Zone', backref='rukomatanyo', lazy='dynamic')
    ibindiRukomatanya = db.relationship(
        'IbindiRukomatanyi', backref='rukomatanyo', lazy='dynamic')
    isanduku = db.relationship(
        'IsandukuNshya', backref='rukomatanyo', lazy='dynamic')
    ikoreshwaRyimari = db.relationship(
        'IkoreshwaRyimari', backref='rukomatanyo', lazy='dynamic')
    ibicuruzwa = db.relationship(
        'Ibicuruzwa', backref='rukomatanyo', lazy='dynamic')
    inguzanyozabandi = db.relationship(
        'InguzanyoZabandi', backref='rukomatanyo', lazy='dynamic')
    inkunga = db.relationship('Inkunga', backref='rukomatanyo', lazy='dynamic')
    umugabaneShingiro = db.relationship(
        'UmugabaneShingiro', backref='rukomatanyo', lazy='dynamic')
    ibiramba = db.relationship(
        'Ibiramba', backref='rukomatanyo', lazy='dynamic')
    ububiko = db.relationship('Ububiko', backref='rukomatanyo', lazy='dynamic')
    InguzanyoZatanzwe = db.relationship(
        'InguzanyoZatanzwe', backref='rukomatanyo', lazy='dynamic')
    bank = db.relationship('BankModel', backref='rukomatanyo', lazy='dynamic')
    isanduku = db.relationship(
        'IsandukuNshya', backref='rukomatanyo', lazy='dynamic')
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))


class UbwisazureEnter(db.Model):
    """
    Creating the table which allow the cooperative
    to record and manage the depreciation of the cooperative's
    properties.
    """

    __tablename__ = "ubwisazures"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    AssetDescription = db.Column(db.String(200))
    cost = db.Column(db.Integer)
    YearOfPurchase = db.Column(db.String(200))
    SalvageValue = db.Column(db.Integer)
    UsefulLife = db.Column(db.String(200))
    Method = db.Column(db.String(200))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Ubwisazure: {}>'.format(self.id)


"""
These are models related to accounting operations.
We have already built Rukomatanyi, but in some ways the Rukomatanyi
Does not meet some accounting standards, so that's why
We got to add some accounting prenciples in the system.
"""


class IncomeCategory(db.Model):
    """
    Creating the table which allow the cooperative
    to create different categories of their income.
    """
    __tablename__ = "incomecategory"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    Category = db.Column(db.String(200))
    cooperative_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<IncomeCategory: {}>'.format(self.id)


class ExpenseCategory(db.Model):
    """
    Creating the table which allow the cooperative
    to create different categories of their expenses.
    """

    __tablename__ = "expensecategory"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    AccountName = db.Column(db.String(200))
    cooperative_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<ExpenseCategory: {}>'.format(self.id)


class Expense(db.Model):
    """
    Creating the table which allow the cooperative
    to record and manage expenses that occurs within the
    cooperative, periodically.
    """

    __tablename__ = "expense"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    Title = db.Column(db.String(200))
    Date = db.Column(db.String(200))
    Category = db.Column(db.String(200))
    Account = db.Column(db.String(200))
    Amount = db.Column(db.String(200))
    Desciption = db.Column(db.String(200))
    cooperative_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Expense: {}>'.format(self.id)


class Income(db.Model):
    """
    Creating the table which allow the cooperative
    to record and manage income that occurs within the
    cooperative, periodically.
    """

    __tablename__ = "income"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    Title = db.Column(db.String(200))
    Date = db.Column(db.String(200))
    Category = db.Column(db.String(200))
    Account = db.Column(db.String(200))
    Amount = db.Column(db.String(200))
    Desciption = db.Column(db.String(200))
    cooperative_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Income: {}>'.format(self.id)


class Budget(db.Model):
    """
    Creating the table which allow the cooperative
    to create and manage the budget that will be used
    in a given time.
    """

    __tablename__ = "budget"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    Category = db.Column(db.String(200))
    Date = db.Column(db.String(200))
    Amount = db.Column(db.String(200))
    cooperative_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Budget: {}>'.format(self.id)


class assetsAccounting(db.Model):
    """
    Creating the table which allow the cooperative
    to record and manage it's assets.
    """

    __tablename__ = "assetsaccounting"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    Date = db.Column(db.String(200))
    Category = db.Column(db.String(200))
    Account = db.Column(db.String(200))
    Amount = db.Column(db.String(200))
    Description = db.Column(db.String(200))
    cooperative_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<assetsAccounting: {}>'.format(self.id)


class Account(db.Model):
    """
    Creating the table which allow the cooperative
    to create different accounts that can be used to
    track all accounting transactions.
    """

    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    AccountName = db.Column(db.String(200))
    Description = db.Column(db.String(200))
    cooperative_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))

    def __repr__(self):
        return '<Account: {}>'.format(self.id)


class Abishyuwe(db.Model):
    """
    Creating the table which allow the cooperative
    to record and manage all payments of it's members.
    """

    __tablename__ = "abishyuwe"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    amount_payed = db.Column(db.Integer)
    member_id = db.Column(db.Integer)
    member_name = db.Column(db.String(200))
    ibiro = db.Column(db.Float)
    done_date = db.Column(db.Date, default=datetime.datetime.utcnow())
    umusaruro_id = db.Column(db.Integer, db.ForeignKey('umusarurob.id'))
    department_id = db.Column(
        db.String(200), db.ForeignKey('departments.email'))


class CRM(db.Model):
    """
    Creating the table which allow the cooperative
    to record and manage all of it's customers, 
    => Customer Relationship Management.
    """
    __tablename__ = "CRMs"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    # cooperative_id = db.Column(db.Integer, db.ForeignKey('cooperatives.id'))
    tag = db.Column(db.String(100))
    company_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    website = db.Column(db.String(100))
    address = db.Column(db.String(200))
    contact_type = db.Column(db.String(200))
    phone_number = db.Column(db.String(100))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    description = db.Column(db.String(255))
    status = db.Column(db.String(100))



class Arc_stock(db.Model):
    """
    Creating the table which allow the cooperative
    to record and manage the previous stock data they collected
    using different tools like excel, before joining the AICOS platform.
    """
    __tablename__ = "arc_stock"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    nimero	= db.Column(db.Integer)
    date	= db.Column(db.String(255))
    izina_ribanza = db.Column(db.String(255))
    izina_rikurikira = db.Column(db.String(255))
    ubwoko	         = db.Column(db.String(255))
    ingano_kg	     = db.Column(db.String(255))
    igiciro_kg	     = db.Column(db.String(255))
    igiciro_cya_byose	= db.Column(db.String(255))
    umusanzu_koperative	= db.Column(db.String(255))
    ayishyurwa_umuhinzi	= db.Column(db.String(255))
    telefoni            = db.Column(db.String(255))
    season              = db.Column(db.String(255))
    department_id = db.Column(
            db.String(200), db.ForeignKey('departments.email'))
				 	














class Arc_cooperative(db.Model):
    """
    Creating the table which allow the cooperatives 
    which registered before the AICOS platform 
    to stored in the platform too
    """
    __tablename__ = "arc_cooperatives"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    sno	= db.Column(db.Integer)
    cooperative_name	= db.Column(db.String(255))
    code	= db.Column(db.String(255))
    certificate = db.Column(db.String(255))
    activity = db.Column(db.String(255))
    reg_date	         = db.Column(db.String(255))
    province	     = db.Column(db.String(255))
    district	     = db.Column(db.String(255))
    sector         	 = db.Column(db.String(255))
    male_members   	 = db.Column(db.String(255))
    female_members	 = db.Column(db.String(255))
    total_members    = db.Column(db.String(255))
    capital          = db.Column(db.String(255))
    share_person     = db.Column(db.String(255))
    president_and_contact = db.Column(db.String(255))
    status_rca       = db.Column(db.String(255))









class Temp_coopthevigi(db.Model):
    """
    Creating the table which allow the cooperatives 
    which registered before the AICOS platform 
    to stored in the platform too
    """
    __tablename__ = "temp_coopthevigi"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    Code = db.Column(db.Integer)
    Amazina	= db.Column(db.String(255))
    Ibiro = db.Column(db.Float)
    Igiciro = db.Column(db.Float)

    Quality = db.Column(db.Float)
    Avance  = db.Column(db.Float)
    Musa = db.Column(db.Integer)
    Asigaye  = db.Column(db.Float)

    Telephone	= db.Column(db.String(255))
    Status = db.Column(db.Boolean, default=False)
