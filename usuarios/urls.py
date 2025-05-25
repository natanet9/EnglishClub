# usuarios/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

urlpatterns = [
    path('login/', LoginView.as_view(template_name='usuarios/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
