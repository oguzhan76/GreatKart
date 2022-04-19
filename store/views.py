from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product
from carts.views import _getCartId
from carts.models import CartItem
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def Store(request, categorySlug=None):
    categories = None
    products = None

    if categorySlug != None:
        categories = get_object_or_404(Category, slug=categorySlug)
        products = Product.objects.all().filter(category=categories)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    else:
        products = Product.objects.all()
        #Paginator
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)


    product_count = products.count()
    context = {
        'products': paged_products,
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


def search(requests):
    if 'keyword' in requests.GET:
        keyword = requests.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-date_created').filter(Q(description__icontains=keyword) | Q(name__icontains=keyword)) # Use Q to be able to use OR operator
    product_count = products.count()
    context = { 
        'products': products,
        'product_count': product_count
        }
    print(*list(products))
    return render(requests, 'store/store.html', context)