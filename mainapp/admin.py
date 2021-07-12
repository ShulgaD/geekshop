from django.contrib import admin
# from geekshop.mainapp.models import ProductCategory, Product
from mainapp.models import ProductCategory, Product

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)
