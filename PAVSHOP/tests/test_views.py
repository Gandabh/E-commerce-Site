from django.test import TestCase
from django.conf import settings
from django.urls import reverse_lazy
from account.models import User
from core.models import Contact
from core.views import ContactView
from blog.views import BlogView



class TestContactView(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.contact_url = f'/en/contact/'
        cls.url = reverse_lazy('core:contact')
        cls.view = ContactView()

        cls.valid_data = {
            'full_name':'gandab',
            'email':'gandabhasan@gmail.com',
            'phone_number': '12345',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }

        cls.invalid_data = {
           'full_name':'gandab',
            'email':'gandabhasan@gmail.com',
            'phone_number': '1234536363636366363636663663636',
            # 'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }

    def test_reverse_lazy_method(self):
        self.assertEqual(self.contact_url, self.url)

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertTemplateUsed(response, 'contact.html')

    def test_post_request(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 302)
        contact_data = Contact.objects.last()
        self.assertEqual(self.valid_data['subject'], contact_data.subject)
        self.assertEqual(self.valid_data['message'], contact_data.message)



    def test_post_invalid_request(self):
        response = self.client.post(self.url, self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "", html=True)


    @classmethod
    def tearDownClass(cls):
        pass




class TestBlogView(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.list_url = f'/blog/blog-list'
        cls.url = reverse_lazy('blog:blog_list')
        cls.view = BlogView()

    def test_reverse_lazy_method(self):
        self.assertEqual(self.list_url, self.url)


    @classmethod
    def tearDownClass(cls):
        pass