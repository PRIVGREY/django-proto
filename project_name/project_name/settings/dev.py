"""Development settings and globals."""

from __future__ import absolute_import

from os.path import join, normpath

from .base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/1.7/ref/settings/#debug
DEBUG = True
# See: https://docs.djangoproject.com/en/1.7/ref/settings/#template-debug
TEMPLATE_DEBUG = True
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/1.7/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION




########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/1.7/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'dbname',
#         'USER': 'username',
#         'PASSWORD': 'badpassword',
#         'HOST': '127.0.0.1',

#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'db.sqlite3'),
    }
}

#DATABASE_ROUTERS = ['appname.router.AppRouter',]

########## END DATABASE CONFIGURATION
