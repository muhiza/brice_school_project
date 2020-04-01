"""
This file is used to setup the Flask Application.
"""

# System imports
import os
# third-parties imports
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, current_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, redirect, url_for
import flask_excel

import flask_excel as excel
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_restful import reqparse
from flask import Flask, request, jsonify, redirect, url_for
import flask_excel
import flask_excel as excel
from flask_sqlalchemy import SQLAlchemy # sql operations

from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_restless import APIManager
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
#from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

flask_excel.init_excel(app)

#Configuring the database path
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://juru:Password@123@localhost/aicos'
# app.config['SQLALCHEMY_BINDS'] = {'test':'mysql://juru:Password@123@localhost/test'}
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# Configuring the recaptha variables for user login checkings.
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LdYIDcUAAAAAEE3N3tNqcYu50MJSTlGA5lwu5Pl'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LdYIDcUAAAAAD8ayN_2Mkhauh_-MdK12XxdTLEo'

db = SQLAlchemy(app)  
api = Api(app)
#manager = APIManager(app, flask_sqlalchemy_db=db)

# Configure the image uploading via Flask-Uploads
images = UploadSet('images', IMAGES)

# local imports
#from config import app_config

# Initiating the database instance.
db = SQLAlchemy()

# Initiating the user management instance.
login_manager = LoginManager()


