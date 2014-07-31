from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$/?', WebDevMainView.as_view(), name='webdev.main'),
)