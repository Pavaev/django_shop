from django.contrib import admin

from products.models import Product, ProductImage, ProductCategory


class ProductCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductCategory

    list_display = [field.name for field in ProductCategory._meta.fields]


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)
