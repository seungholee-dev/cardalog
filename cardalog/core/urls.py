from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('sets/', include('sets.urls')),
    path('users/', include('users.urls')),
]