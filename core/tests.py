from django.test import TestCase
from django.urls import reverse
from rest_framework.status import *
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from users.models import *
from .models import *

# Create your tests here.

class TestViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_user = CustomUser.objects.create(email='test_user@gmail.com', password='test@password')
        self.test_supplier = Suppliers.objects.create(name='test supplier', address='test_address', phone_number=1234 )
        self.test_supplier2 = Suppliers.objects.create(name='test supplier2', address='test_address', phone_number=1234)
        self.test_user.save()
        self.item = InventoryItems.objects.create(item_name='product one',price=10, item_description='test', date_added ='2024-06-20')
        self.item.suppliers.set([self.test_supplier.id])
        self.access_token = AccessToken.for_user(self.test_user)
    
    def test_get_inventory_item_unauthenticated(self):
        url = reverse('inventory_items-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED )
    
    def test_get_inventory_item_authenticated(self):
        url = reverse('inventory_items-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK )
    
    def test_create_inventory_product_unauthenticated(self):
        url = reverse('inventory_items-list')
        data = {'item_name':'new product', 'item_description':'test', 'price': 5, 'suppliers':'1, 2'}
        response = self.client.post(url)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED )

    def test_create_inventory_product_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse('inventory_items-list')
        data = {'item_name':'new product', 'item_description':'test', 'price': 5, 'suppliers':[1], 'date_added':'2024-06-06'}
        
        response = self.client.post(url)
        response1 = self.client.post(url, data=data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response1.status_code, HTTP_201_CREATED)
        
        
    
    def test_create_inventory_product_auth_with_missing_field(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse('inventory_items-list')
        data = {'item_name':'new product', 'item_description':'test', 'suppliers':[], 'price': 5, 'date_added':'2024-06-06'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_update_inventory_product(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse('inventory_items-detail', args=[self.item.id])
        data = {
            'item_name':'new name', 'item_description':'new description', 'price':100, 'suppliers':[2]
        }
        response = self.client.put(url, data=data)
        print(response.json())
        self.assertEqual(response.status_code, HTTP_200_OK)
    

    def test_create_supplier_authenticated(self):

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse('suppliers-list')
        data = {'name':'tester', 'address':'1223', 'phone_number':1234, 'supplies':[1] }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)
    
    def test_update_supplier_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse('suppliers-detail', args=[self.test_supplier2.id])
        data = {'name':'john', 'address':'1223', 'phone_number':1234, 'supplies':[1] }
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertNotEqual(response.json()['name'], self.test_supplier.name)
    
   