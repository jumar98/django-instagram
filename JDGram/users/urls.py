from django.urls import path
from users.views import login_view, logout_view, SignUpView, UpdateProfileView, UserDetailView

urlpatterns = [
    path('<str:username>', UserDetailView.as_view(template_name='users/detail.html'), name='detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('me/profile/', UpdateProfileView.as_view(), name='update_profile')
]