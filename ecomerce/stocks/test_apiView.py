from urllib import response
from django.test import TestCase,Client
from .models import Stock
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase 
import json
from django.test.client import MULTIPART_CONTENT, encode_multipart, BOUNDARY


class StockCase(APITestCase):
    def create_user(self):
        user = User.objects.create(username='admin')
        user.set_password('123')
        user.save()
        response=self.client.post(reverse('token_obtain_pair'),{'username':'admin',"password":"123"})
        self.token = response.data['access']
        
    def create_stock(self):
        new_stock = {'name':"samsung"} 
        self.create_stock_response =  self.client.post(reverse('stocks-list'), new_stock, format='json',  HTTP_AUTHORIZATION=f"Bearer {self.token}")
        
        
class StockListViewTest(StockCase):
    
    def setUp(self):
       self.create_user()
       
        
    def test_create_stock(self): 
        self.create_stock()
        self.assertEqual(self.create_stock_response.status_code , status.HTTP_201_CREATED) 
        
    def test_list_stocks(self):
        self.create_stock()
        response =  self.client.get(reverse('stocks-list'))
        self.assertEqual(response.status_code , status.HTTP_200_OK) 
        self.assertIsInstance(response.data['results'], list)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'], 1)   
        
             
class StockDetialTest(StockCase):
    
    def setUp(self):
       self.create_user()
       self.create_stock()
       
    def test_retrieves_one_item(self):
        response = self.client.get(reverse('stocks-detail', kwargs={'pk':self.create_stock_response.data['id'] } ) )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    def test_update_one_item(self):
        response = self.client.patch(reverse('stocks-detail', kwargs={'pk':self.create_stock_response.data['id'] } ) , {
            'name': "updated item"
        } ,format='json')
        updated_stock=Stock.objects.get(id=self.create_stock_response.data['id'])
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_stock.name, "updated item")
    
    def test_delete_one_item(self):
        stocks_counter = Stock.objects.all().count()

        self.assertGreater(stocks_counter , 0)
        self.assertEqual(stocks_counter , 1)
        
        response=self.client.delete(reverse('stocks-detail', kwargs={'pk':self.create_stock_response.data['id'] } ))
        
        self.assertEqual(response.status_code , status.HTTP_204_NO_CONTENT)
        self.assertEqual(Stock.objects.all().count(), 0)