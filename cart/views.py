from django.shortcuts import render, redirect   
from store.models import Product
from .models import Cart
from.models import CartIteam


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
       cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id = product_id)
    
    try:
        cart = Cart.objects.get(cart_id =_cart_id(request))  
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id =_cart_id(request)
        )
    cart.save()
    
    try:
        cart_iteam = CartIteam.objects.get(product=product, cart= cart)
        cart_iteam.quantity +=1
        cart_iteam.save()
    except CartIteam.DoesNotExist:
        cart_iteam = CartIteam.objects.create(
            product = product,
            quantity = 1,
            cart = cart ,
        )
        cart_iteam.save()
    return redirect('cart')

# Render Cart Page
def cart(request):
    return render(request, 'cart.html')
