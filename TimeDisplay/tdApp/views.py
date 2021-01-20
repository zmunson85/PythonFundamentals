from django.http import HttpResponse
from django.shortcuts import render
import datetime

def index(request):
    return HttpResponse("Hello, world")

def showdate(request):
    datetime.datetime.now()
    
    return render(request, 'index.html')


def showtime(request):
    datetime.datetime.now()

    return render(request, 'index.html')
