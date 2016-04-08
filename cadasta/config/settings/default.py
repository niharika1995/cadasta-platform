"""
Django settings for cadasta project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.utils.translation import ugettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@=fy$)xx+6yjo*us@&+m6$14@l-s6#atg(msm=9%)9@%b7l%h('

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'accounts.User'

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',
    'corsheaders',

    'core',
    'accounts',
    'organization',

    'crispy_forms',
    'widget_tweaks',
    'django_countries',
    'leaflet',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_docs',
    'djoser',
    'tutelary',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'audit_log.middleware.UserLoggingMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_VERSION': 'v1',
    'EXCEPTION_HANDLER': 'core.views.api.exception_handler'
}

ROOT_URLCONF = 'config.urls'
SITE_NAME = 'Cadasta'

BASE_TEMPLATE_DIR = os.path.join(os.path.dirname(BASE_DIR), 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_TEMPLATE_DIR,
                 os.path.join(BASE_TEMPLATE_DIR, 'allauth')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'core.backends.Auth',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

DJOSER = {
    'SITE_NAME': SITE_NAME,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'account/password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'account/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
}

CORS_ORIGIN_ALLOW_ALL = False

LOGIN_REDIRECT_URL = '/dashboard/'
LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'

WSGI_APPLICATION = 'config.wsgi.application'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_FORMS = {
    'signup': 'accounts.forms.RegisterForm',
    'profile': 'accounts.forms.ProfileForm',
}
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_URL

LEAFLET_CONFIG = {
    'TILES': [('OpenStreetMap',
               'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
               {'attribution': 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'})],  # noqa
    'RESET_VIEW': False
}

LEAFLET_CONFIG = {
    'TILES': [('OpenStreetMap',
               'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
               {'attribution': 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'})],  # noqa
    'RESET_VIEW': False
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
    ('de', _('German')),
    ('es', _('Spanish')),
]

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'