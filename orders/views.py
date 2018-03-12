from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from cart.models import Cart
from my_shop.decorators import required_AJAX

from products.models import Product


@require_POST
@required_AJAX
def add_to_cart(request):
    cart = Cart(request)
    data = request.POST
    count = data.get("count")
    if not count or int(count) < 1:
        return JsonResponse({"count_error": "Неверное число заказанных товаров"})
    product = get_object_or_404(Product, id=data.get("product_id"))
    cart.add(product, count)
    return_dict = {}
    return_dict["total_amount"] = 0
    return_dict["products_in_basket"] = cart.cart
    return_dict["products_total_count"] = len(cart)
    return JsonResponse(return_dict)


@require_POST
@csrf_exempt
@required_AJAX
def remove_from_cart(request):
    cart = Cart(request)
    data = request.POST
    product = get_object_or_404(Product, id=data.get("product_id"))
    cart.delete_product(product)
    return_dict = {}
    return_dict["products_total_count"] = len(cart)
    return_dict["products_in_basket"] = cart.cart
    return JsonResponse(return_dict)
