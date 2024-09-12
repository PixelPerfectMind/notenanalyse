from audioop import reverse

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout, user_login_failed
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'account/base.html')
