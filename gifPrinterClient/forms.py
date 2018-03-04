from django.forms import ModelForm
from .models import Upload
from .signals import *

class gifForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('gif',)
