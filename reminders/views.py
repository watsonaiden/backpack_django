from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from .models import Reminder
from django.db.models import Q
from django.db import IntegrityError
from django.http import JsonResponse

# Create your views here.


class ReminderList(ListView):
    template_name = 'reminder_list.html'
    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Reminder.objects.filter(Q(user_owner=self.request.user))
            return qs
        else:
            return 0


def ajax_createReminder(request):
    if request.method == 'POST' and request.is_ajax():
        title = request.POST.get('title')
        description = request.POST.get('desc')
        deadline = request.POST.get('deadline')
        try:
            reminder = Reminder.objects.create(title=title, description=description,
                                    deadline=deadline, user_owner=request.user)
            return JsonResponse({"success":1,
                                 "url": reminder.get_view_url()})
        except IntegrityError:
            return JsonResponse({"success":0})
    return JsonResponse({"success":0})


class Reminder_detail(DetailView):
    template_name = 'reminder_detail.html'
    model = Reminder
    
def delete_reminder(request, pk):
    reminder = Reminder.objects.get(pk=pk)
    if reminder.user_owner != request.user:
        return HttpResponse("Don't have permission to delete this reminder")
    else:
        reminder.delete()
    return redirect("reminders")

def ajax_autosave(request):
    if request.method == 'POST' and request.is_ajax():
        pk = request.POST.get('pk')
        description = request.post.get('desc')
        user = request.user
        try:
            saving_reminder = Reminder.objects.get(pk=pk, user_owner=user)
            saving_doc.update(description=description)
            return JsonResponse({"success":1})
        except IntegrityError:
            return JsonResponse({"success": 0})


    
        
    
        
        


