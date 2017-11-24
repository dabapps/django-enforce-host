django-enforce-hostname
=======================

[![Build Status](https://travis-ci.org/dabapps/django-enforce-hostname.svg)](https://travis-ci.org/dabapps/django-enforce-hostname)
[![pypi release](https://img.shields.io/pypi/v/django-enforce-hostname.svg)](https://pypi.python.org/pypi/django-enforce-hostname)

Sometimes, it's unavoidable that multiple URLs point at the same app - for example, on Heroku, all apps get a `.herokuapp.com` address, as well as any custom domains that are pointed at them.

This is a simple Django middleware (new-style for Django 1.10 or later) that redirects all traffic from hosts other than the one(s) you specify to your canonical URL.

Tested against Django 1.10, 1.11 on Python 2.7, 3.4 and 3.6

### Installation

Install from PIP

    pip install django-enforce-hostname

In your `MIDDLEWARE` setting, add the following at the top:

    MIDDLEWARE = [
        'enforce_hostname.EnforceHostnameMiddleware',
        ... other middleware
    ]

Set the following setting to be either a single allowed host, or a list of allowed hosts:

    ENFORCE_HOSTNAME = 'yourapp.com'

That's it!
