from rest_framework import serializers
from .models import Customer
class CustomerNameSerializer(serializers.ModelSerializer):
    class Meta():
        model = Customer
        fields = ['c_name']
class CustomerSerializer(serializers.ModelSerializer):
    class Meta():
        model = Customer
        fields = '__all__'
