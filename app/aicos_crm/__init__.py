from flask import Blueprint

aicos_crm = Blueprint('aicos_crm', __name__,
							template_folder='templates')

from . import views