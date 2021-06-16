from collections import OrderedDict

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from social.models import Post, UserProfile
from .serializers import PostSerializer, UserProfileSerializer


""" 
    class ListApiView позволяет нам получать исключительно
    некий список объектов с данной модели и ничего более
    
    class ListCreateApiView позволяет нам делать POST запрос
    
    class RetrieveUpdateAPIView позволяет делать PUT запрос
"""


class PostPagination(PageNumberPagination):
    """ Пагинация для PostListApiView """

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        """ Переопределяем вывод значений элементов (кастомизация) """
        return Response(OrderedDict([
            ('objects_count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('items', data)
        ]))


class PostListCreateApiView(ListCreateAPIView, RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination

    lookup_field = 'id'

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title']


class ProfileListApiView(ListAPIView):
    """ Забирает всех пользователей из модели UserProfile """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
