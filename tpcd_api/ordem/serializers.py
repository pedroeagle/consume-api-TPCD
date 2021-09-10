from rest_framework import serializers
from .models import Ordem
class OrdemSerializer(serializers.ModelSerializer):
    class Meta():
        model = Ordem
        fields = ['o_orderkey', 'o_custkey', 'o_orderstatus', 'o_totalprice', 'o_orderdate', 'o_orderpriority', 'o_clerk', 'o_shippriority', 'o_comment', 'c_name']