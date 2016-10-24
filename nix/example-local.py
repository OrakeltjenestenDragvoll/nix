
TEMPLATE_DEBUG = True
SECRET_KEY = 'override this in prod'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

PRINTMON_URL = 'http://nix.svt.ntnu.no:8080'

EMAIL_ADDRESS_SENDER = 'example@example.com'
ORDER_TARGET_EMAIL = 'example@example.com'
ORDER_COPY_EMAIL = 'example@example.com'

EMAIL_HOST = 'smtp.stud.ntnu.no'
