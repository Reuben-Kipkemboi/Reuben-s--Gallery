from unicodedata import category
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
        
 # Testing Save Method
    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
        
#-------------Tets class Category------------------------------------

class TestCategory(TestCase):
    def setUp(self):
        self.new_category=Category(category = "test_category1")

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))
        
 # Testing Save Method
    def test_save_method(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
        
        
        
        
#-------------Tets class Image------------------------------------

class TestImage(TestCase):
    def setUp(self):
        
        self.location = Location(location=' Mountain')
        self.location.save_location()

        self.category = Category(category='Travel')
        self.category.save_category()
        
        self.new_Image=Image(image = "photos/test_img1",name ="jungle", description="Jungle is Jungle", location_id = self.location, category_id= self.category)

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_Image,Image))
        
 # Testing Save Method
    def test_save_method(self):
        self.new_Image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

        
