from django.urls import path

from sets.views import SetListView, SetDetailView, SetCreateView, SetDeleteView

urlpatterns = [
    path('list/', SetListView.as_view(), name='set-list'),
    path('detail/<int:pk>', SetDetailView.as_view(), name='set-detail'),
    path('create/', SetCreateView.as_view(), name='set-create'),
    path('delete/<int:pk>', SetDeleteView.as_view(), name='set-delete'),
]