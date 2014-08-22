from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
from datetime import datetime, timedelta
import pytz

class Contact(TimeStampedModel):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    subject=models.CharField(max_length=256)
    message=models.TextField()
    
    def send(self):
        mail_from = settings.MAIL_FROM
        mail_to = settings.MESSAGES_TO
        context = Context({'name' : self.name, 'email' : self.email, 'subject' : self.subject, 'message' : self.message})
        message = get_template('contact/email/message.txt').render(context)
        send_mail(self.subject, message, mail_from, mail_to)
        
    @staticmethod
    def can_send():
        yesterday = datetime.now(pytz.utc) - timedelta(hours=24)
        return Contact.objects.filter(created__gte=yesterday).count() <= settings.MAX_DAILY_MESSAGES