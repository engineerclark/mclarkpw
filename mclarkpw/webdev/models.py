from django.db import models
from django_extensions.db.models import TimeStampedModel
from about.models import Tag

import markdown

class Project(TimeStampedModel):
    name = models.CharField(max_length=128)
    url = models.URLField(null=True, blank=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __unicode__(self):
        return self.name

class Screenshot(TimeStampedModel):
    image = models.ImageField(upload_to='screenshots')
    title = models.CharField(max_length=128, default='Screenshot')
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project)
    
