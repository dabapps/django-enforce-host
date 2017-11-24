
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = 'enforce_hostname.tests.urls'

SECRET_KEY = 'abcde12345'

ALLOWED_HOSTS = ['original.com', 'enforced.com', 'enforced2.com']

MIDDLEWARE = [
    'enforce_hostname.EnforceHostnameMiddleware'
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
