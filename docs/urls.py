from django.urls import path, include
from .views import FolderListView, DocView, DocDetailView

urlpatterns = [
    path('', FolderListView.as_view(), name='folders'),
    path('<str:folder_title>', DocView.as_view(), name ='doc_list'),
    path('<str:folder_title>/<str:pk>', DocDetailView.as_view(), name='doc_detail'),
    
]
