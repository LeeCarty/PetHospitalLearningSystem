# coding: utf-8
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^login$', csrf_exempt(views.login), name='login'),
    url(r'^register$', csrf_exempt(views.register), name='register'),
]