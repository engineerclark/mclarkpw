from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$/?', EnterpriseMainView.as_view(), name='enterprise.main'),
)