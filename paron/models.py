from django.db import models


# Create your models here.
class Product(models.Model):
    product_nr = models.CharField(max_length=4)
    type = models.CharField(max_length=15, default='')
    price = models.IntegerField(max_length=15, default=0)

    def __str__(self):
        return self.type


class Inventory(models.Model):
    inventory_nr = models.IntegerField(max_length=10, default=0)
    city = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.city


class Balance(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)


class Delivery(models.Model):
    Date = models.DateTimeField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, default='')
    amount = models.IntegerField(default=0)
