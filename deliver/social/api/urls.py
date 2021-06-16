from django.urls import path

from .api_views import PostListApiView, ProfileListApiView

urlpatterns = [
    path('posts/', PostListApiView.as_view(), name='posts'),
    path('users/', ProfileListApiView.as_view(), name='users'),
]

