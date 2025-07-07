from .models import Cart, CartIteam
from .views import _cart_id


def counter(request):
    cart_count = 0
    try :
        cart = Cart.objects.get(cart_id= _cart_id(request))
        cart_itams = CartIteam.objects.filter(cart=cart, is_active=True)
        cart_count = sum(iteam.quantity for iteam in cart_itams)
    except Cart.DoesNotExist:
        cart_count = 0
    return dict(cart_count=cart_count)


                
            