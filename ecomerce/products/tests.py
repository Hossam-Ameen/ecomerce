<<<<<<< HEAD
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from brands.models import Brand
from modules.models import Module
from .models import Product
from rest_framework.test import APITestCase 
from django.core.files.uploadedfile import SimpleUploadedFile
from pathlib import Path


class ModuleCase(APITestCase):
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
    
    def create_module(self):
        self.create_brand()
        new_module = {'name':"samsung a1",'brand':self.brand_create_response.data['id']}
        self.module_create_response = self.client.post(reverse('modules-list'), new_module, HTTP_AUTHORIZATION=f"Bearer {self.token}")
    
    def create_product(self):
        self.create_module()
        new_product = {'name':"smart tv",
                      'quantity':1,
                      'price':200,
                      'discount':10,
                      'module':self.module_create_response.data['id']}
        self.product_create_response = self.client.post(reverse('products-list'), new_product, HTTP_AUTHORIZATION=f"Bearer {self.token}")
    
    def setUp(self):
       self.create_user()
       self.create_product()
    
    def tearDown(self):
        brands = Brand.objects.all()
        for brand in brands:
            brand.delete()
        
class ProductListTest(ModuleCase):            
    def test_create_product(self):
        self.assertEqual(self.product_create_response.status_code , status.HTTP_201_CREATED) 

    def test_list_products(self):
        response = self.client.get(reverse('products-list'))
        self.assertEqual(response.status_code , status.HTTP_200_OK) 
        self.assertIsInstance(response.data['results'], list)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'], 1)
        
        
class ProductDetialTest(ModuleCase):                    
    def test_retrieves_one_item(self):
        response = self.client.get(reverse('products-detail', kwargs={'pk':self.product_create_response.data['id'] } ) )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_one_item(self):
        response = self.client.patch(reverse('products-detail', kwargs={'pk':self.product_create_response.data['id'] } ) , {
            'name': "samrt tv a2",
            'module':self.module_create_response.data['id']
        } )
        updated_product=Product.objects.get(id=self.product_create_response.data['id'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_product.name, "samrt tv a2")      
            
    def test_delete_product(self):
        products_counter = Product.objects.all().count()
        self.assertGreater(products_counter , 0)
        self.assertEqual(products_counter , 1)
        response=self.client.delete(reverse('products-detail', kwargs={'pk':self.product_create_response.data['id'] } ))
        self.assertEqual(response.status_code , status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.all().count(), 0)
        
=======
from django.test import TestCase

# Create your tests here.
>>>>>>> main
