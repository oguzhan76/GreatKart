from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product
from carts.views import _getCartId, _getOrCreateCart
from carts.models import CartItem

# Create your views here.

def _isProductInCart(request, product):
    cart = _getOrCreateCart(request)
    try:
        item = CartItem.objects.get(product=product, cart=cart)
        return True
    except CartItem.DoesNotExist:
        return False

def Store(request, categorySlug=None):
    categories = None
    products = None

    if categorySlug != None:
        categories = get_object_or_404(Category, slug=categorySlug)
        products = Product.objects.all().filter(category=categories)
    else:
        products = Product.objects.all()
    
    product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)

def ProductDetail(request, categorySlug, productSlug):
    try:
        product = Product.objects.get(category__slug=categorySlug, slug=productSlug)
    except Exception as e:
        raise e

    incart = CartItem.objects.filter(product=product, cart__cart_id=_getCartId(request)).exists()
    context = {
        'product': product,
        'inCart': incart,
    }
    return render(request, 'store/product_detail.html', context)