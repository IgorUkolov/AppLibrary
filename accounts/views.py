from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class RegistrationView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('main')
    template_name = 'registration/register.html'
