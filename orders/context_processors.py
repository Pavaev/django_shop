from .models import ProductInBasket


# TODO: Remove products from landing page(CSRF trouble)
def get_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_count = 0
    total_amount = 0
    for product in products_in_basket:
        products_total_count += product.count
        total_amount += product.count * product.price_per_item
    return locals()
