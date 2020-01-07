
from django.urls import path
from posts.views import PostListView, create_post

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('new/', create_post, name='create_post'),
]