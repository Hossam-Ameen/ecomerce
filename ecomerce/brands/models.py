from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to="", max_length=100)
    user = models.ForeignKey(User,related_name='owner', on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super(Brand,self).delete(*args,**kwargs)
        