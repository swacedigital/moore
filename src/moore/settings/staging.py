"""
Django settings for the development environment of Project Moore.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l0gkw_q4rgex=0%ep84(yw$gx+mxr)u1e-x5yv@2j)a%(4=1!s'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DB', 'moore'),
        'USER': os.environ.get('DJANGO_DB_USER', 'moore'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASS', ''),
        'HOST': os.environ.get('DJANGO_DB_HOST', '127.0.0.1'),
        'PORT':  os.environ.get('DJANGO_DB_PORT', '5432'),
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin
# backend - e.g. in notification emails. Don't include '/admin' or a
# trailing slash
BASE_URL = 'moore.swace.se'

ALLOWED_HOSTS = ['.swace.se', '.utn.swace.se']

# Email
# https://docs.djangoproject.com/en/1.10/ref/settings/#email-backend

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'info@moore.swace.se'

MELOS_URL = os.environ.get('MELOS_URL')
MELOS_ORG_ID = os.environ.get('MELOS_ORG_ID')
MELOS_ADMIN = os.environ.get('MELOS_ADMIN')

# Google API
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Instagram API
INSTAGRAM_ACCESS_TOKEN = os.environ.get('INSTAGRAM_ACCESS_TOKEN')

# Facebook API
FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')

try:
    from .local import *
except ImportError:
    pass
