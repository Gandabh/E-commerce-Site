from django.test import TestCase
from core.forms import ContactForm
from account.forms import CheckoutForm




class TestContactForm(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_data = {
            'full_name':'gandab',
            'email':"gandab@gmail.com",
            'phone_number': '12345',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }

        cls.invalid_data = {
            'full-name':'gandab',
            'email':"gandab@gmail.com",
            # 'phone_number': '12345',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }
        cls.form = ContactForm

    def test_form_with_valid_data(self):
        form = self.form(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_with_invalid_data(self):
        form = self.form(data=self.invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors)
        self.assertIn('This field is required.', form.errors['phone_number'])

    @classmethod
    def tearDownClass(cls):
        pass





class TestCheckoutForm(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_data = {
            'company': 'Company Name',
            'address': 'Azerbaijan',
            'city': 'Baku',
            'country': 'Azerbaijan',
            'email': 'gandabhasan@gmail.com',
            'phone':'0501234545', 
            'shipping_company':'Company Name',
            'shipping_address': 'Azerbaijan',
            'shipping_city': 'Baku',
            'shipping_country': 'Azerbaijan',
            'shipping_email':'gandabhasan@gmail.com',
            'shipping_phone':'0501234545', 
        }

        cls.invalid_data = {
            'city': 'Baku',
            'country': 'Azerbaijan',
            'email': 'gandabhasan@gmail.com',
            'phone':'0501234545', 
            'shipping_company':'Company Name',
            'shipping_address': 'Azerbaijan',
            'shipping_city': 'Baku',
            'shipping_country': 'Azerbaijan',
            'shipping_email':'gandabhasan@gmail.com',
            'shipping_phone':'0501234545', 
        }
        cls.form = CheckoutForm

    def test_form_with_valid_data(self):
        form = self.form(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_with_invalid_data(self):
        form = self.form(data=self.invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('company', form.errors)
        self.assertIn('This field is required.', form.errors['company'])

    @classmethod
    def tearDownClass(cls):
        pass