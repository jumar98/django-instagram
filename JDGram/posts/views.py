from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from posts.models import Post

# Create your views here.
@login_required
def list_posts(requests):
    posts = Post.objects.all().order_by('-created')
    return render(requests, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
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