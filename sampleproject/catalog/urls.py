#encoding: utf-8

from django.conf.urls import patterns, include, url

from .views import Catalog1, Catalog2

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', Catalog1.as_view(), name='catalog1'),
    url(r'^list/$', Catalog2.as_view(), name='catalog2'),
)
