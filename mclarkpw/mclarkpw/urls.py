from django.conf.urls import patterns, include, url
from about.views import MainView
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MainView.as_view(), name='home'),
    url(r'^about/', include('about.urls')),
    url(r'^web/', include('webdev.urls')),
    url(r'^enterprise/', include('enterprise.urls')),
    url(r'^contact/', include('contact.urls')),
    
    url(r'^login/?$', 'django.contrib.auth.views.login', {'template_name':'auth/login.html'}, name='login'),
    url(r'^logout/?$', 'django.contrib.auth.views.logout_then_login', {'login_url':'/'}, name='logout'),
    
    url(r'^portal/', include('portal.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
