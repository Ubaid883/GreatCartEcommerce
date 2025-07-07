from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Categorie
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
        paginator = Paginator(product, 5)  # Show 25 contacts per page.
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        product_count = product.count()
    
    context ={
        'products':page_obj,
        'prouduct_count': product_count,
       
    }
    return render(request, 'store.html', context)


def product_details(request,category_slug,product_slug):
   
    try:
        single_product = Product.objects.get(category__slug=category_slug,Slug=product_slug)
    except Product.DoesNotExist:
        raise Http404("Product not found.")
    context ={
        'single_product': single_product,
         
    }
    return render(request, 'product-detail.html', context)