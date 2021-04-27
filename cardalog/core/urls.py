from django.urls import path, include
from .views import (
    HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='cardalog-home'),
    # path('sets/', include('sets.urls')),
    path('users/', include('users.urls')),
]
