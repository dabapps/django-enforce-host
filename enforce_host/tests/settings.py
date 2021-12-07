from django.conf import global_settings

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "enforce_host.tests.urls"

SECRET_KEY = "abcde12345"

ALLOWED_HOSTS = ["original.com", "enforced.com", "enforced2.com"]

if hasattr(global_settings, "MIDDLEWARE"):
    MIDDLEWARE = ["enforce_host.EnforceHostMiddleware"]
else:
    MIDDLEWARE_CLASSES = ["enforce_host.EnforceHostMiddleware"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
