from django.http.request import HttpRequest
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def abc(request):
    return render(request, 'app/abc.html')