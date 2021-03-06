from django.db import models
from django.contrib.auth.models import User
from brands.models import Brand

class Module(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, related_name="module_brand", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="module_user", on_delete=models.CASCADE)
