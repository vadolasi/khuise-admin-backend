import django_heroku

from src.settings.base import *

DEBUG = False

ALLOWED_HOSTS.append('')

django_heroku.settings(locals())
