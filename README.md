shopping-helper
==================


- Framework: Django 1.5
- Language: Python 2.7
- Database: Postgresql 9.2


Developmental Guide:

- init.sh script: This initializes all the dependecy modules and packages needed for this project. 
  - Pre-req: homebrew on OSX needs to be installed
  - run it with sh ./init.sh

Data layer (Postgres setup):

- Install http://postgresapp.com/ for OSX. It automatically runs on port 5432 , can also configure through brew or postgres installation package from the official website.
    - Database name: shopping 
    - User: root (You can modify the settings.py DATABASES/USERNAME to whatever you use) creating a root user is prefered
    - Password: None by default, can modify according to perference for development


Documentaion Referals:

- http://django-rest-framework.org
- https://www.djangoproject.com
- http://docs.python.org/2/
- http://www.virtualenv.org/en/latest/
- http://postgresapp.com
