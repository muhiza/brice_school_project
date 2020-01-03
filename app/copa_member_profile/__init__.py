"""
This is the file which create the -auth- Blueprint.
"""

from flask import Blueprint

member_profile = Blueprint('member_profile', __name__, template_folder="templates")

from . import views
