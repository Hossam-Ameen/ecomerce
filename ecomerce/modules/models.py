from django.db import models
from django.contrib.auth.models import User
import brands
from brands.models import Brand


class Module(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.
