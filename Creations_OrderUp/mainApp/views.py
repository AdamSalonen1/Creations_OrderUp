from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mainApp/index.html')

def advertisements(request):
    return render(request, 'mainApp/advertisements.html')

