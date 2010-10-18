#!/usr/bin/env/python
#-*- coding: utf-8 -*-
# Django settings for {{ project_name }} project.

import os
import socket

ADMINS = (
    ('Recep KIRMIZI', 'rkirmizi@gmail.com'),
)

MANAGERS = ADMINS
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

if socket.gethostname() == 'li184-202': # remote server ise...
    WEB_URL = 'http://siteadi.com'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.',# Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }
    ADMIN_MEDIA_PREFIX = '/admin_media/'
    DEBUG = False
else:
    WEB_URL = 'http://localhost:8000'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.',# Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }
    ADMIN_MEDIA_PREFIX = '/home/rkirmizi/sourcebox/pythonlibs/django/contrib/admin/media/'
    DEBUG = True

TEMPLATE_DEBUG = DEBUG
TIME_ZONE = 'Europe/Istanbul'
LANGUAGE_CODE = 'tr-TR'
SITE_ID = 1
USE_I18N = True
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '%s/media/' % WEB_URL
SECRET_KEY = ''

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # 'django.contrib.admin',
    # 'django.contrib.admindocs',
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
        'django.request':{
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
