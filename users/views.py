from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class LoginView(generic.CreateView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'login'
