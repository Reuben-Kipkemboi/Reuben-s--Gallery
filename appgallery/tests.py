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
        
       #clearing every image, location & category instance properties
    def teardown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_Image,Image))
        
# Testing Save Method
    def test_save_method(self):
        self.new_Image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
        
        
# #delete
    def test_deleteImage(self):
        self.new_Image.save_image()
        self.new_image2 = Image.objects.create(image ='photos/test_img3.jpg', name = 'Jpg image', description= 'Png and jpg are image formats', location_id=self.location, category_id=self.category)
        Image.delete_image(self.new_Image.id)
        self.assertTrue(len(Image.objects.all())==1)
        
#Test update method
    def test_updateImage(self):
        self.new_Image.save_image()
        self.new_Image.update_image(self.new_Image.id, 'photos/test_img2.jpg')
        new_updated_image = Image.objects.get(id=self.new_Image.id)
        self.assertEqual(new_updated_image.image, 'photos/test_img2.jpg')



        
