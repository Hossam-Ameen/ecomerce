from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Brand
from rest_framework.test import APITestCase 


class BrandModelTests(APITestCase):
    user = User(username="hossam", email="hosam@gm.com", password="123")
    # def test_create_brand(self):
    #     user = User(username="hossam", email="hosam@gm.com", password="123")
    #     new_brand = Brand(name="samsung", user=user)
    
    def test_create_brand(self):
        new_brand = {'name':"samsung" ,'user':self.user}
        response = self.client.post(reverse('brands-list') , new_brand)
        self.assertEqual(response.status_code , status.HTTP_201_CREATED) 
