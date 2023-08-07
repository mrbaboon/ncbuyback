from django.test import TestCase


class ApplicationTestCase(TestCase):
    def test__foo(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp["Location"], "/account/login/?next=/")
