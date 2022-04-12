from tkinter import E
from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product

# Create your views here.

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
        'product_count': product_count
    }

    return render(request, 'store/store.html', context)

def ProductDetail(request, categorySlug, productSlug):
    try:
        product = Product.objects.get(category__slug=categorySlug, slug=productSlug)
    except Exception as e:
        raise e

    context = {
        'product': product
    }
    return render(request, 'store/product_detail.html', context)