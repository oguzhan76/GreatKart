from django.urls import path
from . import views

urlpatterns = [
    path('', views.Store, name='store'),
    path('category/<slug:categorySlug>/', views.Store, name='category'),
    path('category/<slug:categorySlug>/<slug:productSlug>/', views.ProductDetail, name= 'productDetail'),
    path('search/', views.search, name='search' ),    
]