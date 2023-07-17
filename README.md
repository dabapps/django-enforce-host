django-enforce-host
===================

[![pypi release](https://img.shields.io/pypi/v/django-enforce-host.svg)](https://pypi.python.org/pypi/django-enforce-host)

Sometimes, it's unavoidable that multiple URLs point at the same app - for example, on Heroku, all apps get a `.herokuapp.com` address, as well as any custom domains that are pointed at them.

This is a simple Django middleware that redirects all traffic from hosts other than the one(s) you specify to your canonical URL.

Tested against Django 3.2 and 4.0, 4.1 and 4.2 on Python 3.8, 3.9, 3.10 and 3.11.

### Installation

Install from PyPI

    pip install django-enforce-host

In your `MIDDLEWARE` setting, add the middleware just after the `SecurityMiddleware`:

    MIDDLEWARE = [
        # Django's SecurityMiddleware will handle HTTP -> HTTPS redirects
        # before the EnforceHostMiddleware redirects to the canonical domain
        'django.middleware.security.SecurityMiddleware',
        'enforce_host.EnforceHostMiddleware',
        ... other middleware
    ]

Set the following setting to be either a single allowed host, or a list of allowed hosts:

    ENFORCE_HOST = 'yourapp.com'

That's it!

## Code of conduct

For guidelines regarding the code of conduct when contributing to this repository please review [https://www.dabapps.com/open-source/code-of-conduct/](https://www.dabapps.com/open-source/code-of-conduct/)

