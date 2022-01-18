from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to="uploads/", max_length=100)
    user = models.ForeignKey(User, related_name='brand_user', on_delete=models.CASCADE)
