from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request, 'templates/home.html')