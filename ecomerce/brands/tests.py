from rest_framework import status
from django.urls import reverse
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
        file=SimpleUploadedFile(name='samsung_image.jpg', content=open(self.BASE_DIR/'samsung.png', 'rb').read(), content_type='image/jpeg')
        new_brand = {'name':"samsung",'image':file}
        self.brand_create_response = self.client.post(reverse('brands-list'), new_brand, HTTP_AUTHORIZATION=f"Bearer {self.token}")
        
        
class BrandListTest(BrandCase):
    def setUp(self):
       self.create_user()
       self.create_brand()
    
    def tearDown(self):
        brands = Brand.objects.all()
        for brand in brands:
            brand.delete()
             
    def test_create_brand(self):
        self.assertEqual(self.brand_create_response.status_code , status.HTTP_201_CREATED) 

    def test_list_brands(self):
        response = self.client.get(reverse('brands-list'))
        self.assertEqual(response.status_code , status.HTTP_200_OK) 
        self.assertIsInstance(response.data['results'], list)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'], 1)
        
        
class BrandDetialTest(BrandCase):
    def setUp(self):
       self.create_user()
       self.create_brand()
       
    def tearDown(self):
        brands = Brand.objects.all()
        for brand in brands:
            brand.delete()  
            
    def test_retrieves_one_item(self):
        response = self.client.get(reverse('brands-detail', kwargs={'pk':self.brand_create_response.data['id'] } ) )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_one_item(self):
        file=SimpleUploadedFile(name='lg_updated.jpg', content=open(self.BASE_DIR/'lg.jpeg', 'rb').read(), content_type='image/jpeg')
        response = self.client.patch(reverse('brands-detail', kwargs={'pk':self.brand_create_response.data['id'] } ) , {
            'name': "LG",
            'image': file
        } )
        updated_brand=Brand.objects.get(id=self.brand_create_response.data['id'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_brand.name, "LG")      
    
    def test_update_one_item_with_image(self):
        file=SimpleUploadedFile(name='lg_updated.jpg', content=open(self.BASE_DIR/'lg.jpeg', 'rb').read(), content_type='image/jpeg')
        response = self.client.patch(reverse('brands-update-image', kwargs={'pk':self.brand_create_response.data['id'] } ) , {
            'image': file
        } ) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

            
    def test_delete_brand(self):
        brands_counter = Brand.objects.all().count()
        self.assertGreater(brands_counter , 0)
        self.assertEqual(brands_counter , 1)
        response=self.client.delete(reverse('brands-detail', kwargs={'pk':self.brand_create_response.data['id'] } ))
        self.assertEqual(response.status_code , status.HTTP_204_NO_CONTENT)
        self.assertEqual(Brand.objects.all().count(), 0)
        
