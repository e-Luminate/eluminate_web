import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PACKAGE_ROOT, "apps"))

DEBUG = True

ADMINS = [
     ("Kim Spence-Jones", "kim@spencejones.com"),
]


DATABASES = {
    'default': {
        'ENGINE' : 'django.contrib.gis.db.backends.postgis',
        'NAME': 'e_luminate_db',
        'USER': 'e_luminate_user',
        'PASSWORD': 'e_luminate_password',
    }
}

### now overwrite stuff from the production server, if local_settings.py exists

try:
    from local_settings import *
except ImportError:
    pass

TEMPLATE_DEBUG = DEBUG
MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Europe/London"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

ugettext = lambda s: s

LANGUAGES = (
    ('en', ugettext('English')),
)
DEFAULT_LANGUAGE = 1

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/site_media/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PACKAGE_ROOT, "static"),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = "5cp+0%ee(yyq&amp;++izz088#xiw=vy%@k4^yv(4@o1)%1(fshwwz"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "pinax_utils.context_processors.settings",
    "account.context_processors.account",
    "events.context_processors.search",
    "custom_account.context_processors.theme",
]


MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "account.middleware.LocaleMiddleware",
    "account.middleware.TimezoneMiddleware",
]

ROOT_URLCONF = "eluminate_web.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "eluminate_web.wsgi.application"

TEMPLATE_DIRS = [
    os.path.join(PACKAGE_ROOT, "templates"),
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.gis',
    
    # theme
    "pinax_theme_bootstrap_account",
    "pinax_theme_bootstrap",
    "django_forms_bootstrap",
    
    
    # external
    "account",
    "metron",
    "eventlog",
    "south",
    "crispy_forms",
    "debug_toolbar",
    
    # project
    "eluminate_web",
    "events",
    "maps",
    "participant"
]

#SERIALIZATION_MODULES = { 'geojson' : 'maps.geojson_serializer' }

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOGIN_URL = "/account/login/" # @@@ any way this can be a url name?
ACCOUNT_OPEN_SIGNUP = False
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = True
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EMAIL = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
THEME_ACCOUNT_CONTACT_EMAIL = "info@e-luminatefestivals.co.uk"

SERVER_EMAIL = "no-reply@e-luminatefestivals.co.uk"

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'eluminate'
EMAIL_HOST_PASSWORD ='1209foxFlower'
DEFAULT_FROM_EMAIL = 'no-reply@e-luminatefestivals.co.uk'


# Django Debug toolbar
if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

