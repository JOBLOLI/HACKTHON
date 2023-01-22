from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Login(request):
    return HttpResponse('login page')

def grafana(request):
    return HttpResponse('the grafana page')

def setpreferences(request):
    return HttpResponse('settings')
