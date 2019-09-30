from django.test import TestCase

from wishlist.models import WishList

class WishListModelTests(TestCase):
    def setUp(self):
        ...
    def test_create_wish_list_success(self):
        wishlist = WishList.objects.create(
            name='Notebooks',
        )
        self.assertIsNotNone(wishlist)
