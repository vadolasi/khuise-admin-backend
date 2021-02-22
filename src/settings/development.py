import platform

from src.settings.base import *

DEBUG = True

ALLOWED_HOSTS.append('*')

INSTALLED_APPS.extend(['django.contrib.admin', 'django.contrib.messages', 'django_extensions', 'debug_toolbar', 'mjml'])

TEMPLATES[0]['OPTIONS'] = {'loaders': [(
    'pypugjs.ext.django.Loader',
    (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ),
    )]}
TEMPLATES[0]['OPTIONS']['builtins'] = [
    'pypugjs.ext.django.templatetags',
]
TEMPLATES[0]['OPTIONS']['context_processors'] = [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
]

MIDDLEWARE.insert(1, 'debug_toolbar.middleware.DebugToolbarMiddleware')
MIDDLEWARE.insert(4, 'django.contrib.messages.middleware.MessageMiddleware')

INTERNAL_IPS = ['127.0.0.1']

MJML_BACKEND_MODE = 'tcpserver'
MJML_TCPSERVERS = [
    ('127.0.0.1', 28101),
]

