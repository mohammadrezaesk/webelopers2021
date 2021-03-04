from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Account(User):
    role = models.CharField(max_length=10, default="buyer")

    def __str__(self):
        return self.username + "-" + self.role
