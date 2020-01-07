
from django.urls import path
from posts.views import PostListView, CreatePostView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('posts/new/', CreatePostView.as_view(), name='create_post'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='detail')
]