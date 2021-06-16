# from django.test import TestCase
# from django.contrib.auth.models import User
# from django.core.files.uploadedfile import SimpleUploadedFile
#
# from social.models import Post, Comment, UserProfile
#
#
# class PostTestCases(TestCase):
#
#     def setUp(self) -> None:
#         self.user = User.objects.create(username='testuser', password='password')
#         self.blog = Post.objects.create(
#             author=self.user,
#             title='Our testing Post',
#             slug='our-testing-post',
#             body='we are testing this cases',
#             photo=SimpleUploadedFile("default.jpg", content=b'', content_type='photo/jpg'),
#             created_at='2021-06-14 10:00:09.589721',
#             replace_at='2021-06-14 10:00:09.589721',
#         )
#         self.comment = Comment.objects.create(
#             comment='test case comment',
#             created_at='2021-06-14 10:00:09.589721',
#             author=self.user,
#             post=self.blog,
#         )
#         self.profile = UserProfile(
#             user=self.user,
#             name='Tyler Blackout',
#             bio='bio from user profile',
#             birth_date='2021-06-14',
#             location='USA California',
#             picture=SimpleUploadedFile("default.jpg", content=b'', content_type='photo/jpg')
#         )
#
