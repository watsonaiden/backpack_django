from django.urls import path, include
from .views import ReminderList,ajax_createReminder

urlpatterns = [
    path('', ReminderList.as_view(), name='reminders'),
    path('ajax/reminder_create', ajax_createReminder, name="create_reminder"),
]
