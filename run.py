import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000)
=======
    app.run()
>>>>>>> 8af27a770af8a0ec55584e6e047bf8786eb76dab






    