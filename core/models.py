from django.db import models

# Create your models here.
class InventoryItems(models.Model):
    item_name = models.CharField(max_length=500)
    item_description = models.TextField()
    price = models.FloatField()
    date_added = models.DateField()
    suppliers = models.ManyToManyField(to='Suppliers', related_name='supplies')



class Suppliers(models.Model):
    name = models.CharField(max_length=1000)
    address = models.TextField()
    phone_number = models.IntegerField()

