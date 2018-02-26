from django.shortcuts import render, render_to_response

# Create your views here.
from products.models import Product


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render_to_response('products/product.html', locals())
