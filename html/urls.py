from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'html.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'main.views.index', name='index'),
    url(r'^element/(?P<id>[0-9]+)/$', 'main.views.element', name='element'),
    url(r'^example/(?P<id>[0-9]+)/$', 'main.views.example', name='example'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),

)
