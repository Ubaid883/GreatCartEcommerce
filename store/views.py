from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Categorie


# Create your views here.
def Store(request, category_slug=None):
    categories = None
    product = None
    if category_slug != None:
        categories = get_object_or_404(Categorie, slug = category_slug)
        product = Product.objects.filter(category=categories, is_available=True)
        product_count = product.count()
    else:
        product = Product.objects.all().filter(is_available=True)
        product_count = product.count()
    
    context ={
        'products':product,
        'prouduct_count': product_count
    }
    return render(request, 'store.html', context)