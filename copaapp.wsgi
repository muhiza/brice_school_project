#!/usr/bin/python

#activate_this = '/var/www/venv/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))

import sys
import os
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/aicos_coop/")

#callable = create_app

#from app import create_app as application 
#application.secret_key = 'Addyoursecretkey'




from app import create_app

config_name = os.getenv('FLASK_CONFIG')
application = create_app(config_name)


application.secret_key = 'Addyoursecretkey'
