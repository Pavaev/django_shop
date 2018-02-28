from decimal import Decimal
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from orders.forms import CheckoutContactForm
from orders.models import ProductInBasket, ProductInOrder, Order


def basket_addition(request):
    return_dict = {}
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id")
    count = data.get("count")

    is_delete = data.get("is_delete")
    if is_delete == 'true':
        ProductInBasket.objects.get(id=product_id).delete()
    else:
        product_existed, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id)
        if not created:
            product_existed.count += int(count)
            product_existed.save(force_update=True)

    products = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_count = 0
    return_dict["products"] = list()
    return_dict["total_amount"] = 0
    for product in products:
        products_total_count += product.count
        product_dict = {"id": product.id, "name": product.product.name, "price_per_item": product.price_per_item,
                        "count": product.count}
        return_dict["products"].append(product_dict)
        return_dict["total_amount"] += product.price_per_item * product.count
    return_dict["products_total_count"] = products_total_count
    return JsonResponse(return_dict)


def checkout(request):
    products_in_basket = ProductInBasket.objects.filter(session_key=request.session.session_key)
    contact_form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if contact_form.is_valid():
            print("yes")
            data = request.POST
            name = data.get("name", "No name")
            phone = data["phone"]
            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})

            order = Order.objects.create(user=user, name=name, phone=phone, status_id=4, total_price=Decimal(0))
            print(order)
            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    product_in_basket.count = value
                    product_in_basket.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_basket.product,
                                                  count=product_in_basket.count,
                                                  price_per_item=product_in_basket.price_per_item,
                                                  total_price=product_in_basket.total_price,
                                                  order=order)

    return render(request, 'orders/checkout.html', locals())
