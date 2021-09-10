from django.db import models

class Customer(models.Model):
    c_custkey = models.IntegerField(primary_key=True, db_column='c_custkey')
    c_name = models.CharField(max_length=25)
    c_address = models.CharField(max_length=40)
    c_nationkey = models.IntegerField()
    c_phone = models.CharField(max_length=15)
    c_acctbal = models.FloatField()
    c_mktsegment = models.CharField(max_length=10)
    c_comment = models.CharField(max_length=117)
    class Meta:
        db_table = 'dss_customer'
    def __unicode__(self):
        return self.c_name