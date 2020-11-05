from django.test import TestCase
from django.contrib.auth.models import User
from .models import Reminder
import datetime
# Create your tests here.


class test_reminderCreate(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': '12345'}
        
        User.objects.create_user(**self.credentials)
        
    def test_timetil(self):
        date = datetime.datetime.now()
        due_date = date + datetime.timedelta(days=5) + datetime.timedelta(hours=1)
        
        reminder = Reminder.objects.create(title="test", deadline = due_date, user_owner = User.objects.get(username='testuser'))
        print(reminder.days_to_complete())
        self.assertEqual(reminder.days_to_complete(), 5)
        
        
                                        
