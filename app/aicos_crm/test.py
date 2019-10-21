import os
import sys
import unittest

# from config import basedir
from . import create_app, db
 
from app.models import *
from .froms import *
from .views import *

from datetime import datetime
# import datetime

# from sqlalchemy import DateTime

topdir = os.path.join(os.path.dirname(__file__),"..")
sys.path.append(topdir)

class TestCRMViews(unittest.TestCase):
    '''

    '''

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.config['BASEDIR'], TEST_DB)        
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
    def test_add_CRM_item():
        """
        Test that 
        """
        # create a department and a crm_item
        department = Department(id = 1,no = 1,
                                code  = '500',
                                email = 'department@gmail.com',
                                name  = 'TERIMBERE',
                                regdate = '2010',
                                certificate = 'CERTIFICATE',
                                description = 'description',
                                province    = 'province',
                                district    = 'district',
                                sector      = 'sector',
                                cell        = 'cell',
                                Activity    = 'Activity',
                                coop_type   = 'coop_type',

                                category   = 'category',
                                field      = 'field',
                                started_data     = datetime.datetime.utcnow,
                                starting_share   = 'starting_share',
                                share_per_person = 'share_per_person',
                                male_members     = '40',
                                female_members   = '60'

                               )
        crm_item = CRM(id=12345,tag = 'followup',
                        company_name = 'MyCompany',
                        email = 'mycompany@gmail.com',
                        website = 'www.mycompany.com',
                        address = 'KG345',
                        contact_type = 'Prime Customer',
                        phone_number = 'form.phone_number.data',
                        city = 'form.city.data',
                        country = 'form.country.data',
                        description = 'form.description.data',
                        status = 'form.status.data'
                        )

        db.session.add(department)
        db.session.add(crm_itemp)
        db.session.commit()

        # query the crm_item and destroy the session
        crm_item = CRM.query.get(1)
        db.session.remove()
        # delete the crm_item using a new session
        db.session = db.create_scoped_session()
        db.session.delete(p)
        db.session.commit()

    # def test_remove_CRM_item(id)
    #     """
    #     Test that CRM items table page has the number of items minus one
    #     after removing one item
    #     """
    #     target_url = url_for('aicos_crm.list_employees')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, redirect_url)

    # def test_edit_CRM_item(id, employee_id)
    #     """
    #     Test that employees page is inaccessible without login
    #     and redirects to login page then to employees page
    #     """
    #     target_url = url_for('admin.list_employees')
    #     redirect_url = url_for('auth.login', next=target_url)
    #     response = self.client.get(target_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, redirect_url)

if __name__ == '__main__':
    unittest.main()
