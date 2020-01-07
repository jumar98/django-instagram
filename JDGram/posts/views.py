from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from posts.models import Post
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
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
    
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:posts')
    else:
        form = PostForm()

    return render(
            request=request,
            template_name='posts/new_post.html',
            context={
                'form': form,
                'user': request.user,
                'profile': request.user.profile
            }
        )