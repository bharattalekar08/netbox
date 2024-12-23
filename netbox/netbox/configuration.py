import os

ALLOWED_HOSTS = ['*']

DATABASE = {
    'NAME': 'netbox',
    'USER': 'netbox',
    'PASSWORD': os.getenv('NETBOX-DB-PASSWORD'),
    'HOST': 'localhost',
    'PORT': '',
    'CONN_MAX_AGE': 300,
}

PLUGINS = [
    'netbox.tests.dummy_plugin',
]

REDIS = {
    'tasks': {
        'HOST': 'localhost',
        'PORT': 6379,
        'USERNAME': '',
        'PASSWORD': os.getenv('NETBOX-REDIS-PASSWORD'),
        'DATABASE': 0,
        'SSL': False,
    },
    'caching': {
        'HOST': 'localhost',
        'PORT': 6379,
        'USERNAME': '',
        'PASSWORD': os.getenv('NETBOX-REDIS-PASSWORD'),
        'DATABASE': 1,
        'SSL': False,
    }
}

# The secret key should be minimum 50 characters long
SECRET_KEY = os.getenv('SECRET-KEY')

DJANGO_ADMIN_ENABLED = True

DEFAULT_PERMISSIONS = {}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True
}
