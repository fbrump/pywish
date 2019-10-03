from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from ..models import WishList
from ..serializers import WishListSerializer

WISH_LIST_URL = reverse('api-list')

class WishListApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user_test@pywish.com',
            'T3st3@1w3r5y'
        )
        self.client.force_authenticate(self.user)
    
    def test_retrieve_all_wish_lists(self):
        WishList.objects.create(
            name='eBooks',
        )
        WishList.objects.create(
            name='Trips',
        )
        
        res = self.client.get(WISH_LIST_URL)
        
        wishLists = WishList.objects.all().order_by('-name')
        serializer = WishListSerializer(wishLists, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
    
    def test_create_wish_list_successful(self):
        payload = {
            'name': 'Games'
        }
        self.client.post(WISH_LIST_URL, payload)
        
        exists = WishList.objects.filter(
            created_by = self.user.user_name,
            name = payload['name'],
        ).exists()
        self.assertTrue(exists)
