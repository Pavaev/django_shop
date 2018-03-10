from django.shortcuts import render, get_object_or_404

# Create your views here.
from products.models import Product


def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return render(request, 'products/product.html', locals())
