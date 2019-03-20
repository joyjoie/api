from django.test import TestCase
import datetime as dt
# Create your tests here.
from .models import Ratings,Profile
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
       

class ProfileTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.type= Profile(bio ="me")

    def test_instance(self):
        self.assertTrue(isinstance(self.type,Profile))

    def test_init(self):
       
        self.assertTrue(self.type.bio == "me")

  
    def tearDown(self):
       Profile.objects.all().delete()
