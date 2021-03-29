from django.urls import path, include
from .views import SignUpView, MyLoginView

urlpatterns = [
    path('register/', SignUpView.as_view(template_name='registration/register.html'), name='register'),
    path('login/', MyLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', .as_view(template_name='registration/login.html'), name='logout')
]
