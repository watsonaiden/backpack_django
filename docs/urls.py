from django.urls import path, include
from .views import (FolderListView,
                    DocView,
                    DocDetailView,
                    ajax_autosave,
                    ajax_createfolder,
                    ajax_createdocument)

urlpatterns = [
    path('ajax/save/', ajax_autosave, name='ajax_autosave'),
    path('ajax/create/folder', ajax_createfolder, name='create_folder'),
    path('ajax/create/document', ajax_createdocument, name='create_document'),
    path('', FolderListView.as_view(), name='folders'),
    path('<str:folder_title>/', DocView.as_view(), name ='doc_list'),
    path('<str:folder_title>/<str:pk>/', DocDetailView.as_view(), name='doc_detail'),

]
