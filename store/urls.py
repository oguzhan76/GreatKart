from django.urls import path
from . import views

urlpatterns = [
    path('', views.Store, name='store'),
    path('<slug:categorySlug>/', views.Store, name='category'),
    path('<slug:categorySlug>/<slug:productSlug>/', views.ProductDetail, name= 'productDetail')
]