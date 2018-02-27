from django.db import models
from django.db.models import signals
from django.utils.encoding import smart_text

# Create your models here.
from products.models import Product


class Status(models.Model):
    class Meta:
        db_table = 'statuses'
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    name = models.CharField(max_length=24, blank=True, default=None, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return smart_text('Статус: ' + str(self.name))


class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    total_price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2,
                                      default=0)  # total price for all products in order
    name = models.CharField(max_length=64, blank=False, default=None, null=False)
    email = models.EmailField(blank=True, default=None, null=True)
    phone = models.CharField(max_length=48, blank=False, default=None, null=False)
    comments = models.TextField(blank=True, default=None, null=True)
    address = models.CharField(blank=False, default=None, null=False, max_length=256)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return smart_text('Заказ: ' + str(self.id) + ' Статус: ' + self.status.name)


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, default=None, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, blank=True, default=None, null=True, on_delete=models.SET_NULL)
    count = models.IntegerField(default=1, blank=False, null=False)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price_per_item*count
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Product in basket'
        verbose_name_plural = 'Products in basket'

    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.total_price = int(self.count) * self.price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, default=None, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, blank=True, default=None, null=True, on_delete=models.SET_NULL)
    count = models.IntegerField(default=1, blank=False, null=False)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price_per_item*count
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product in order'
        verbose_name_plural = 'Products in order'

    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price

        self.total_price = self.count * self.price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    all_products_in_order = ProductInOrder.objects.filter(order=instance.order, is_active=True)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


def __str__(self):
    return smart_text('Товар: ' + str(self.product.name))


signals.post_save.connect(product_in_order_post_save, sender=ProductInOrder)
