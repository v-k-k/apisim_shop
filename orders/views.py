from django.http import JsonResponse
from .models import *
from django.shortcuts import render
from .forms import CheckoutContactForm
from django.contrib.auth.models import User
import re
import uuid


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("prod_id")
    number = data.get("number")
    is_delete = data.get("is_delete")
    if is_delete == 'true':
        Product_in_basket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = Product_in_basket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                       is_active=True, defaults={"number": number})
        if not created:
            new_product.number += int(number)
            new_product.save(force_update=True)

    products_in_basket = Product_in_basket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()

    return_dict["products_total_nmb"] = products_total_nmb
    return_dict["products"] = list()
    for i in products_in_basket:
        product_dict = dict()
        product_dict["id"] = i.id
        product_dict["name"] = i.product.name
        product_dict["price_per_item"] = i.price_per_item
        product_dict["number"] = i.number
        return_dict["products"].append(product_dict)
    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = Product_in_basket.objects.filter(session_key=session_key, is_active=True)#.exclude(order__isnull=True)
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
            mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
            #print(ip, mac)
            data = request.POST
            name = data.get("name", "777")
            phone = data["phone"]
            consult_request = email = ""
            if "consult_request" in data:
                consult_request = data["consult_request"]
            if "email" in data:
                email = data["email"]
            print(data)
            print(email)
            temp = 0.0
            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})
            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=1, ip=ip, mac=mac, customer_email=email, consult_request=consult_request)
            for k, v in data.items():
                if k.startswith("product_in_basket_"):
                    product_in_basket_id = k.split('product_in_basket_')[1]
                    product_in_basket = Product_in_basket.objects.get(id=product_in_basket_id)
                    product_in_basket.number = v
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)
                    Product_in_order.objects.create(product=product_in_basket.product, number=product_in_basket.number,
                                                    price_per_item=product_in_basket.price_per_item,
                                                    total_price=product_in_basket.total_price,
                                                    order=order)
        else:
            print('huy')
    else:
        print("ASS")
    return render(request, 'checkout.html', locals())
