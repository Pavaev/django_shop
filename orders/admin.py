from django.contrib import admin

# Register your models here.
from django.contrib import admin

from orders.models import Order, Status


class ProductOrderInline(admin.TabularInline):
    model = Order.product.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model = Order

    date_hierarchy = 'updated'
    empty_value_display = ''

    inlines = [ProductOrderInline, ]
    list_display = [field.name for field in Order._meta.fields]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    class Meta:
        model = Status

    list_display = [field.name for field in Status._meta.fields]
