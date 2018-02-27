from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from orders.models import ProductInBasket


def basket_addition(request):
    return_dict = {}
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id");
    count = data.get("count")

    try:
        product_existed = ProductInBasket.objects.get(session_key=session_key, product_id=product_id)
        product_existed.count += int(count)
        product_existed.save()
    except ObjectDoesNotExist:
        ProductInBasket.objects.create(session_key=session_key, product_id=product_id, count=count)
    finally:
        products = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
        products_total_count = 0
        for product in products:
            products_total_count += product.count
        return_dict["products_total_count"] = products_total_count
        return JsonResponse(return_dict)
