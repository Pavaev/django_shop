from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_text


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, default=None, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return smart_text('Категория: ' + self.name)


class Product(models.Model):
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(max_length=64, blank=True, default=None, null=True)
    category = models.ForeignKey(ProductCategory, blank=True, null=True,
                                 on_delete=models.NOT_PROVIDED)
    price = models.IntegerField(blank=False, default=None, null=False)
    discount = models.IntegerField(default=0)
    description = models.TextField(blank=True, default=None, null=True)
    short_description = models.TextField(blank=True, default=None, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return smart_text('Товар: ' + self.name + " Цена:" + str(self.price))


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, default=None, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return smart_text(str(self.id))


class ProductComment(models.Model):
    class Meta:
        db_table = 'comments'

    text = models.TextField(blank=False, null=False, max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True, auto_now=False)
