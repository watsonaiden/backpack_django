from django.test import TestCase
from django.contrib.auth.models import User
from .forms import SignUpForm
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
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        response = self.client.post('/accounts/login', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(last_url, '/')
