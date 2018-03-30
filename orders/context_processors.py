from cart.models import Cart


def get_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    cart = Cart(request)
    total_amount = cart.get_sum()
    products_total_count = len(cart)
    products_in_basket = cart.cart
    return locals()
