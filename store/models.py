from django.db import models

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    '''
    profile class to define profile objects
    '''
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to = 'images/')
    profile_pic = CloudinaryField('image')
    bio=models.CharField(max_length = 100)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    def delete_profile(self):
        '''
        method that deletes post from database
        '''
        self.delete()    

    @classmethod
    def search_by_name(cls,search_term):
        '''
        method that rerieves a user by use of username
        '''
        name = cls.objects.filter(user__username__icontains = search_term)
        return name


class Image(models.Model):
    '''
    image class to define image objects
    '''
    image=models.ImageField(upload_to = 'images/')
    image = CloudinaryField('image')
    name=models.CharField(max_length = 100)
    caption=models.CharField(max_length = 100,blank=True)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    def __str__(self):
        '''
        Setting up self
        '''
        return self.name

    def save_image(self):
        '''
        method that saves post to database
        '''
        self.save()

    def delete_image(self):
        '''
        method that deletes post from database
        '''
        self.delete()
    

    @classmethod
    def update_caption(cls,id,caption):
        '''
        method to update caption
        '''
        captions=cls.objects.filter(caption_id=id).update(caption = caption)
        return captions

    @classmethod
    def get_image_by_id(cls,image_id):
        images=cls.objects.get(id=image_id)
        return images      

class Comments(models.Model):
    '''
    Comment class for comment objects
    '''
    comment= models.TextField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image_id=models.ForeignKey(Image, on_delete=models.CASCADE,null=True)

    def __str__(self):
        '''
        Setting up self
        '''
        return self.comment

    @classmethod
    def get_comments(cls):
        '''
        Method for getting all the comments posted
        '''
        comment=cls.objects.all()
        return comment

    @classmethod
    def get_singlepost_comments(cls, id):
        '''
        function that gets comments for a single post
        '''
        comments=cls.objects.filter(image_id=id)
        return comments
    def save_comment(self):
        '''
        function that saves a new comment
        '''
        self.save()

    def delete_comment(self):
        '''
        function that deletes a comment
        '''
        self.delete()  

           

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    
    def save_like(self):
        self.save()
