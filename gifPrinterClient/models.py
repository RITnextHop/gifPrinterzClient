from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Upload(models.Model):
    gif = models.ImageField(upload_to='uploads/')

    #def clean(self):
    #    if not self.gif.name.endswith(".gif"):
    #        raise ValidationError("Only .gif image accepted")
