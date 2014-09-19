from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
import pytz
import uuid

class TokenManager(models.Manager):
    def get_queryset(self):
        return super(TokenManager, self).get_queryset().filter(expiration__gt=datetime.now(pytz.utc))

class AuthToken(TimeStampedModel):
    value=models.CharField(max_length=128)
    expiration=models.DateTimeField()
    user=models.ForeignKey(User)
    
    objects=models.Manager()
    current_objects=TokenManager()
    
    @classmethod
    def create(cls, user, expiration=None):
        token = cls()
        token.value = uuid.uuid4().hex
        if not expiration:
            expiration = datetime.now(pytz.utc) + settings.DEFAULT_AUTHTOKEN_EXP
        token.expiration = expiration
        token.user = user
        token.save()
        return token
    
    
