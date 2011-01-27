#coding: utf-8
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^hello_world$', 'views.hello_world'),
)
