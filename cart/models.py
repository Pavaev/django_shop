# Create your models here.
from my_shop import settings
from products.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, count):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'count': 0,
                                     'price': product.price}
            self.cart[product_id]['count'] = count
        else:
            self.cart[product_id]['count'] = int(count) + int(self.cart[product_id]['count'])
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def get_basket_total_count(self):
        total_count = 0
        for item in self.cart.items():
            for product in item:
                total_count += int(product['count'])
        return total_count

    def delete_product_from_cart(self, product):
        self.cart.pop(product.id)
        self.save()
