from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    return render(request, 'notenanalyse/index.html')