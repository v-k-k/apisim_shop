from django.contrib import admin
from django.urls import path, re_path
from orders import views

urlpatterns = [
    #path('landing/', views.landing, name = 'landing'),
    #path('product/<slug:product_id>/', views.Product, name='product'),
    re_path(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    re_path(r'^checkout', views.checkout, name='checkout'),#re_path(r'^checkout/$', views.checkout, name='checkout'),

]