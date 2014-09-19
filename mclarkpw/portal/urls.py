from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^(?P<token>[0-9a-f]{32})/?$', views.TokenAuth, name='portal.tokenauth'),
)