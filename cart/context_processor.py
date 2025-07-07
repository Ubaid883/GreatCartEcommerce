from .models import Cart, CartIteam
from .views import _cart_id


def counter(request):
    cart_count = 0
    try :
        cart = Cart.objects.filter(cart_id= _cart_id(request))
        cart_itams = CartIteam.objects.all().filter(cart=cart[:1])
        cart_count = sum(iteam.quantity for iteam in cart_itams)
    except Cart.DoesNotExist:
        cart_count = 0
    return dict(cart_count=cart_count)


                
            