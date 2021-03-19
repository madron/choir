import warnings

IGNORE_WARNINGS_MODULES = [
    # 'debug_toolbar.middleware',       # https://github.com/jazzband/django-debug-toolbar/pull/1382
]
IGNORE_WARNINGS_MESSAGES = [
]


def configure_warnings():
    warnings.simplefilter('default')
    for module in IGNORE_WARNINGS_MODULES:
        warnings.filterwarnings('ignore', module=module)
    for message in IGNORE_WARNINGS_MESSAGES:
        warnings.filterwarnings('ignore', message=message)
