from .test_common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Debug toolbar
from debug_toolbar import settings as dt_settings
is_running_tests = dt_settings.get_config()['IS_RUNNING_TESTS']
if not is_running_tests:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = ['127.0.0.1']

# S3 Media
# STORAGES = dict(
#     default=dict(
#         backend='storages.backends.s3.S3Storage',
#     ),
# )
