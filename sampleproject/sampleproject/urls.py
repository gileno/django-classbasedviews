#encoding: utf-8

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic import TemplateView

from core.views import Home1, Home2, Home4

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^home1/$', Home1.as_view(), name='home1'),
    url(r'^home2/$', Home2.as_view(), name='home2'),
    url(r'^home3/$', TemplateView.as_view(template_name='home3.html'), 
        name='home3'),
    url(r'^home4/$', Home4.as_view(), name='home4'),

    url(r'^catalog/', include('catalog.urls')),
)
