from django.urls import path

from sets.views import SetListView, SetDetailView

urlpatterns = [
    path('list/', SetListView.as_view(), name='set-list'),
    path('detail/<int:pk>', SetDetailView.as_view(), name='set-detail'),
]