from django.shortcuts import render
from django.http import HttpResponse
from .forms import User

def get_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = User(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'grafana.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = User()

    return render(request, 'login.html', {'form': form})

def Login(request):
    return render(request, 'login.html')

def grafana(request):
    return render(request, 'grafana.html')

def setpreferences(request):
    return render(request, 'settings.html')
