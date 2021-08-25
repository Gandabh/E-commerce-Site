from django.test import TestCase
from account.models import User
from django.test import TestCase
from core.models import Subscriber




class TestSubscriberModel(TestCase):

    @classmethod
    def setUpClass(cls):
        data = {
            'email': 'gandabhasan@gmail.com',

        }
        data2 = {
            'email': 'gandab@gmail.com',
        }
        cls.subs_info1 = Subscriber.objects.create(**data)
        cls.subs_info2 = Subscriber.objects.create(**data2)

    def test_created_data(self):
        self.assertEqual(self.subs_info1.email, 'gandabhasan@gmail.com')
        self.assertEqual(self.subs_info2.email, 'gandab@gmail.com')

    def test_str_method(self):
        self.assertEqual(str(self.subs_info1), self.subs_info1.email)
        self.assertEqual(str(self.subs_info2), self.subs_info2.email)

    @classmethod
    def tearDownClass(cls):
        pass






class TestUserModel(TestCase):

    @classmethod
    def setUpClass(cls):
        data = {
            'username': 'gandabhasan',
            'email': 'gandabhasan@gmail.com',
            'password': 'password12345'
        }
        data2 = {
            'username': 'techacademy',
            'email': 'techacademy@gmail.com',
            'password': 'password12345'
        }
        cls.user_info1 = User.objects.create(**data)
        cls.user_info2 = User.objects.create(**data2)

    def test_created_data(self):
        self.assertEqual(self.user_info1.username, 'gandabhasan')
        self.assertEqual(self.user_info2.username, 'techacademy')

    def test_str_method(self):
        self.assertEqual(str(self.user_info1), self.user_info1.username)
        self.assertEqual(str(self.user_info2), self.user_info2.username)

    @classmethod
    def tearDownClass(cls):
        pass


