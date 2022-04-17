from carts.models import CartItem
from .views import _getOrCreateCart

def itemCountInCart(request):
    if 'admin' in request.path:
        return {}
    itemCount = 0
    try:
        cart = _getOrCreateCart(request)
        cartItems = CartItem.objects.all().filter(cart=cart)
        for item in cartItems:
            itemCount += item.quantity
            # print('Successfull')
    except:
        pass
    return dict(itemCount = itemCount)