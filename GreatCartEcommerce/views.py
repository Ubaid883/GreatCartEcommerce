from django.http import HttpRequest
from django.shortcuts import render

def Home(request):
    return render (request, 'index.html')