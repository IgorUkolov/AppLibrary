from django.urls import path
from .views import *

urlpatterns = [
    path('registration', RegistrationView.as_view(), name='registration'),
]