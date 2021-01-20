from src.settings.base import *

DEBUG = True

ALLOWED_HOSTS.extend(['localhost', '0.0.0.0'])

INSTALLED_APPS.extend(['django_extensions', 'debug_toolbar'])

MIDDLEWARE.insert(1, 'debug_toolbar.middleware.DebugToolbarMiddleware')

INTERNAL_IPS = ['127.0.0.1']
