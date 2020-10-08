from django.urls import path, include
from .views import FolderListView

urlpatterns = [
    path('', FolderListView.as_view(), name='folders'),
]
