from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls import patterns
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns(
        'jango.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root' : settings.MEDIA_ROOT}), )
