from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm



class HomePageView(TemplateView):
    template_name = 'home.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    
