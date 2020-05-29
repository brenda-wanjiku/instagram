from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.CharField(max_length=30)
    img_name = models.CharField(max_length=60)
    caption = models.CharField(max_length=100)
    likes = models.CharField(max_length=30)
    comments = models.CharField(max_length=30)

    def __str__(self):
        return self.img_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Profile(models.Model):
    profile_photo = models.CharField(max_length=30)
    bio = models.CharField(max_length=30)

    def __str__(self):
        self.bio