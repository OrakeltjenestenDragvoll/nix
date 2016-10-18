import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_SETTINGS_DIRECTORY = os.path.dirname(os.path.join(BASE_DIR, 'nix', 'settings'))

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',
    # Nix apps
    'apps.posts',
    'apps.printers',
    # Third party apps
    'apps.feide',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'apps.feide.backend.FeideBackend',
    'django.contrib.auth.backends.ModelBackend')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ROOT_URLCONF = 'nix.urls'

WSGI_APPLICATION = 'nix.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEBUG = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = 'static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'files'),
]

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
]

SAML_FOLDER = '/webapps/nix2/saml'
SAML_EMPLOYEE_STRING = 'ou=OI-ITAVD-ORAKEL,ou=OI-ITAVD,ou=OI,ou=RE,ou=organization,dc=ntnu,dc=no'

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
# Dev-settings
if DEBUG:
    LOGIN_URL = '/auth/login/'
    LOGOUT_URL = '/auth/logout/'

# Prod-settings
else:
    LOGIN_URL = '/login/'
    LOGOUT_URL = '/logout/'

# Remember to keep 'local' last, so it can override any setting.
for settings_module in ['local']:  # local last
    if not os.path.exists(os.path.join(PROJECT_SETTINGS_DIRECTORY, settings_module + ".py")):
        sys.stderr.write("Could not find settings module '%s'.\n" % settings_module)
        if settings_module == 'local':
            sys.stderr.write("You need to copy the settings file "
                             "'studlan/settings/example-local.py' to "
                             "'studlan/settings/local.py'.\n")
        sys.exit(1)
    try:
        exec('from %s import *' % settings_module)
    except ImportError, e:
        print "Could not import settings for '%s' : %s" % (settings_module, str(e))
