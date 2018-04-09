from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_text

# Create your models here.
from my_shop import settings
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

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', blank=True, default=None, null=True,
                             on_delete=models.CASCADE)
    email = models.EmailField(blank=True, default=None, null=True)
    phone = models.CharField(max_length=48, blank=False, default=None, null=False)
    comments = models.TextField(blank=True, default=None, null=True)
    address = models.CharField(blank=True, default=None, null=True, max_length=256)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.ForeignKey('Status', related_name='status', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    product = models.ManyToManyField(Product, through='ProductInOrder', through_fields=('order', 'product'))

    def __str__(self):
        return smart_text(str(self.id) + ' ' + self.email)


class ProductInOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order,  on_delete=models.CASCADE)
    count = models.IntegerField(blank=False, null=False, default=1)
