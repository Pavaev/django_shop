from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.views.decorators.http import require_POST

from orders.decorators import require_ajax
from products.models import Product, ProductComment


def show_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = ProductComment.objects.filter(product=product).order_by('-created')
    paginator = Paginator(comments, 2)
    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    if request.is_ajax():
        return render(request, 'products/comments.html', {'comments': comments, 'product_id': product_id})
    return render(request, 'products/product.html', locals())


@login_required
@require_POST
@require_ajax
def add_comment(request, product_id):
    data = request.POST
    ProductComment.objects.create(text=data['text'], user=request.user, product_id=product_id)
    product = get_object_or_404(Product, id=product_id)
    comments = ProductComment.objects.filter(product=product).order_by('-created')
    paginator = Paginator(comments, 2)
    comments = paginator.page(1)
    return render(request, 'products/comments.html', {'comments': comments, 'product_id': product_id})
