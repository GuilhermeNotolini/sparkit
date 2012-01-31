# -*- coding: utf-8 -*-
import os 

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
LOCAL = lambda x: os.path.join(SITE_ROOT, x)

SECRET_KEY = '!y21_@+av*=)@**%f9_8m42dyvhm1a0r2%_^(53c2^tm%qqd8i'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Victor Fontes', 'contato@victorfontes.com')
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': LOCAL('db.sqlite'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'

USE_I18N = True
USE_L10N = True

SITE_ID = 1

ON_HEROKU = os.environ.has_key('DATABASE_URL')

#if ON_HEROKU:
#    from libs.configs.env_heroku import * 
#else:
#    from libs.configs.env_dev import * 



MEDIA_ROOT = LOCAL('media')
MEDIA_URL = '/media/'

#STATIC_ROOT = LOCAL('static_root')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    LOCAL('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    
    # required by django-admin-tools
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'sparkitsite.urls'

TEMPLATE_DIRS = (LOCAL('templates'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'core',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
