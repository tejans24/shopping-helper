brew install python
pip install virtualenv
virtualenv ENV
ENV/bin/pip install django
ENV/bin/pip install djangorestframework
ENV/bin/pip install markdown
ENV/bin/pip install django-filter
ENV/bin/pip install pyyaml
sudo easy_install psycopg2
ENV/bin/pip install psycopg2
ENV/bin/python manage.py syncdb
