from django.forms import ModelForm
from .models import Image,Profile

class AddImageForm(ModelForm):
    class Meta:
        model = Image
        exclude = ['comments', 'likes', 'profile']


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']