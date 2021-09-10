from item.models import Item
from rest_framework import serializers
from .models import Order
from customer.serializers import CustomerNameSerializer
from customer.models import Customer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
class OrderCustomerKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['o_custkey']
class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'