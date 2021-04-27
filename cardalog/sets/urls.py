from django.urls import path

from sets.views import SetListView

urlpatterns = [
    path('list/', SetListView.as_view(), name='set-list'),
]