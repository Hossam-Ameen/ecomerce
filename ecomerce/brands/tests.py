from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Brand
from rest_framework.test import APITestCase 
from django.core.files.uploadedfile import SimpleUploadedFile
from pathlib import Path


class BrandCase(APITestCase):
    
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    def create_user(self):
        user = User.objects.create(username='admin')
        user.set_password('123')
        user.save()
        response=self.client.post(reverse('token_obtain_pair'),{'username':'admin',"password":"123"})
        self.token = response.data['access']
        
    def create_brand(self):
        file=SimpleUploadedFile(name='test_image.jpg', content=open(self.BASE_DIR/'lg.jpeg', 'rb').read(), content_type='image/jpeg')
        new_brand = {'name':"samsung",'image':file}
        self.brand_create_response = self.client.post(reverse('brands-list'), new_brand, HTTP_AUTHORIZATION=f"Bearer {self.token}")
        
        
class BrandListTest(BrandCase):
    
    def setUp(self):
       self.create_user()
         
    def test_create_brand(self):
        self.create_brand()
        self.assertEqual(self.brand_create_response.status_code , status.HTTP_201_CREATED) 

    def test_list_brands(self):
        self.create_brand()
        response = self.client.get(reverse('brands-list'))
        self.assertEqual(response.status_code , status.HTTP_200_OK) 
        self.assertIsInstance(response.data['results'], list)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'], 1)
        
