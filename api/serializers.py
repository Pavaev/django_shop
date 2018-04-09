from django.utils.timezone import now
from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from authentication.models import User
from orders.models import Order
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 2


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'product',)
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)
    time_since_last_login = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'is_staff', 'time_since_last_login', 'orders',)
        depth = 1

    def get_time_since_last_login(self, obj):
        return (now() - obj.last_login).seconds
