import os
from .default import *


def getenv_bool(name, default=False):
    value = os.getenv(name)
    if value is None:
        return default
    if value.lower() in ('yes', 'true'):
        return True
    return False


DEBUG = getenv_bool('DEBUG', default=False)
SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'authentication',
    'choir.repertory',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
