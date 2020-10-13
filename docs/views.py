from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Folder, Document
from django.db.models import Q


# Create your views here.

class FolderListView(ListView):
    model = Folder
    template_name = 'folder_list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Folder.objects.filter(Q(user_owner=self.request.user))
            return qs
        else:
            return 0

class DocView(ListView):
    model = Document
    template_name = "Doc.html"
    def get_queryset(self):
        if self.request.user.is_authenticated:
            folder = Folder.objects.get(user_owner=self.request.user, title=self.kwargs['title'])
            qs = folder.document_set.all()
            return qs
        else:
            return 0
        


class DocDetailView(DetailView):
    model = Document
    template_name = "doc_detail.html"
