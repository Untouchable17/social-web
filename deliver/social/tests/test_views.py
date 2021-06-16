from social.views import *
from rest_framework import status
from django.test import TestCase


class ViewApiTestCase(TestCase):
    def test_post_list_url(self):
        url = reverse('post-list')
        response = self.client.get(url)

        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
