

# TODO: Remove products from landing page(CSRF trouble)
def get_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    return locals()
