from django.contrib import admin

# Register your models here.
from django.contrib import admin

from orders.models import Order, Status


class ProductOrderInline(admin.TabularInline):
    model = Order.product.through


class OrderAdmin(admin.ModelAdmin):
    class Meta():
        model = Order

    inlines = [ProductOrderInline, ]
    list_display = [field.name for field in Order._meta.fields]
    exclude = ('product',)


admin.site.register(Order, OrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    class Meta:
        model = Status

    list_display = [field.name for field in Status._meta.fields]


admin.site.register(Status, StatusAdmin)
