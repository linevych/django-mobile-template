from django.test import TestCase
try:
    from django.shortcuts import reverse
except:
    from django.core.urlresolvers import reverse


class MobileViewTestCase(TestCase):
    def test_desktop_view(self):
        response = self.client.get(reverse('home'))
        self.assertIn(b'<title>Desktop template</title>', response.content)

    def test_mobile_view(self):
        response = self.client.get(reverse('home'), SERVER_NAME='m.localhost')
        self.assertIn(b'<title>Mobile template</title>', response.content)
