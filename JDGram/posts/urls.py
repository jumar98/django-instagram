
from django.urls import path
from posts.views import PostListView, create_post, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('posts/new/', create_post, name='create_post'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='detail')
]