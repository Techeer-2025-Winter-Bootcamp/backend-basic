from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("MYSQL_DATABASE"),
        'USER': os.getenv("MYSQL_USER"),
        'PASSWORD': os.getenv("MYSQL_PASSWORD"),
        'HOST': 'mysqldb',
        'PORT': int(os.getenv("DB_PORT", 3306)),
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

CORS_ORIGIN_ALLOW_ALL = False
