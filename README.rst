django-proto
=======================

Features
---------

* For Django 1.7
* Twitter Bootstrap_ 3


.. _Bootstrap: https://github.com/twbs/bootstrap

Usage
--------------------------

Name your project first::

    mkvirtualenv project_name

Install Django::

    pip install django


To create the project, run the following command::

    django-admin.py startproject --template=https://github.com/privgrey/django-proto/archive/master.zip --extension=py,rst,html --name project_name.conf,uwsgi.ini,base.txt,prod.txt  project_name

check the document:
https://docs.djangoproject.com/en/2.2/ref/django-admin/#startproject

Set Environment Variable
--------------------------
Set Django settings file before bootstraping::

    export DJANGO_SETTINGS_MODULE=project_name.settings.dev

Add custom environment variables to your postactivate script
--------------------------

Edit your virtualenvs/bin/postactivate::

    export DJANGO_SETTINGS_MODULE=project_name.settings.dev
    
    
Install Python packages, Enter the 'requirements' folder::

    pip install -r base.txt
    
Setup the postgresql database
--------------------------

After Setting up settings/dev.py::

    sudo su - postgres
    createuser -P
    createdb --owner user dbname
    logout
