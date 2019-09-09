from django.contrib import admin
from .models import *


class Prod_img_inline(admin.TabularInline):
    model = Product_img
    extra = 0
class Product_category_admin(admin.ModelAdmin):
    list_display = [field.name for field in Product_category._meta.fields]

    class Meta:
        model = Product_category

admin.site.register(Product_category, Product_category_admin)

class Product_admin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [Prod_img_inline]


    class Meta:
        model = Product

admin.site.register(Product, Product_admin)

class Product_img_admin(admin.ModelAdmin):
    list_display = [field.name for field in Product_img._meta.fields]

    class Meta:
        model = Product_img

admin.site.register(Product_img, Product_img_admin)