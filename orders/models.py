from django.db import models
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

    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # total price for all products in order
    name = models.CharField(max_length=64, blank=False, default=None, null=False)
    email = models.EmailField(blank=True, default=None, null=True)
    phone = models.CharField(max_length=48, blank=False, default=None, null=False)
    comments = models.TextField(blank=True, default=None, null=True)
    address = models.CharField(blank=False, default=None, null=False, max_length=256)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    def __str__(self):
        return smart_text('Заказ: ' + str(self.id) + ' Статус: ' + self.status.name)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, default=None, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, blank=True, default=None, null=True, on_delete=models.SET_NULL)
    count = models.IntegerField(default=1, blank=False, null=False)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price_per_item*count
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return smart_text('Товар: ' + str(self.product.name))
