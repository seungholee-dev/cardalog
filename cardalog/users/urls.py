from django.urls import path, include
from .views import SignUpView

urlpatterns = [
    path('', include("django.contrib.auth.urls")), #includes login, logout, etc...
    path('register/', SignUpView.as_view(template_name='registration/register.html'), name='register')
]
