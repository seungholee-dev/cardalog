from django.urls import path
from .views import SignUpView, MyLoginView
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', SignUpView.as_view(template_name='registration/register.html'), name='register'),
    path('login/', MyLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', user_views.abc, name='profile'),
]
