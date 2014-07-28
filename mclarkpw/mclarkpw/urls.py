from django.conf.urls import patterns, include, url
from about.views import MainView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mclarkpw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$/?', MainView.as_view()),
    url(r'^about/', include('about.urls')),
    url(r'^web/', include('webdev.urls')),
)
