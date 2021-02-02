import platform

from src.settings.base import *

DEBUG = True

ALLOWED_HOSTS.extend(['localhost', '0.0.0.0', '192.168.0.3'])

INSTALLED_APPS.extend(['django_extensions', 'debug_toolbar', 'mjml'])

TEMPLATES['OPTIONS']['loaders'] = [(
    'pypugjs.ext.django.Loader',
    (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ),
)]
TEMPLATES['OPTIONS']['builtins'] = [
    'pypugjs.ext.django.templatetags',
]

MIDDLEWARE.insert(1, 'debug_toolbar.middleware.DebugToolbarMiddleware')

INTERNAL_IPS = ['127.0.0.1']

if platform.system() == "Linux":
    MJML_EXEC_CMD = str(BASE_DIR / 'node_modules' / '.bin' / 'mjml')

else:
    MJML_EXEC_CMD = str(BASE_DIR / 'node_modules' / '.bin' / 'mjml.cmd')

