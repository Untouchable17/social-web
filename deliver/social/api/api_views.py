from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from .serializers import PostSerializer, UserProfileSerializer
from social.models import Post, UserProfile


class PostListApiView(ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title']


class ProfileListApiView(ListAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer