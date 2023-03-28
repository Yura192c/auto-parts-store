from django.test import TestCase
from django.urls import resolve
from main.views import index, about, contact


# Create your tests here.

class HomePageTest(TestCase):
    '''Home page test'''


    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
    
