from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Cart, CartItem
from store.models import Product

# Create your views here.
def _getCartId(request):
    cartId = request.session.session_key
    if not cartId:
        cartId = request.session.create()
    return cartId

def _getOrCreateCart(request):
    try:
        cart = Cart.objects.get(cart_id=_getCartId(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_getCartId(request))
        cart.save()
    return cart

def _getCartItem(cartItemId):
    try:
        item = CartItem.objects.get(id=cartItemId)
    except CartItem.DoesNotExist:
        print('No such item')
        return redirect('cart')
    return item

def AddToCart(request, productId):
    product = Product.objects.get(id=productId)
    cart = _getOrCreateCart(request)

    #Get or create cartItem for the product that is wanted to be added to the cart
    try: #If the cart has already got the same product - hence cartItem - we just increase quantity 
        cartItem = CartItem.objects.get(product=product, cart=cart)
        cartItem.quantity += 1
        cartItem.save()
    except CartItem.DoesNotExist:
        cartItem = CartItem.objects.create(product=product, cart=cart, quantity=1)
        cartItem.save()
    #return HttpResponse(productId)
    return redirect('cart')

def decreaseItemInCart(request, cartItemId):
    item = _getCartItem(cartItemId)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart')

def removeFromCart(request, cartItemId):
    item = _getCartItem(cartItemId)
    item.delete()
    return redirect('cart')


def CartView(request, total=0, quantity=0, cartItems=None):
    cart = _getOrCreateCart(request)
    cartItems = CartItem.objects.filter(cart=cart, is_active=True)
    for item in cartItems:
        total += item.product.price * item.quantity
        quantity += item.quantity
    tax = total * 0.02 # %2 tax
    grandTotal = total + tax
    context = {
        'total': total,
        'quantity': quantity,
        'cartItems': cartItems,
        'tax': tax,
        'grandTotal': grandTotal
    }

    return render(request, 'Carts/cart.html', context)