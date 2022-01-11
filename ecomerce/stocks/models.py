from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    name=models.CharField( max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
# Create your models here.