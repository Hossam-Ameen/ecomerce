from django.test import TestCase
from django.contrib.auth.models import User
from .models import Brand


class BrandModelTests(TestCase):
    
    def test_create_brand(self):
        user = User(username="hossam", email="hosam@gm.com", password="123")
        new_brand = Brand(name="samsung", user=user)
        
    def test_get_brand(self):
        Brand.get()
     
