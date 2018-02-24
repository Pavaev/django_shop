from django.db import models
from django.utils.encoding import smart_text


# Create your models here.

class Product(models.Model):
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(max_length=64, blank=True, default=None, null=True)
    price = models.IntegerField(blank=False, default=None, null=False)
    description = models.TextField(blank=True, default=None, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return smart_text('Товар: ' + str(self.name))


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, default=None, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        return smart_text(str(self.id))
