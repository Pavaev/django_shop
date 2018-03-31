from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from cart.models import Cart
from my_shop import settings
from orders.decorators import require_ajax
from orders.forms import CheckoutContactForm
from orders.models import Order, ProductInOrder, Status

from products.models import Product


@require_POST
@require_ajax
def add_to_cart(request):
    cart = Cart(request)
    data = request.POST
    count = data.get("count")
    if not count or int(count) < 1:
        return JsonResponse({"count_error": "Неверное число заказанных товаров"})
    product = get_object_or_404(Product, id=data.get("product_id"))
    cart.add(product, count)
    return_dict = {}
    return_dict["total_amount"] = cart.get_sum()
    return_dict["products_in_basket"] = cart.cart
    return_dict["products_total_count"] = len(cart)
    return JsonResponse(return_dict)


@require_POST
@csrf_exempt
@require_ajax
def remove_from_cart(request):
    cart = Cart(request)
    data = request.POST
    product = get_object_or_404(Product, id=data.get("product_id"))
    cart.delete_product(product)
    return_dict = {}
    return_dict["products_total_count"] = len(cart)
    return_dict["products_in_basket"] = cart.cart
    return_dict["total_amount"] = cart.get_sum()
    return JsonResponse(return_dict)


def checkout(request):
    cart = Cart(request)
    if len(cart.cart) == 0:
        return redirect('/')
    contact_form = CheckoutContactForm()
    products_in_basket = cart.cart
    if request.method == 'POST':
        data = request.POST
        contact_form = CheckoutContactForm(request.POST or None)
        if contact_form.is_valid():
            email = contact_form.cleaned_data['email']
            phone = contact_form.cleaned_data['phone']
            user = None
            if request.user.is_authenticated:
                user = get_user_model().objects.get(email=request.user.email)
            order = Order.objects.create(email=email, phone=phone, status_id=1, user=user)
            for item in data:
                if len(item.split('product_in_basket_')) == 1:
                    continue
                id = item.split('product_in_basket_')[1]
                product = get_object_or_404(Product, id=id)
                ProductInOrder.objects.create(product=product, order=order, count=data[item])
        cart.del_all()
        return redirect(reverse('landing:home'))
    return render(request, 'orders/checkout.html', locals())
