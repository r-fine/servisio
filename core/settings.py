import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = 'django-insecure-kb!nn%q25by6@+0rqr#_uz9xy(q$=ycyg4=t#plp)m4qhm3s6&'

DEBUG = True

ALLOWED_HOSTS = ['servicio-391.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.postgres',
    'crispy_forms',
    'widget_tweaks',
    'django_tables2',
    'django_filters',
    'mptt',
    'allauth',
    'allauth.account',
    'captcha',
    'ckeditor',
    'apps.accounts.apps.AccountsConfig',
    'apps.services',
    'apps.orders',
    'tawkto',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.services.context_processors.services',
                'apps.orders.context_processors.order_item_counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd4u7ooip9hgqaa',
#         'USER': 'tzopvjlqycsvda',
#         'PASSWORD': 'f454331e7417ceb06a0510533868d0ee32d703a7f1a31a307b35f24eb9de534d',
#         'HOST': 'ec2-52-19-164-214.eu-west-1.compute.amazonaws.com',
#         'PORT': '5432',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cse391Final',
        'USER': 'postgres',
        'PASSWORD': 'pgpasswd',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# debug_toolbar Settings

if DEBUG:
    INTERNAL_IPS = ("127.0.0.1",)
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
    INSTALLED_APPS += ("debug_toolbar",)

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.history.HistoryPanel',
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
    ]

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media Files

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# crispy forms template pack

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# login urls

LOGIN_URL = "/auth/login"
LOGIN_REDIRECT_URL = "/"

# authentication settings

AUTH_USER_MODEL = 'accounts.LocalUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Email setting

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# allauth settings

ACCOUNT_SIGNUP_FORM_CLASS = 'apps.accounts.forms.SignupForm'
ACCOUNT_ADAPTER = 'apps.accounts.adapter.AccountAdapter'

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_DISPLAY = 'apps.accounts.utils.user_display'
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'accounts:order_history'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'accounts:order_history'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300

SITE_ID = 1

# ckeditor settings

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Format'],
            ['Bold', 'Italic', 'Underline'],
            [
                'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'
            ],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'height': 300,
        'width': 550,
    },
    'minimal': {
        'toolbar': [
            ['Bold', 'Italic', 'Underline'],
            ['Smiley'],
        ],
        'height': 140,
        'width': 465,
    },
}

TAWKTO_ID_SITE = '127.0.0.1'
