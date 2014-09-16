from django.db import models
from django_extensions.db.models import TimeStampedModel
import markdown

class Tag(TimeStampedModel):
    name = models.CharField(max_length=64)
    
class PositionManager(models.Manager):
    def get_queryset(self):
        return super(PositionManager, self).get_queryset().filter(hide=False)

class Position(TimeStampedModel):
    company = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    hide = models.BooleanField(default=False, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    
    objects = PositionManager()
    including_hidden = models.Manager()
    
    def render_description(self):
        return markdown.markdown(self.description)
    
class School(TimeStampedModel):
    program = models.CharField(max_length=128)
    school = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    hide = models.BooleanField(default=False, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    
    objects = PositionManager()
    including_hidden = models.Manager()
    
    def render_description(self):
        return markdown.markdown(self.description)
    
    