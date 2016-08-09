from base import *



INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY="u)jrq1dya1lu@(4g5@+z=g=xze^+qx%8aq*7fa5-opva$wrt8q"
AWS_ACCESS_KEY_ID = "AKIAIAYMABUJSUZQIRXA"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "awkwardnamebucket-dev"
