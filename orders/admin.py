from django.contrib import admin
from .models import *


class Product_in_order_inline(admin.TabularInline):
    model = Product_in_order
    extra = 0




class Status_admin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, Status_admin)


class Order_admin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [Product_in_order_inline]

    class Meta:
        model = Order

admin.site.register(Order,Order_admin)




class Product_in_order_admin(admin.ModelAdmin):
    list_display = [field.name for field in Product_in_order._meta.fields]

    class Meta:
        model = Product_in_order

admin.site.register(Product_in_order, Product_in_order_admin)


class Product_in_basket_admin(admin.ModelAdmin):
    list_display = [field.name for field in Product_in_basket._meta.fields]

    class Meta:
        model = Product_in_basket

admin.site.register(Product_in_basket, Product_in_basket_admin)