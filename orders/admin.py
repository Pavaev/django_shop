from django.contrib import admin

# Register your models here.
from django.contrib import admin

from orders.models import Order, Status, ProductInOrder


class OrderAdmin(admin.ModelAdmin):
    class Meta():
        model = Order

    list_display = [field.name for field in Order._meta.fields]


admin.site.register(Order, OrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    class Meta:
        model = Status

    list_display = [field.name for field in Status._meta.fields]


admin.site.register(Status, StatusAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductInOrder

    list_display = [field.name for field in ProductInOrder._meta.fields]


admin.site.register(ProductInOrder, ProductInOrderAdmin)
