from django.db import models
from Accounts.models import Account


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, default="")
    quantity = models.IntegerField()
    price = models.IntegerField()
    seller = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
