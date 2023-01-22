from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Login(request):
    return render(request, 'login.html')

def grafana(request):
    return render(request, 'grafana.html')

def setpreferences(request):
    return render(request, 'settings.html')
