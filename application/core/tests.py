import json

from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

from rest_framework import test


class BookmarkTests(test.APITestCase):

    def setUp(self):
        self.user = get_user_model()
        self.user.objects.create_user('user', None, 'Password123')
        self.uri = '/my-bookmarks/'
        self.client = test.APIClient()
        self.params = {'title': 'new url', 'url': 'www.new-url.com', 'private': False}

    def test_create_bookmark(self):
        client = self.client
        client.login(username='user', password='Password123')
        response = client.post(self.uri, data=json.dumps(self.params), content_type='application/json')
        self.assertEqual(response.status_code, 201)