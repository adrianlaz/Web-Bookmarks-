import json

from django.contrib.auth import get_user_model

# Create your tests here.

from rest_framework import test


class BookmarkTests(test.APITestCase):

    def setUp(self):
        self.user_obj = get_user_model()
        self.user = self.user_obj.objects.create_user('user', None, 'Password123')
        self.user.save()
        self.uri = '/my-bookmarks/'
        self.params = {'title': 'new url', 'url': 'www.new-url.com', 'public': True}

    def test_create_bookmark(self):
        self.client.login(username='user', password='Password123')
        response = self.client.post(self.uri, data=json.dumps(self.params), content_type='application/json')
        resp_dict = response.json()
        params = self.params.keys()
        expected_response = {k: v for (k, v) in resp_dict.items() if k in params}

        self.assertEqual(response.status_code, 201)
        self.assertTrue(self.user.is_authenticated)
        self.assertEqual(self.params, expected_response)