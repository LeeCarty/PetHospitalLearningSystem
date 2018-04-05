# coding: utf-8
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^test_type$', csrf_exempt(views.test_type), name='test_type'),
    url(r'^test_manage$', csrf_exempt(views.test_manage), name='test_manage'),
    url(r'^test_choice/(?P<type_id>[1-6])$', csrf_exempt(views.test_choice), name='test_choice'),
]