from django.test import TestCase
from django.test.client import Client


class MashaTemplatetagsTest(TestCase):
    def startUp(self):
        self.client = Client()

    def test_load_simple(self):
        response = self.client.get('/')
        print response
