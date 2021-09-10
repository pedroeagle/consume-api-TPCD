from django.db import models

class Cliente(models.Model):
    c_custkey = models.IntegerField(primary_key=True)
    c_name = models.CharField()
    c_address = models.CharField()
    c_nationkey = models.IntegerField()
    c_phone = models.CharField()
    c_acctbal = models.FloatField()
    c_mktsegment = models.CharField()
    c_comment = models.CharField()
