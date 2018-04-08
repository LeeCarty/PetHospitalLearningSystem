# coding: utf-8
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^test_type$', csrf_exempt(views.test_type), name='test_type'),
    url(r'^test_manage$', csrf_exempt(views.test_manage), name='test_manage'),
    url(r'^test_choice/(?P<type_id>[1-6])$', csrf_exempt(views.test_choice), name='test_choice'),
    url(r'^test_choice/(?P<search_key>.+)', csrf_exempt(views.paper_search), name='paper_search'),
    url(r'^test_paper/(?P<paper_id>[0-9]+)$', csrf_exempt(views.test_paper), name='test_paper'),
    url(r'^paper_submit$', csrf_exempt(views.paper_submit), name='paper_submit'),

]