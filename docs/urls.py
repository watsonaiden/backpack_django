from django.urls import path, include
from .views import FolderListView, DocView

urlpatterns = [
    path('', FolderListView.as_view(), name='folders'),
    path('<str:pk>', DocView.as_view(), name ='doc_list'),
    
]
