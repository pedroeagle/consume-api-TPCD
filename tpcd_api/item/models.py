from django.db import models
class Item(models.Model):
    l_orderkey = models.IntegerField(primary_key=True, db_column='l_orderkey')
    l_partkey = models.IntegerField()
    l_suppkey = models.IntegerField()
    l_linenumber = models.IntegerField()
    l_quantity = models.FloatField()
    l_extendedprice = models.FloatField()
    l_discount = models.FloatField()
    l_tax = models.FloatField()
    l_returnflag = models.CharField(max_length=1)
    l_linestatus = models.CharField(max_length=1)
    l_shipdate = models.DateField()
    l_commitdate = models.DateField()
    l_receiptdate = models.DateField()
    l_shipinstruct = models.CharField(max_length=25)
    l_shipmode = models.CharField(max_length=10)
    l_comment = models.CharField(max_length=44)
    class Meta:
        db_table = 'dss_lineitem'