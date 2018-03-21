from django.contrib import admin

from orders.admin import ProductOrderInline
from products.models import Product, ProductImage, ProductCategory, ProductComment


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductCategory

    list_display = [field.name for field in ProductCategory._meta.fields]


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductCommentInline(admin.TabularInline):
    model = ProductComment
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline, ProductCommentInline, ProductOrderInline, ]
