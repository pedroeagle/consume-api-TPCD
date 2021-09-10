from rest_framework import serializers
from .models import Cliente
class NomeClienteSerializer(serializers.ModelSerializer):
    class Meta():
        model = Cliente
        fields = ['c_name']
