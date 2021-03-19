# import os
from .common import *
from .warn import configure_warnings

configure_warnings()

DEBUG = True

CELERY_TASK_ALWAYS_EAGER = True

if not 'LOG_LEVEL' in os.environ:
    LOGGING = dict()

AUTHENTICATION_ADMIN_USER = 'test'
