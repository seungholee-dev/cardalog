from django.urls import path

from sets.views import SetListView, SetDetailView, SetCreateView, SetDeleteView, SetUpdateView

urlpatterns = [
    path('list/', SetListView.as_view(), name='set-list'),
    path('<int:pk>/detail/', SetDetailView.as_view(), name='set-detail'),
    path('create/', SetCreateView.as_view(), name='set-create'),
    path('<int:pk>/delete/', SetDeleteView.as_view(), name='set-delete'),
    path('<int:pk>/update', SetUpdateView.as_view(), name='set-update'),
]