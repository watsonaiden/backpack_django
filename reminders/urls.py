from django.urls import path, include
from .views import (ReminderList,
                    ajax_createReminder,
                    Reminder_detail,
                    ajax_autosave,
                    delete_reminder)

urlpatterns = [
    path('', ReminderList.as_view(), name='reminders'),
    path('ajax/reminder_create', ajax_createReminder, name="create_reminder"),
    path('<int:pk>', Reminder_detail.as_view(), name='reminder_detail'),
    path('ajax/auto_save', ajax_autosave, name="save_notes"),
    path('<int:pk>/delete_reminder', delete_reminder, name="delete_reminder"),
]
