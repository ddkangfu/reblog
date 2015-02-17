from django.conf.urls import patterns, include, url
from django.contrib import admin

from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)


#from django.conf import settings

#if not settings.DEBUG:
#    urlpatterns += patterns('',
#        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
#            'document_root': settings.STATIC_ROOT,
#        }),
#    )