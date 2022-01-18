from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from brands.models import Brand
from .models import Module
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
    
    def setUp(self):
       self.create_user()
       self.create_module()
    
    def tearDown(self):
        brands = Brand.objects.all()
        for brand in brands:
            brand.delete()
        
class ModuleListTest(ModuleCase):            
    def test_create_module(self):
        self.assertEqual(self.module_create_response.status_code , status.HTTP_201_CREATED) 

    def test_list_modules(self):
        response = self.client.get(reverse('modules-list'))
        self.assertEqual(response.status_code , status.HTTP_200_OK) 
        self.assertIsInstance(response.data['results'], list)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'], 1)
        
        
class ModuleDetialTest(ModuleCase):                    
    def test_retrieves_one_item(self):
        response = self.client.get(reverse('modules-detail', kwargs={'pk':self.module_create_response.data['id'] } ) )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_one_item(self):
        response = self.client.patch(reverse('modules-detail', kwargs={'pk':self.module_create_response.data['id'] } ) , {
            'name': "samsung a2",
            'brand':self.brand_create_response.data['id']
        } )
        updated_module=Module.objects.get(id=self.module_create_response.data['id'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_module.name, "samsung a2")      
            
    def test_delete_module(self):
        modules_counter = Module.objects.all().count()
        self.assertGreater(modules_counter , 0)
        self.assertEqual(modules_counter , 1)
        response=self.client.delete(reverse('modules-detail', kwargs={'pk':self.module_create_response.data['id'] } ))
        self.assertEqual(response.status_code , status.HTTP_204_NO_CONTENT)
        self.assertEqual(Module.objects.all().count(), 0)
        
