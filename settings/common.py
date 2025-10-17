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
    'choir.events',
    'choir.player',
    'choir.web',
    'bootstrap4',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'en-us')

STORAGES = dict(
    default=dict(
        BACKEND='storages.backends.s3.S3Storage',
    ),
    staticfiles=dict(
        BACKEND='django.contrib.staticfiles.storage.StaticFilesStorage',
    ),
)

# S3 Media
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', 'admin')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'admin123')
AWS_S3_ENDPOINT_URL = os.getenv('AWS_S3_ENDPOINT_URL', None)
AWS_S3_PUBLIC_URL = os.getenv('AWS_S3_PUBLIC_URL', '')
AWS_S3_SECURE_URLS = getenv_bool('AWS_S3_SECURE_URLS', default=True)
AWS_S3_CUSTOM_DOMAIN = os.getenv('AWS_S3_CUSTOM_DOMAIN', None)
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME', 'media')
AWS_S3_FILE_OVERWRITE = getenv_bool('AWS_S3_FILE_OVERWRITE', default=True)
AWS_QUERYSTRING_AUTH = getenv_bool('AWS_QUERYSTRING_AUTH', default=True)
AWS_QUERYSTRING_EXPIRE = int(os.getenv('AWS_QUERYSTRING_EXPIRE', '3600'))
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "public, max-age=604800, immutable",
}

PLAYER_AUDIO_FILE_PREFIX = os.getenv('PLAYER_AUDIO_FILE_PREFIX', 'https://corosantantonio.s3.amazonaws.com/songfile/')
DEFAULT_EVENT_LOCATION = os.getenv('DEFAULT_EVENT_LOCATION', '')
