from django.test import TestCase
from django.test.utils import override_settings


class EnforceHostTestCase(TestCase):
    @override_settings(ENFORCE_HOST="enforced.com")
    def test_single_host_allowed(self):
        response = self.client.get("/", HTTP_HOST="enforced.com")
        self.assertEqual(response.status_code, 200)

    @override_settings(ENFORCE_HOST=["enforced.com", "enforced2.com"])
    def test_multiple_hosts_allowed(self):
        response = self.client.get("/", HTTP_HOST="enforced2.com")
        self.assertEqual(response.status_code, 200)

    @override_settings(ENFORCE_HOST="enforced.com")
    def test_basic_redirect(self):
        response = self.client.get("/", HTTP_HOST="original.com")
        self.assertRedirects(
            response,
            "http://enforced.com/",
            status_code=301,
            fetch_redirect_response=False,
        )

    @override_settings(ENFORCE_HOST=["enforced.com", "enforced2.com"])
    def test_redirect_to_first_in_list(self):
        response = self.client.get("/", HTTP_HOST="original.com")
        self.assertRedirects(
            response,
            "http://enforced.com/",
            status_code=301,
            fetch_redirect_response=False,
        )

    @override_settings(ENFORCE_HOST="enforced.com")
    def test_all_url_components_are_preserved(self):
        response = self.client.get(
            "/foo/bar/?foo=bar",
            HTTP_HOST="original.com",
            HTTP_X_FORWARDED_PROTO="https",
        )
        self.assertRedirects(
            response,
            "https://enforced.com/foo/bar/?foo=bar",
            status_code=301,
            fetch_redirect_response=False,
        )
