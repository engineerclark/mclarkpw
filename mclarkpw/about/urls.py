from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$/?', MainView.as_view(), name='about.main'),
)