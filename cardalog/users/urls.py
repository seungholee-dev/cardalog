from django.urls import path, include
from .views import SignUpView, MyLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', SignUpView.as_view(template_name='registration/register.html'), name='register'),
    path('login/', MyLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
