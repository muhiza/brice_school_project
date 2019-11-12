![alt text](https://raw.githubusercontent.com/muhiza/extrat/master/static/welcome%20image.png)

# SMART COOPERATIVE PLATFORM - AICOS

## Modular Approach in Smart Cooperative Platform Development

Modular programming is the process of subdividing a computer program into separate sub-programs. A module is a separate software component. It can often be used in a variety of applications and functions with other components of the system.

* Some programs might have thousands or millions of lines and to manage such programs it becomes quite difficult as there might be too many syntax errors or logical errors present in the program, so to manage such type of programs concept of modular programming approached.

* Each sub-module contains something necessary to execute only one aspect of the desired functionality.
Modular programming emphasis on breaking of large programs into small problems to increase the maintainability, readability of the code and to make the program handy to make any changes in the future or to correct the errors.

## Points which should be taken care of prior to modular program development:

* Limitations of each and every module should be decided.
* In which way a program is to be partitioned into different modules.
* Communication among different modules of the code for proper execution of the entire program.

The complete code for smart cooperative platform, Build all functionalities with as a Web Platform With Python and Flask, which you can find on aicos.rw [here](http://www.aicos.rw/).

## Installation and Set Up
Prerequisites:

* [Python 3](https://www.python.org/)
* [virtualenv](https://virtualenv.pypa.io/en/latest/)

Clone the repo from GitHub:
```
git clone https://github.com/muhiza/aicos_coop.git
```

Create a virtual environment for the project and activate it:
```
virtualenv smart-coop
source smart-coop/bin/activate
```
Install the required packages:
```
pip install -r requirements.txt
```
## Database configuration
You will need to create a MySQL user your terminal, as well as a MySQL database. Then, grant all privileges on your database to your user, like so:
```
$ mysql -u root

mysql> CREATE USER 'sc_admin'@'localhost' IDENTIFIED BY 'sc2019';

mysql> CREATE DATABASE smartcoop_db;

mysql> GRANT ALL PRIVILEGES ON smartcoop_db . * TO 'sc_admin'@'localhost';
```
Note that ```sc_admin``` is the database user and ```sc2019``` is the user password. After creating the database, run migrations as follows:

* ```flask db migrate```
* ```flask db upgrade```

## instance/config.py file

Create a directory, ```instance```, and in it create a ```config.py``` file. This file should contain configuration variables that should not be publicly shared, such as passwords and secret keys. The app requires you to have the following configuration variables:

* SECRET_KEY
* SQLALCHEMY_DATABASE_URI ('mysql://sc_admin:sc2019@localhost/smartcoop_db')

## Launching the Program
Set the FLASK_APP and FLASK_CONFIG variables as follows:

* ```export FLASK_APP=run.py```
* ```export FLASK_CONFIG=development```
You can now run the app with the following command: ```flask run```

## Testing
First, create a test database and grant all privileges on your test database to your user:
```
$ mysql -u root

mysql> CREATE DATABASE smartcoop_test;

mysql> GRANT ALL PRIVILEGES ON smartcoop_test . * TO 'sc_admin'@'localhost';
```

To test, run the following command: python tests.py

## Built With...
* [Python/Flask](https://flask.palletsprojects.com/en/0.12.x/)

## Credits and License
Copyright (c) 2019 Extra technologies ltd

Permission is hereby granted, to Extra team obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to copy, modify, merge, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
