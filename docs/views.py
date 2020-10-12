from django.shortcuts import render
from django.views.generic import ListView
from .models import Folder, Document
from django.db.models import Q


# Create your views here.

class FolderListView(ListView):
    model = Folder
    template_name = 'folder_list.html'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            qs = super(FolderListView, self).get_queryset(*args, **kwargs)
            qs = qs.filter(user_owner__exact=self.request.user)
            return qs
        else:
            return 0

class DocView(ListView):
    model = Document
    template_name = "Doc.html"
