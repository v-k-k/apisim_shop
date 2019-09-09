from django.conf.urls import *
from django.urls import *
from . import views

urlpatterns = [
    re_path(r'^products', views.products, name='products'),
    #re_path(r'^checkout', views.checkout, name='checkout'),
    re_path(r'^contacts', views.contacts, name='contacts'),
    re_path(r'^consult', views.consult, name='consult'),
    #re_path(r'^product', views.product),
    re_path(r'^index', views.glavnaya, name='index'),
    re_path(r'^media-files', views.media, name='media-files'),
    re_path(r'^obo_mne', views.obo_mne, name='obo_mne'),
    re_path(r'^$', views.home, name='home'),

]