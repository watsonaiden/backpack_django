from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views import generic
from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views import View


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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None: #Verify form's content existence
            if user.is_active: #Verify validity
                login(request, user)
                return redirect('home') #It's ok, so go to index
            
    return render(request, 'home.html', {'state':1})

