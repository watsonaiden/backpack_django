from django.urls import path, include
from .views import (FolderListView,
                    DocView,
                    DocDetailView,
                    ajax_autosave,
                    ajax_createfolder)

urlpatterns = [
    path('ajax/', ajax_autosave, name='ajax_autosave'),
    path('ajax/create/', ajax_createfolder, name='create_folder'),
    path('', FolderListView.as_view(), name='folders'),
    path('<str:folder_title>/', DocView.as_view(), name ='doc_list'),
    path('<str:folder_title>/<str:pk>/', DocDetailView.as_view(), name='doc_detail'),

]
