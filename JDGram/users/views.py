from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from users.forms import ProfileForm, SignUpForm

# Create your views here.

def login_view(request):
    """"Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'users/login.html', {'error': "Invalid user or password"})
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Logout view"""
    logout(request)
    return redirect('login')

def signup_view(request):
    """Sign up view"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')
    else:
        form = SignUpForm()
    
    return render(
        request=request,
        template_name='users/signup.html',
        context={
            'form': form
        }
    )
@login_required
def update_profile(request):
    """Update profile from users"""
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.biography = data.get('biography')
            profile.phone_number = data.get('phone_number')
            profile.picture = data.get('picture')
            profile.website = data.get('website')
            profile.save()
            return redirect('update_profile')
    else:
        form = ProfileForm()
    return render(
        request=request, 
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user': request.user,
            'form': form
        })