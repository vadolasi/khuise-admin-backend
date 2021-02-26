"""Django settings for controleDeEstoque project.

Generated by "django-admin startproject" using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from io import StringIO
from pathlib import Path
from datetime import timedelta

import environ
from kombu import Exchange, Queue

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SRC_DIR = BASE_DIR / 'src'

env = environ.Env()
env_file = SRC_DIR / 'settings' / '.env'

if env_file.exists():
    environ.Env.read_env(str(env_file))
else:
    env_content = ''

    for env_var, env_var_content in os.environ.items():
        env_content = f'{env_content}{env_var}={env_var_content}\n'

    environ.Env.read_env(StringIO(env_content))

BASE_URL = env("BASE_URL")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_filters',
    'graphene_django',
    'graphql_auth',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'rest_framework',
    'apps.accounts',
    'apps.products',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
    }
]

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': env.db(),
    # 'products': {
    #     'ENGINE': 'djongo',
    #     'NAME': 'products',
    #     'CLIENT': {
    #         'name': env('MONGO_DATABASE'),
    #         'host': env('MONGO_HOST'),
    #         'username': env('MONGO_USER'),
    #         'password': env('MONGO_PASSWORD'),
    #         'authMechanism': 'SCRAM-SHA-1',
    #     },
    # },
}

# DATABASE_ROUTERS = ['src.database_routers.Router']


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_USER_MODEL = 'accounts.User'

AUTHENTICATION_BACKENDS = [
    'graphql_auth.backends.GraphQLAuthBackend',
    'django.contrib.auth.backends.ModelBackend'
]


# * GraphQl

GRAPHENE = {
    'SCHEMA': 'src.schema.schema',
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

GRAPHQL_JWT = {
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
    'JWT_EXPIRATION_DELTA': timedelta(minutes=5),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
    'JWT_COOKIE_SAMESITE': 'None',
    'JWT_ALLOW_ANY_CLASSES': [
        'graphql_auth.relay.Register',
        'graphql_auth.relay.SendPasswordResetEmail',
        'graphql_auth.relay.PasswordReset',
        'graphql_auth.relay.ObtainJSONWebToken',
        'graphql_auth.relay.VerifyToken', 
    ],
}

GRAPHQL_AUTH = {
    'REGISTER_MUTATION_FIELDS': ['email', 'first_name', 'last_name'],
    'SEND_ACTIVATION_EMAIL': False,
    'LOGIN_ALLOWED_FIELDS': ['email'],
    'USER_NODE_FILTER_FIELDS': {
        'email': ['exact'],
        'is_active': ['exact'],
        'status__archived': ['exact'],
        'status__verified': ['exact'],
        'status__secondary_email': ['exact'],
    },
    'EMAIL_ASYNC_TASK': 'src.tasks.graphql_auth_async_email',
}


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3-sa-east-1.amazonaws.com'

AWS_S3_FILE_OVERWRITE = False

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

STATICFILES_STORAGE = 'src.storage_backends.StaticStorage'
DEFAULT_FILE_STORAGE = 'src.storage_backends.MediaStorage'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

# UPLOADED_FILES_USE_URL = True


#* Email

EMAIL_CONFIG = env.email_url()
vars().update(EMAIL_CONFIG)

TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'


# * CORS

CORS_ALLOWED_ORIGINS = [
  "http://localhost:3000",
  "http://192.168.0.2",
  "https://a1f7bd701779.ngrok.io",
  "http://a1f7bd701779.ngrok.io",
]
CORS_ALLOW_CREDENTIALS = True


# * Celery

task_default_queue = 'default'
default_exchange = Exchange('media', type='direct')
task_queues = (
    Queue(
        'media_queue',
        exchange=default_exchange,
        routing_key='video',
    )
)

