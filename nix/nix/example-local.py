
TEMPLATE_DEBUG = True
SECRET_KEY = 'override this in prod'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

PRINTMON_URL = 'http://nix.svt.ntnu.no:8080'

ORDER_TARGET_EMAIL = 'example@example.com'
ORDER_COPY_EMAIL = 'example@example.com'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gmail'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
