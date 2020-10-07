from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="timothy", password="timothypass")
        User.objects.create_user(username="jimbob", password='jimbobpass')
        
    def correct_info(self):
        tim = User.objects.get(username='timothy')
        jimbob = User.objects.get(username='jimbob')
        
        self.assertEqual(tim.get_username() == 'timothy')
        self.assertEqual(jimbob.get_username() == 'jimbob')



        
