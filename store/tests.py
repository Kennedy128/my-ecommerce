from django.test import TestCase

from django.test import TestCase

from .models import Image,Profile

# Create your tests here.
class ImageTestClass(TestCase):
    '''
    test class to test methods of the  image class
    '''
    def setUp(self):
        self.profile=Profile(user="Kennedy",profile_pic="pic",bio="person")
        self.image=Image(image="image",name="image",caption="nice",profile=self.profile)
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 

    def test_delete_method(self):
        self.image.delete_image()
        images=Image.objects.all()
        self.assertTrue(len(images) > 0)        

class ProfileTestClass(TestCase):
    '''
    test class to test methods of the profile class
    '''
    def setUp(self):
        self.profile=Profile(user="Kennedy",profile_pic="pic",bio="person")

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile.delete_profile()
        profiles= Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

# Create your tests here.
