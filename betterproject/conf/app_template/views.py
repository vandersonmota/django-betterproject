#coding: utf-8
from django import http

def hello_world(request):
    return http.HttpResponse("Hello World")
