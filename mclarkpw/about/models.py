from django.db import models
from django_extensions.db.models import TimeStampedModel

class Tag(TimeStampedModel):
    name = models.CharField(max_length=64)

class Position(TimeStampedModel):
    company = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    
class School(TimeStampedModel):
    program = models.CharField(max_length=128)
    school = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)    
    