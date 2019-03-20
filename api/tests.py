from django.test import TestCase
import datetime as dt
# Create your tests here.
from .models import Ratings
import datetime as dt

class RatingsTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.type= Ratings(design =1)

    def test_instance(self):
        self.assertTrue(isinstance(self.type,Ratings))

    def test_init(self):
       
        self.assertTrue(self.type.design == 1)

  
    def tearDown(self):
       Ratings.objects.all().delete()
       

