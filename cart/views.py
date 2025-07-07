from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart
from.models import CartIteam
from django.http import HttpResponse


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
    # return HttpResponse(cart_iteam.quantity)
    # exit()
    return redirect('cart')

# Removing Iteam fom Cart
def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id= _cart_id(request))
    product = get_object_or_404(Product,id =product_id)
    cart_iteam = CartIteam.objects.get(cart= cart, product=product)
    if cart_iteam.quantity > 1:
        cart_iteam.quantity -=1
        cart_iteam.save()
    # else:
    #     cart_iteam.delete()
    return redirect ('cart')

#Delete cart Iteam
def delete_cart_itam(request, product_id):
    cart = Cart.objects.get(cart_id= _cart_id(request))
    product = get_object_or_404(Product,id =product_id)
    cart_iteam = CartIteam.objects.get(cart= cart, product=product)
    cart_iteam.delete()
    return redirect('cart')
        

# Render Cart Page
def cart(request, total=0,quantity=0,cart_iteams=None):
    try:
        cart =Cart.objects.get(cart_id = _cart_id(request))
        cart_iteams = CartIteam.objects.filter(cart=cart, is_active=True)
        for cart_iteam in cart_iteams:
            total += (cart_iteam.product.Price * cart_iteam.quantity)
            quantity +=cart_iteam.quantity
        tax = (2 * total)/100   # Calculate 2 % Tax
        grand_total = total + tax          # Calculate Grand Total
    except :
        pass
    context ={
        'total'         : total,
        'quantity'      : quantity,
        'cart_iteams'   :cart_iteams,
        'tax'           : tax,
        'grand_total'   : grand_total
    }
    return render(request, 'cart.html',context)