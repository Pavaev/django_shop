from django.contrib import admin

from products.models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)


