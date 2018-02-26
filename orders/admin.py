from django.contrib import admin

# Register your models here.
from django.contrib import admin

from orders.models import Order, Status, ProductInOrder, ProductInBasket


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    class Meta():
        model = Order

    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]


admin.site.register(Order, OrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    class Meta:
        model = Status

    list_display = [field.name for field in Status._meta.fields]


admin.site.register(Status, StatusAdmin)


class ProductInBasketAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductInBasket

    list_display = [field.name for field in ProductInBasket._meta.fields]


admin.site.register(ProductInBasket, ProductInBasketAdmin)
