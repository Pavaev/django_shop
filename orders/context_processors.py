# TODO: Remove products from landing page(CSRF trouble)
from cart.models import Cart


def get_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    cart = Cart(request)
    products_total_count = len(cart)
    return locals()
