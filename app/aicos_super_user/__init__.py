from flask import Blueprint

aicos_super_user = Blueprint('aicos_super_user', __name__, template_folder='templates')

from . import views