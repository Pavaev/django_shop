from django.contrib import admin

from products.models import Product, ProductImage


class ProductAdmin(admin.ModelAdmin):
    class Meta():
        model = Product


list_display = ['id', 'product', 'image', 'is_active', 'created', 'updated']

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    class Meta():
        model = ProductImage

    list_display = [field.name for field in ProductImage._meta.fields]


admin.site.register(ProductImage, ProductAdmin)
