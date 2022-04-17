from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartView, name='cart'),
    path('addToCart/<int:productId>', views.AddToCart, name='addToCart'),
    path('removeFromCart/<int:cartItemId>', views.removeFromCart, name='removeFromCart'),
    path('decreaseItemInCart/<int:cartItemId>', views.decreaseItemInCart, name='decreaseItemInCart'),
]