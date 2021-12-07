from django.urls import path, include
from .views import SignUpView, MyLoginView, PasswordResetView
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # TODO: check the urls and remove the redundant linked views.
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', user_views.profile, name='profile'),

    # Password Reset related urls
    path('password_reset/', PasswordResetView.as_view(template_name='password/password_reset.html'), name='password-reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='/password/password_reset_complete.html'), name='password_reset_complete'),
]