# Creating the application factory to help in initiating and
# Manage all other different functions and instances.
def create_app(config_name, *args):
    if os.getenv('FLASK_CONFIG') == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
        
    else:
        app = Flask(__name__, instance_relative_config=True)
        # app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py')

    # Import all models
    from .models import Member, Department, Umusarurob, InyongeraMusaruro, Employee, Role, Notification, Umusanzu, Ibirarane, Ibihano, Ibindi, Itsinda, ItsindaMember, IsandukuNshya, BankModel, InguzanyoZatanzwe, Ibiramba, Ububiko, UmugabaneShingiro, Inkunga, InguzanyoZabandi, Ibicuruzwa, IkoreshwaRyimari, IbindiRukomatanyi, Zone, Rukomatanyo, UbwisazureEnter

    from .models import CRM

    # A class to help in access the employees view flask admin extension.
    class EmployeeView(ModelView):
        form_columns = ['email', 'username', 'first_name', 'last_name', 'department_id', 'phone_number']

    class MyModelView(ModelView):
        def is_accessible(self):
            return current_user.is_authenticated
        def inaccessible_callback(self, name, **kwags):
            return redirect(url_for('auth.login'))

    class MyAdminIndexView(AdminIndexView):
        def is_accessible(self):
            return current_user.is_authenticated

        can_edit = True
        edit_modal = True
        create_modal = True    
        can_export = True
        can_view_details = True
        details_modal = True


    # Class to retrieve and diplay different models with their information.
    # To users via the flask admin extension.
    class CustomView(BaseView):
        @expose('/')
        def index(self):
            return self.render('admin/custom_index.html')

    admin = Admin(app, name='aicos_admin', base_template='my_master.html', template_mode='bootstrap3', index_view=MyAdminIndexView())
    admin.add_view(MyModelView(Member, db.session))
    admin.add_view(MyModelView(Department, db.session))
    admin.add_view(MyModelView(Umusarurob, db.session))
    admin.add_view(MyModelView(InyongeraMusaruro, db.session))
    admin.add_view(MyModelView(Employee, db.session))
    admin.add_view(MyModelView(Rukomatanyo, db.session))
    admin.add_view(MyModelView(BankModel, db.session))
    admin.add_view(MyModelView(Ibirarane, db.session))
    admin.add_view(MyModelView(Umusanzu, db.session))
    admin.add_view(MyModelView(Ibihano, db.session))
    admin.add_view(MyModelView(Ibindi, db.session))
    admin.add_view(MyModelView(Itsinda, db.session))
    admin.add_view(MyModelView(ItsindaMember, db.session))
    admin.add_view(MyModelView(IsandukuNshya, db.session))
    admin.add_view(MyModelView(InguzanyoZatanzwe, db.session))
    admin.add_view(MyModelView(InguzanyoZabandi, db.session))
    admin.add_view(MyModelView(Ibiramba, db.session))
    admin.add_view(MyModelView(Ububiko, db.session))
    admin.add_view(MyModelView(Role, db.session))
    admin.add_view(MyModelView(Notification, db.session))
    admin.add_view(MyModelView(CRM, db.session))

    #toolbar = DebugToolbarExtension(app)

    # Initiating different instances that are to be used with the application.
    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)
    #manager.init_app(app)
    flask_excel.init_excel(app)
    api.init_app(app)
    #toolbar.init_app(app)

    from app import models
    #from .overall import overall as overall_blueprint
    #app.register_blueprint(admin_blueprint, url_prefix="overall")

    # from .admin import admin as admin_blueprint
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')

    # Importing different Blueprints that are defined within the platform.
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .scmapp import supply_chain as supply_chain_blueprint
    app.register_blueprint(supply_chain_blueprint, url_prefix='/supply_chain')

    from .tumika import tumika as tumika_blueprint
    app.register_blueprint(tumika_blueprint, url_prefix='/tumika')

    from .aicos_backup import aicos_backup as aicos_backup_blueprint
    app.register_blueprint(aicos_backup_blueprint, url_prefix='/aicos_backup_blueprint')

    from .aicos_cb import aicos_cb as aicos_cb_blueprint
    app.register_blueprint(aicos_cb_blueprint, url_prefix='/aicos_cb_blueprint')

    from .aicos_eregister import aicos_eregister as aicos_eregister_blueprint
    app.register_blueprint(aicos_eregister_blueprint, url_prefix='/aicos_eregister_blueprint')

    from .aicos_ezigama import aicos_ezigama as aicos_ezigama_blueprint
    app.register_blueprint(aicos_ezigama_blueprint, url_prefix='/aicos_ezigama_blueprint')

    from .aicos_finance import aicos_finance as aicos_finance_blueprint
    app.register_blueprint(aicos_finance_blueprint, url_prefix='/aicos_finance_blueprint')

    from .aicos_imboni import aicos_imboni as aicos_imboni_blueprint
    app.register_blueprint(aicos_imboni_blueprint, url_prefix='/aicos_imboni_blueprint')

    from .aicos_mgt import aicos_mgt as aicos_mgt_blueprint
    app.register_blueprint(aicos_mgt_blueprint, url_prefix='/aicos_mgt_blueprint')

    from .aicos_proof import aicos_proof as aicos_proof_blueprint
    app.register_blueprint(aicos_proof_blueprint, url_prefix='/aicos_proof_blueprint')

    from .aicos_reporter import aicos_reporter as aicos_reporter_blueprint
    app.register_blueprint(aicos_reporter_blueprint, url_prefix='/aicos_reporter_blueprint')

    from .aicos_salesio import aicos_salesio as aicos_salesio_blueprint
    app.register_blueprint(aicos_salesio_blueprint, url_prefix='/aicos_salesio_blueprint')

    from .aicos_stack import aicos_stack as aicos_stack_blueprint
    app.register_blueprint(aicos_stack_blueprint, url_prefix='/aicos_stack_blueprint')

    from .aicos_monitor import aicos_monitor as aicos_monitor_blueprint
    app.register_blueprint(aicos_monitor_blueprint, url_prefix='/aicos_stack_blueprint')

    from .aicos_acc import aicos_acc as aicos_acc_blueprint
    app.register_blueprint(aicos_acc_blueprint, url_prefix='/aicos_acc')

    from .aicos_members import aicos_members as aicos_members_blueprint
    app.register_blueprint(aicos_members_blueprint, url_prefix='/aicos_members')

    from .aicos_pm import aicos_pm as aicos_pm_blueprint
    app.register_blueprint(aicos_pm_blueprint, url_prefix='/aicos_pm')

    from .aicos_req import aicos_req as aicos_req_blueprint
    app.register_blueprint(aicos_req_blueprint, url_prefix='/aicos_requirements')

    from .aicos_wcm import aicos_wcm as aicos_wcm_blueprint
    app.register_blueprint(aicos_wcm_blueprint, url_prefix='/wide_cooperative_market')

    from .aicos_trainer import aicos_trainer as aicos_trainer_blueprint
    app.register_blueprint(aicos_trainer_blueprint, url_prefix='/aicos_trainer')
    
    from .aicos_ferwacotamo import aicos_ferwacotamo as aicos_ferwacotamo_blueprint
    app.register_blueprint(aicos_ferwacotamo_blueprint, url_prefix='/federation')

    from .aicos_confederation import aicos_confederation as aicos_confederation_blueprint
    app.register_blueprint(aicos_confederation_blueprint, url_prefix='/confederation')

    from .aicos_rca import aicos_rca as aicos_rca_blueprint
    app.register_blueprint(aicos_rca_blueprint, url_prefix='/rca')

    from .aicos_union import aicos_union as aicos_union_blueprint
    app.register_blueprint(aicos_union_blueprint, url_prefix='/union')

    from .aicos_users import aicos_users as aicos_users_blueprint
    app.register_blueprint(aicos_users_blueprint, url_prefix='/aicos_users')

    from .aicos_stock_managment import aicos_stock_managment as aicos_stock_managment_blueprint
    app.register_blueprint(aicos_stock_managment_blueprint, url_prefix='/aicos_stock_managment')

    from .aicos_crm import aicos_crm as aicos_crm_blueprint
    app.register_blueprint(aicos_crm_blueprint, url_prefix='/aicos_crm')


    from .aicos_bank import aicos_bank as aicos_bank_blueprint
    app.register_blueprint(aicos_bank_blueprint, url_prefix='/banks')


    from .copa_member_profile import member_profile as member_profile_blueprint
    app.register_blueprint(member_profile_blueprint, url_prefix='/member_profile')


    
    """
    from .product.views import product as product_blueprintmember_profile
    app.register_blueprint(product_blueprint, url_prefix='/try')
    """

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('description', type=float)

    # The route to define home without any other blueprint.
    @app.route('/')
    @app.route('/home')
    def home():
        return "Welcome to the Catalog Home. Muhiza Frank"
     
    # Class to try building API using extension that
    # interact with the models directly.
    class MemberApi(Resource):
        def get(self, id=None, page=1):
            if not id:
                products = Member.query.paginate(page, 10).items
            else:
                products = [Member.query.get(id)]
            if not products:
                abort(404)
            res = {}
            for product in products:
                res[product.id] = {
                    'name': product.name,
                    'plate': product.plate,
                }
            return json.dumps(res)
     
        def post(self):
            args = parser.parse_args()
            name = args['name']
            plate = args['plate']
            product = Role(name, plate)
            db.session.add(product)
            db.session.commit()
            res = {}
            res[product.id] = {
                'name': product.name,
                'plate': product.plate,
            }
            return json.dumps(res)
            """
                api.add_resource(
                   MemberApi,
                   '/api/member',
                   '/api/member/<int:id>'
                   )
            """
    # Routes to handle different errors that occur
    # during the interection between user and the platform.

    # Handline forbidden error.
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    # Handline page not found error.
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    # Handline internal server error, error
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    return app












