from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$/?', ContactMainView.as_view(), name='contact.main'),
)