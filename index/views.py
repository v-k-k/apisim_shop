from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *
from .models import *
import re
import uuid


def home(request):

    return render(request, 'index.html', locals())


def obo_mne(request):

    return render(request, 'obo_mne.html', locals())


def media(request):

    return render(request, 'media-files.html', locals())


def products(request):#, product_id=None):
    product = Product_img.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_nastoiki = product.filter(product__category__id=3)
    products_clear = product.filter(product__category__id=2)
    products_honey = product.filter(product__category__id=1)
    return render(request, 'products.html', locals())


def contacts(request):

    return render(request, 'contacts.html', locals())


def checkout(request):

    return render(request, 'checkout.html', locals())


def consult(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        #print(request.POST)
        ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        new_form = form.save()
        Subscriber.objects.filter(id=new_form.id).update(ip=ip, mac=mac)

    return render(request, 'consult.html', locals())

'''
def product(request):
    product = Product_img.objects.filter(is_active=True, is_main=True)
    return render(request, 'product.html', locals())
'''


def glavnaya(request):

    return render(request, 'index.html', locals())
