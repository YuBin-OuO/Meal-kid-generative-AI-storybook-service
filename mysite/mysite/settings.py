"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import environ
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env.dev')
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
# DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myaccount",
    "reader",
    "generator",
    'quiz',
    #'debug_toolbar',
    # all auth
    "django.contrib.sites",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.kakao',
    "mine",

]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "myaccount.custom_middleware.UserSessionMiddleware",  # 사용자 정의 미들웨어 추가
    "allauth.account.middleware.AccountMiddleware",
    #"debug_toolbar.middleware.DebugToolbarMiddleware",
]
#INTERNAL_IPS = ['127.0.0.1',] #temp
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#         'quiz': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     },
# }
ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates',
                 BASE_DIR / 'myaccount/templates',],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

SITE_ID = 1
SOCIALACCOUNT_LOGIN_ON_GET = True

from .local_settings import *

SOCIALACCOUNT_PROVIDERS = {
    "kakao": {
        "APP": {
            "client_id": KAKAO_CLIENT_ID,
            #"client_id": 'os.getenv("KAKAO_CLIENT_ID")',
            "secret": KAKAO_SECRET_SECRET,
            #"secret": os.getenv("KAKAO_SECRET_KEY"),
            "key": ""
        },
        "SCOPE": [
            "profile_nickname",
            "account_email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    },
    "naver": {
        "APP": {
            "client_id": NAVER_CLIENT_ID,
            "secret": NAVER_CLIENT_SECRET,
            "key": ""
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    },
    "google": {
        "APPS": [
            {
                "client_id": GOOGLE_CLIENT_ID,
                "secret": GOOGLE_CLIENT_SECRET,
                "key": ""
            },
        ],
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}


WSGI_APPLICATION = "mysite.wsgi.application"

LOGIN_REDIRECT_URL = 'select_account'
# LOGOUT_REDIRECT_URL = 'index'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    'story': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database/story_db.db',
    }
}

DATABASE_ROUTERS = ['common.db_router.AccountDBRouter',
                    'common.db_router.StoryDBRouter',
]



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = 'ko-kr'
# TIME_ZONE = "UTC"
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / 'static',
                    BASE_DIR / 'generator/static',
                    BASE_DIR / 'reader/static']

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 이메일 설정, manage.py와 같은 경로에 secret.json 파일을 만든 후 EMAIL_HOST_USER, EMAIL_HOST_PASSWORD 정의.
import json

#SECRET_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_FILE_PATH = os.path.join(BASE_DIR, 'secret.json')

with open(SECRET_FILE_PATH) as f:
    secrets = json.load(f)

def get_secret(secret_name):
    try:
        return secrets[secret_name]
    except KeyError:
        raise Exception(f"Set the {secret_name} environment variable")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "youracc@gmail.com"
EMAIL_HOST_PASSWORD = "app password"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER