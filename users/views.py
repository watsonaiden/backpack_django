from .forms import SignUpForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name= 'signup.html'
    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, user)
        return valid


def Login_auth(request):
    if request.method == 'POST' and request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        data ={}
        if user is not None:
            login(request, user)
            data['success'] = 1
            return JsonResponse(data)
        else:
            data['success'] = 0    
            return JsonResponse(data)

    
class ChangePassView(auth_views.PasswordChangeView):
    success_url = reverse_lazy('home')
    template_name = 'changepass.html'
    
