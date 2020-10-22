from django.shortcuts import render
from django.views.generic import ListView, DetailView,UpdateView
from .models import Folder, Document
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse


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
    template_name = "doc_list.html"
    def get_queryset(self):
        if self.request.user.is_authenticated:
            folder = Folder.objects.get(user_owner=self.request.user, title=self.kwargs['folder_title'])
            qs = folder.document_set.all()
            return qs
        else:
            return 0
    


class DocDetailView(UpdateView):
    model = Document
    fields = ('title','body')
    template_name = "doc_detail.html"
    def get_object(self): #using get_object instead of queryset since only one object returned
        if self.request.user.is_authenticated:
            folder = Folder.objects.get(user_owner=self.request.user, title=self.kwargs['folder_title'])
            qs = Document.objects.get(folder_parent=folder, title=self.kwargs['pk'])
            return qs
        else:
            return 0




def ajax_autosave(request):
    if request.method == 'POST' and request.is_ajax():
        title = request.POST.get('title')
        body = request.POST.get('body')
        my_pk = request.POST.get('pk')
        saving_doc = Document.objects.filter(pk=my_pk)
        saving_doc.update(title = title, body = body)
        return JsonResponse({"success":1})

def createFolder_view(request):
    return render(request,'create_folder.html')

