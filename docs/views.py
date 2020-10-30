from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView,UpdateView
from .models import Folder, Document
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse
from django.db import IntegrityError


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

def ajax_createfolder(request):
    if request.method == 'POST' and request.is_ajax():
        title = request.POST.get('title')
        description = request.POST.get('desc')
        try:
            Folder.objects.create(title = title,
                                description=description,
                                user_owner = request.user)
            return JsonResponse({"success":1})
        
        except IntegrityError as e:
            raise ViewException(format, str(e), 404)
    return JsonResponse({"failure":1})

def ajax_createdocument(request):
    if request.method == 'POST' and request.is_ajax():
        title = request.POST.get('title')
        folder_title = request.POST.get('folder_title')
        folder = Folder.objects.get(user_owner=request.user,
                                    title=folder_title)
        try:
            document = Document.objects.create(
                                title = title,
                                folder_parent= folder)
            return JsonResponse({"success":1,
                                "title": document.title })
        
        except IntegrityError as e:
            raise ViewException(format, str(e), 404)
    return JsonResponse({"sucess":0})
                      
def delete_folder(request,pk): 
    folder = Folder.objects.get(pk=pk)
    if folder.user_owner != request.user:
        return HttpResponse("you do not have permission to delete this folder")
    folder.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def delete_document(request,pk): 
    Doc = Document.objects.get(pk=pk)
    if Doc.folder_parent.user_owner != request.user:
        return HttpResponse("you do not have permission to delete this folder")
    Doc.delete()
    return redirect(request.META.get('HTTP_REFERER'))
