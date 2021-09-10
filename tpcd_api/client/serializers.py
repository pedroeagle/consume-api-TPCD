from rest_framework import serializers
from .models import Client
class ClientNameSerializer(serializers.ModelSerializer):
    class Meta():
        model = Client
        fields = ['c_name']
