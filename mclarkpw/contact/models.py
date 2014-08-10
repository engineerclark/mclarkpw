from django.db import models
from django_extensions.db.models import TimeStampedModel

class Contact(TimeStampedModel):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    subject=models.CharField(max_length=256)
    message=models.TextField()