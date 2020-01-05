from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.db.utils import IntegrityError

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        pw_confirmantion = request.POST.get('password_confirmation')
        if password != pw_confirmantion:
            return render(request, 'users/signup.html', {
                'error': "Password confirmation doesn't match."
                 })
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {
                'error': "This username is already registered."
                 })
        user.first_name =request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        profile = Profile(user=user)
        profile.save()
        
        return redirect('login')
        
    return render(request, 'users/signup.html')