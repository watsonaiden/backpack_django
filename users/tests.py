from django.test import TestCase
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.urls import reverse
import json
# Create your tests here.


class test_signup(TestCase):
    def setUp(self):
        self.credentials = {'email':'test@gmail.com',
                 'username':'testuser',
                 'password1':'password$$',
                 'password2':'password$$'}
    def test_forms(self):
        form = SignUpForm(data=self.credentials)
        self.assertTrue(form.is_valid)
    def test_signupview(self):
        response = self.client.post('/accounts/signup', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(last_url,'/')
                     
class test_Login(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
    def test_login(self):
        response = self.client.post(
            reverse('login_auth'),
            data={
            'username': 'testuser',
            'password': '12345'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
            )
        content = json.loads(response.content)
        value = content['success']
        self.assertEqual(value, 1)
