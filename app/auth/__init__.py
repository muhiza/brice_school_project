"""
This is the file which create the -auth- Blueprint.
"""

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
