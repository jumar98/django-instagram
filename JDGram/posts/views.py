from posts.forms import PostForm
from posts.models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

class PostListView(LoginRequiredMixin, ListView):

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 1
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'
    
class CreatePostView(LoginRequiredMixin, CreateView):

    template_name = 'posts/new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
