from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User

from social.api.serializers import PostSerializer
from social.models import Post


class PostApiTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.blog = Post.objects.create(
            author=self.user,
            title='agagagagagagagag',
            slug='agagagagagagagag',
            body='agagagagagagagagagagagagagagagag',
            photo=SimpleUploadedFile("default.jpg", content=b'', content_type='photo/jpg'),
            created_at='2021-06-14 10:00:09.589721',
            replace_at='2021-06-14 10:00:09.589721',
        )

    def test_get(self):
        url = reverse('posts')
        response = self.client.get(url)
        serializer_data = PostSerializer(self.blog).data
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(serializer_data, response.data)
