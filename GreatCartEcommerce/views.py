from django.http import HttpRequest
from django.shortcuts import render
from store.models import Product
def Home(request):
    product = Product.objects.all().filter(is_available=True)
    
    return render (request, 'index.html',{'products':product})