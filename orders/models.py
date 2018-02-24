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
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return smart_text('Статус: ' + str(self.name))


class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    name = models.CharField(max_length=64, blank=True, default=None, null=True)
    email = models.EmailField(blank=True, default=None, null=True)
    phone = models.CharField(max_length=48, blank=True, default=None, null=True)
    comments = models.TextField(blank=True, default=None, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    def __str__(self):
        return smart_text('Заказ: ' + str(self.id) + ' Статус: ' + self.status.name)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, default=None, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, blank=True, default=None, null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return smart_text('Товар: ' + str(self.product.name))
