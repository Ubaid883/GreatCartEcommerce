from django.http import HttpRequest
from django.shortcuts import render
from store.models import Product
from django.http import Http404


def Home(request):
    try:
        product = Product.objects.all().filter(is_available=True)
    
        context ={
        'products':product
        }
    
        return render (request, 'index.html',context)
    except:
        raise Product.DoesNotExist
    
        
    



