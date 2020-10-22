from django.urls import path, include
from .views import FolderListView, DocView, DocDetailView,ajax_autosave, createFolder_view

urlpatterns = [
    path('ajax/', ajax_autosave, name='ajax_autosave'),
    path('', FolderListView.as_view(), name='folders'),
    path('create/', createFolder_view, name='create_folder'),
    path('<str:folder_title>/', DocView.as_view(), name ='doc_list'),
    path('<str:folder_title>/<str:pk>/', DocDetailView.as_view(), name='doc_detail'),

]
