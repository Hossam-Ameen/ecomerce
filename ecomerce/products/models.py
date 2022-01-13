from django.db import models
from django.contrib.auth.models import User
from modules.models import Module


class Product(models.Model):
    name     = models.CharField( max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField()
    discount = models.FloatField()
    module   = models.ForeignKey(Module,related_name="module", on_delete=models.CASCADE)
    user     = models.ForeignKey(User,related_name="user",  on_delete=models.CASCADE)
    