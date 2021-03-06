from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name="stock_user", on_delete=models.CASCADE)
