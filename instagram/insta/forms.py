from django.forms import ModelForm
from .models import Image

class AddImageForm(ModelForm):
    class Meta:
        model = Image
        exclude = ['comments', 'likes', '']