from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse("Hello world! I'm a Home.")
    #return render(request, 'home.html')