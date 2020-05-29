from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='insta/')
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

    @classmethod
    def update_caption(cls,id,caption):
        cls.objects.filter(id=id).update(caption=caption)
        updated_caption = cls.objects.get(id=id)
        return updated_image

    @classmethod
    def search_image(cls,search_term):
        images = cls.objects.filter(img_name__icontains=search_term)
        return images



class Profile(models.Model):
    profile_photo = models.CharField(max_length=30)
    bio = models.CharField(max_length=30)

    def __str__(self):
        self.bio