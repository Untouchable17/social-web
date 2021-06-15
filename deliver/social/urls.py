from django.urls import path

from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),

    path('post/<str:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<str:slug>/update/', PostEditView.as_view(), name='post-edit'),
    path('post/<str:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<str:slug>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),

    path('post/<str:slug>/dislike/', Dislike.as_view(), name='dislike'),
    path('post/<str:slug>/like/', AddLike.as_view(), name='like'),

    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/update', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers/add/', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove/', RemoveFollower.as_view(), name='remove-following'),

    path('search/', UserSearch.as_view(), name='profile-search'),

    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread/', CreateThread.as_view(), name='thread-create'),
    path('inbox/<int:pk>/', ThreadDetailView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),
]