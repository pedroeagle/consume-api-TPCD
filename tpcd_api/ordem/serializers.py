from rest_framework import serializers
from .models import Ordem
from cliente.serializers import NomeClienteSerializer
from cliente.models import Cliente
class OrdemSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()
    class Meta:
        model = Ordem
        fields = ['o_orderkey', 'o_custkey', 'o_orderstatus', 'o_totalprice', 'o_orderdate', 'o_orderpriority', 'o_clerk', 'o_shippriority', 'o_comment', 'client_name']
    def get_client_name(self, obj):
        ordem = OrdemCustomerKeySerializer(obj).data
        nome_cliente = NomeClienteSerializer(Cliente.objects.filter(c_custkey = ordem['o_custkey']).first()).data['c_name']
        return nome_cliente
class OrdemCustomerKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordem
        fields = ['o_custkey']