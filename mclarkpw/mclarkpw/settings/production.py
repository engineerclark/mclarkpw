import os
from .base import *

dbname = os.environ['MCLARKPW_DBNAME']
dbuser = os.environ['MCLARKPW_DBUSER']
dbpass = os.environ['MCLARKPW_DBPASS']

DEBUG = False
TEMPLATE_DEBUG = False
SECRET_KEY = os.environ['MCLARKPW_SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': dbname,
        'USER': dbuser,
        'PASSWORD': dbpass
    }
}

ALLOWED_HOSTS = [
    '.mclark.pw',
    'www.mclark.pw',
    'localhost',
]