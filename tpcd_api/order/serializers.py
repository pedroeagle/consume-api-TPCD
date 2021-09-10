from rest_framework import serializers
from .models import Order
from client.serializers import ClientNameSerializer
from client.models import Client
class OrderSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['o_orderkey', 'o_custkey', 'o_orderstatus', 'o_totalprice', 'o_orderdate', 'o_orderpriority', 'o_clerk', 'o_shippriority', 'o_comment', 'client_name']
    def get_client_name(self, obj):
        order = OrderCustomerKeySerializer(obj).data
        name = ClientNameSerializer(Client.objects.filter(c_custkey = order['o_custkey']).first()).data['c_name']
        return name
class OrderCustomerKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['o_custkey']