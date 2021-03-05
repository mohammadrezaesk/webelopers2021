from django.contrib.auth.models import User
from django.db import models
from Accounts.models import Account


class Product(models.Model):
    name = models.CharField(max_length=100, default="")
    quantity = models.IntegerField()
    price = models.IntegerField()
    seller = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, upload_to='images/', blank=True)

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

    def __str__(self):
        return f'Rate(score={self.score}, product={self.product.name})'


class Comment(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'Comment(user={self.user.username}, product={self.product.name})'


class Cart(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'Comment(user={self.buyer.username}, product={self.product.name})'
