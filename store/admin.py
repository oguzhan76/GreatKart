from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'date_modified', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)