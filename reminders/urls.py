from django.urls import path, include
from .views import ReminderList

urlpatterns = [
    path('', ReminderList.as_view(), name='reminders'),

]
