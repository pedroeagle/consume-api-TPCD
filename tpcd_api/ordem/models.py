from django.db import models
from cliente.models import Cliente
class Ordem(models.Model):
    o_orderkey = models.IntegerField(primary_key=True)
    o_custkey = models.ForeignKey(Cliente, null=False)
    o_orderstatus = models.CharField()
    o_totalprice = models.FloatField()
    o_orderdate = models.DateField()
    o_orderpriority = models.CharField()
    o_clerk = models.CharField()
    o_shippriority = models.IntegerField()
    o_comment = models.CharField()
