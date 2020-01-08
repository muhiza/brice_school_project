
from flask import Blueprint

aicos_bank = Blueprint("aicos_bank", __name__, template_folder="templates")

from . import views