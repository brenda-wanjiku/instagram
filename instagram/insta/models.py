from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    '''
    Class that defines Image attributes
    '''
    image = models.ImageField(upload_to='insta/')
    img_name = models.CharField(max_length=60)
    caption = models.CharField(max_length=100)
    profile = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    likes = models.CharField(max_length=30)
    comments = models.CharField(max_length=30)

    def __str__(self):
        return self.img_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls,id,caption):
        cls.objects.filter(id=id).update(caption=caption)
        updated_caption = cls.objects.get(id=id)
        return updated_image

    @classmethod
    def search_image(cls,search_term):
        images = cls.objects.filter(img_name__icontains=search_term)
        return images

    @classmethod
    def get_images(cls,profile):
        return cls.objects.filter(profile = profile)



class Profile(models.Model):
    '''
    Class that defines the Profile attributes
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,default="")
    profile_photo =models.ImageField(upload_to='insta/')
    bio = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.user.username


    @receiver(post_save, sender=User)
    def create_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save,sender=User)
    def save_profile(sender,instance, **kwargs):
        instance.profile.save()
