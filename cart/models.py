# Create your models here.
from django.core.exceptions import ObjectDoesNotExist

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
            self.cart[product_id] = {'name': product.name, 'count': 0,
                                     'price': product.price}
            self.cart[product_id]['count'] = count
        else:
            self.cart[product_id]['count'] = int(count) + int(self.cart[product_id]['count'])
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def __len__(self):
        return sum(int(item['count']) for item in self.cart.values())

    def delete_product(self, product):
        self.cart.pop(str(product.id))
        self.session.modified = True

    def get_all(self):
        products = []
        for product_id in self.cart:
            try:
                product = Product.objects.get(id=product_id)
                products.append(product)
            except ObjectDoesNotExist:
                pass
        return products
