
"""
	This is python's standard utility module, 
	it allow us to interact with operating system
	that we are using
"""
import os



# Accessing the current directory that we are working with
BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

# These are the environment variables that are used for securing the application.
SECRET_KEY = "thisisthesecretkeyhere"
SQLALCHEMY_DATABASE_URI  = "mysql://root:annemuhiza@localhost/coop"
#SQLALCHEMY_DATABASE_URI  = "mysql://root:anne1Muhiza@localhost/aicos"
RECAPTCHA_PUBLIC_KEY = '6LdYIDcUAAAAAEE3N3tNqcYu50MJSTlGA5lwu5Pl'
RECAPTCHA_PRIVATE_KEY = '6LdYIDcUAAAAAD8ayN_2Mkhauh_-MdK12XxdTLEo'


# Path for saving the uploaded madia files
UPLOADS_DEFAULT_DEST = TOP_LEVEL_DIR + '/project/static/img/'
UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/img/'
UPLOADED_IMAGES_DEST = TOP_LEVEL_DIR + '/project/static/img/'
UPLOADED_IMAGES_URL = 'http://localhost:5000/static/img/'
















