__version__ = "1.1.0"

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django.http import HttpResponsePermanentRedirect


class EnforceHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        setting_value = getattr(settings, "ENFORCE_HOST", None)

        if setting_value is None:
            raise MiddlewareNotUsed()

        if isinstance(setting_value, str):
            setting_value = [setting_value]

        self.allowed_hosts = setting_value

    def __call__(self, request):
        host = request.get_host()

        if host in self.allowed_hosts:
            return self.get_response(request)

        new_url = "%s://%s%s" % (
            "https" if request.is_secure() else "http",
            self.allowed_hosts[0],
            request.get_full_path(),
        )

        return HttpResponsePermanentRedirect(new_url)
