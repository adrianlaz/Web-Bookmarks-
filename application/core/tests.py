import json

from django.contrib.auth import get_user_model

# Create your tests here.

from rest_framework import test


class BookmarkTests(test.APITestCase):

    def setUp(self):
        self.user_obj = get_user_model()
        self.user = self.user_obj.objects.create_user('user', None, 'Password123')
        self.user2 = self.user_obj.objects.create_user('user2', None, 'Password123')
        self.user.save()
        self.uri = '/my-bookmarks/'
        self.params = {'title': 'new url', 'url': 'www.new-url.com', 'public': True}
        self.data1 = {'title': 'user2 url', 'url': 'www.old-urls.com', 'public': False}
        self.data2 = {'title': 'user2 Public url', 'url': 'www.another-url.com', 'public': True}
        self.contet_type = 'application/json'
        self.client.login(username='user', password='Password123')
        self.response1 = self.client.post(self.uri, data=json.dumps(self.params), content_type=self.contet_type)
        self.client.login(username='user2', password='Password123')
        self.response2 = self.client.post(self.uri, data=json.dumps(self.data1), content_type=self.contet_type)
        self.response3 = self.client.post(self.uri, data=json.dumps(self.data2), content_type=self.contet_type)

    def test_create_bookmark(self):
        response = self.response1
        resp_dict = response.json()
        params = self.params.keys()
        expected_response = {k: v for (k, v) in resp_dict.items() if k in params}

        self.assertEqual(response.status_code, 201)
        self.assertTrue(self.user.is_authenticated)
        self.assertEqual(self.params, expected_response)

    def test_my_bookmark(self):
        self.client.login(username='user2', password='Password123')
        user2_response = self.client.get(self.uri, content_type=self.contet_type)
        resp_list2 = user2_response.json()
        user2_in_response = {i['owner'] for i in resp_list2}.pop()

        self.client.login(username='user', password='Password123')
        user1_response = self.client.get(self.uri, content_type=self.contet_type)
        resp_list1 = user1_response.json()
        user1_in_response = {i['owner'] for i in resp_list1}.pop()

        self.assertEqual(user1_response.status_code, 200)
        self.assertEqual(user2_response.status_code, 200)
        self.assertEqual(user1_in_response, 'user')
        self.assertEqual(user2_in_response, 'user2')
        self.assertEqual(len(resp_list1), 1)
        self.assertEqual(len(resp_list2), 2)
