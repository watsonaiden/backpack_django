from django.shortcuts import render
from django.views.generic import ListView
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
                                 "pk": reminder.pk})
        except IntegrityError:
            return JsonResponse({"success":0})
    return JsonResponse({"success":0})
            

        
        


