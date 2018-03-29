# coding: utf-8
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^$', csrf_exempt(views.testmode), name='testmode'),

]