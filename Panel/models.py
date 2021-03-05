from django.db import models
from Accounts.models import Account


class Product(models.Model):
    name = models.CharField(max_length=100, default="")
    quantity = models.IntegerField()
    price = models.IntegerField()
    seller = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, upload_to='media/static/images')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class Rate(models.Model):
    score = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)


class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=200)
