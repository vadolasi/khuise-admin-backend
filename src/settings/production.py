import django_heroku

from src.settings.base import *

DEBUG = False

ALLOWED_HOSTS.append('')

TEMPLATES[0]['APP_DIRS'] = True

django_heroku.settings(locals())

