from .common import *

DEBUG = False
if os.getenv('DEBUG', None) == 'True':
    DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DEFAULT_DB_NAME', 'choir'),
        'USER': os.getenv('DEFAULT_DB_USERNAME', 'choir'),
        'PASSWORD': os.getenv('DEFAULT_DB_PASSWORD', 'choir'),
        'HOST': os.getenv('DEFAULT_DB_HOST', 'db'),
        'PORT': os.getenv('DEFAULT_DB_PORT', '5432'),
    }
}

MEDIA_ROOT = '/media'
STATIC_ROOT = '/static'

MEDIA_URL = '/media/'
