from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name= 'signup.html'
    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, user)
        return valid




class LoginView(generic.CreateView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'login.html'
