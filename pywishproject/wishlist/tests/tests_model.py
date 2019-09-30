from django.test import TestCase
from django.db.utils import IntegrityError

from wishlist.models import WishList

class WishListModelTests(TestCase):
    def setUp(self):
        self.wishlist_name = 'Notebooks'
        self.wishlist_description = 'A expressão pythonico, originada no inglês, pythonic, é uma expressão vaga, isto é, sem um significado exato. Geralmente é utilizada para referenciar um código idiomático em Python. O termo ficou famoso e mundialmente utilizado principalmente pelo sucesso que o Python faz com algumas soluções extremamente simples. Já cheguei a ouvir citações dizendo: "se você não fez em uma linha de código, você fez errado". Claro que isso não é literal, mas expressa bem como é a abordagem da linguagem.'
    
    def test_create_wish_list_with_success(self):
        wishlist = WishList.objects.create(
            name=self.wishlist_name,
        )
        self.assertIsNotNone(wishlist)
        self.assertEqual(self.wishlist_name, wishlist.name)
        self.assertIsNone(wishlist.description)
        self.assertTrue(wishlist.active)
        self.assertIsNotNone(wishlist.created_on)
        self.assertIsNotNone(wishlist.created_by)
    
    def test_create_wish_list_with_description_return_success(self):
        description = self.wishlist_description
        wishlist = WishList.objects.create(
            name=self.wishlist_name,
            description=description,
        )
        self.assertIsNotNone(wishlist)
        self.assertEqual(self.wishlist_description, wishlist.description)
    
    def test_create_wish_list_with_description_none_return_success(self):
        description = None
        wishlist = WishList.objects.create(
            name=self.wishlist_name,
            description=description,
        )
        self.assertIsNotNone(wishlist)
        self.assertIsNone(wishlist.description)
    
    def test_try_to_create_two_wish_list_with_the_same_name(self):
        wishlist_name = self.wishlist_name
        wishlist_first = WishList.objects.create(
            name=wishlist_name,
        )
        with self.assertRaises(IntegrityError) as context:
            wishlist_second = WishList.objects.create(
                name=wishlist_name,
            )
        self.assertIn('duplicate key value violates unique constraint', str(context.exception))
    
    def test_when_create_wish_list_return_object_active_true(self):
        wishlist_name = self.wishlist_name
        wishlist = WishList.objects.create(
            name=wishlist_name,
        )
        self.assertTrue(wishlist.active)
    
    def test_when_create_str_return_name(self):
        wishlist_name = self.wishlist_name
        wishlist = WishList.objects.create(
            name=wishlist_name,
        )
        self.assertEqual(wishlist_name, str(wishlist))
