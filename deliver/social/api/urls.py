from django.urls import path

from .api_views import PostListCreateApiView, ProfileListApiView

urlpatterns = [
    path('posts/', PostListCreateApiView.as_view(), name='posts'),
    path('users/', ProfileListApiView.as_view(), name='users'),
]

