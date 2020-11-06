from django.shortcuts import render
from django.views.generic import ListView
from .models import Reminder
from django.db.models import Q
# Create your views here.


class ReminderList(ListView):
    template_name = 'reminder_list.html'
    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Reminder.objects.filter(Q(user_owner=self.request.user))
            return qs
        else:
            return 0
    
