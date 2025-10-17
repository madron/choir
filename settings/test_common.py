# import os
from .common import *
from .warn import configure_warnings

configure_warnings()

DEBUG = True

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

STORAGES = dict(
    default=dict(
        BACKEND='django.core.files.storage.FileSystemStorage',
    ),
    staticfiles=dict(
        BACKEND='django.contrib.staticfiles.storage.StaticFilesStorage',
    ),
)
