from django.test import TestCase
from .models import Location, Image, Category
# Create your tests here.

#Location Testcases

class TestLocation(TestCase):
    def setUp(self):
        self.location=Location(location = "Location1")

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))