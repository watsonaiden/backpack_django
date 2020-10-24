from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from .models import Folder
from django.urls import reverse
import json
# Create your tests here.


class test_folderCreate(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': '12345'}
        User.objects.create_user(**self.credentials)

    def test_folder(self):
        c = Client()
        logged_in = c.login(username='testuser', password='12345')
        self.assertTrue(logged_in)
        response = c.post(
            reverse('create_folder'),
            data={
            'title': 'testFolder',
            'desc': ''},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
            )
        
        content = json.loads(response.content)
        value = content['success']
        self.assertEqual(value, 1)
        
    
