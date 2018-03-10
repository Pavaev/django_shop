from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.decorators.http import require_POST

from cart.models import Cart

from products.models import Product


@require_POST
def add_to_cart(request):
    cart = Cart(request)
    data = request.POST
    count = data.get("count")
    if not count or int(count) < 1:
        return JsonResponse({"count_error": "Неверное число заказанных товаров"})
    product = get_object_or_404(Product, id=data.get("product_id"))
    cart.add(product, count)
    return render(request, 'base.html', locals())

@require_POST
def remove_from_cart(request):
    cart = Cart(request)
    data = request.POST
    product = get_object_or_404(Product, id=data.get("product_id"))
    cart.delete_product_from_cart(product)