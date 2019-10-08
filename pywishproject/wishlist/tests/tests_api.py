from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from ..models import WishList
from ..serializers import WishListSerializer

WISH_LIST_URL = '/api/v2/wishs/' # reverse('wish-list')

class WishListApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user_test@pywish.com',
            'T3st3@1w3r5y'
        )
        self.client.force_authenticate(self.user)
    
    def test_url_api_used_v1(self):
        self.assertEqual('/api/v1/wishlists/', reverse('api-list'))
    
    def test_url_api_used_v2(self):
        self.assertEqual('/api/v2/wishs/', WISH_LIST_URL)
    
    def test_retrieve_all_wish_lists(self):
        WishList.objects.create(
            name='eBooks',
            created_by = self.user.get_username(),
        )
        WishList.objects.create(
            name='Trips',
            created_by = self.user.get_username(),
        )
        
        res = self.client.get(WISH_LIST_URL)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        wish_lists = WishList.objects.all().order_by('-name')
        serializer = WishListSerializer(wish_lists, many=True)
        self.assertIsNotNone(res)
        self.assertIsNotNone(res.data)
        self.assertEqual(res.data['results'], serializer.data)
    
    def test_create_wish_list_successful(self):
        payload = {
            'name': 'Games'
        }
        response = self.client.post(WISH_LIST_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        exists = WishList.objects.filter(
            created_by = self.user.get_username(),
            name = payload['name'],
        ).exists()
        self.assertTrue(exists)
