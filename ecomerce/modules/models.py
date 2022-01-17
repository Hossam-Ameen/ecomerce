from django.db import models
from django.contrib.auth.models import User
from brands.models import Brand

class Module(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, related_name="brand", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="module_users", on_delete=models.CASCADE)
