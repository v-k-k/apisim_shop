from django.contrib import admin
from django.urls import *
from products import views

urlpatterns = [
    #path('product/<int:product_id>', views.product, name='product'),
    re_path(r'^product/(?P<product_id>\w+)$', views.product, name='product'),
]
