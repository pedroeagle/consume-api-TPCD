from django.db import models
from client.models import Client
class Order(models.Model):
    o_orderkey = models.IntegerField(primary_key=True, db_column='o_orderkey')
    o_custkey = models.ForeignKey(Client, on_delete=models.RESTRICT, db_column='o_custkey', related_name='client')
    o_orderstatus = models.CharField(max_length=1)
    o_totalprice = models.FloatField()
    o_orderdate = models.DateField()
    o_orderpriority = models.CharField(max_length=15)
    o_clerk = models.CharField(max_length=15)
    o_shippriority = models.IntegerField()
    o_comment = models.CharField(max_length=79)
    class Meta:
        db_table = 'dss_order'