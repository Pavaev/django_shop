from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.http import require_POST

from orders.decorators import require_AJAX
from products.models import Product, ProductComment


def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = ProductComment.objects.filter(product=product)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return render(request, 'products/product.html', locals())


@login_required
@require_POST
@require_AJAX
def add_comment(request, product_id):
    data = request.POST
    ProductComment.objects.create(text=data['text'], user=request.user, product_id=product_id)
    print(data['text'])
    return JsonResponse(data)
