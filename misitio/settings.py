"""
Django settings for misitio project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k8-v+)=im8nj$$#hcbiocv9^)bvij%v6jub5e)1^q9n@3ti4va'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.Registro',
    'apps.Usuario',
    'rest_framework',
    'social_django',
    'social.apps.django_app.default',
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'misitio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'misitio.wsgi.application'

AUTHENTICATION_BACKENDS = [
                'social.backends.facebook.FacebookAppOAuth2',
                'social.backends.facebook.FacebookOAuth2',
                'django.contrib.auth.backends.ModelBackend',
                'social_core.backends.facebook.FacebookOAuth2',
]

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY = '453805552275380'
SOCIAL_AUTH_FACEBOOK_SECRET = '5846b40f7b9ed8b7d8ab736ca8cfe11e'



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/images/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'images')
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'static-only')

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'



# PWA
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')

PWA_APP_NAME = 'Proyecto miel y apicultura'
PWA_APP_DESCRIPTION = 'Miel y apicultura Web App DUOC'
PWA_APP_THEME_COLOR = '#ffff40'
PWA_APP_BACKGROUND_COLOR = '#fff'
PWA_APP_ICONS = [
    {
        'src': '/static/images/icons/abeja.png',
        'sizes': '256x256'
    },
    {
        'src': '/static/images/icons/miel.png',
        'sizes': '256x256'
    },
    {
        'src': '/static/images/icons/panal.png',
        'sizes': '256x256'
    }
]

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mielyapicultura@gmail.com'
EMAIL_HOST_PASSWORD = 'duoc2020'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'