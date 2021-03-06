# coding: utf-8
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^list$', csrf_exempt(views.list), name='list'),
    url(r'^choosecase$', csrf_exempt(views.choosecase), name='choosecase'),
    url(r'^choosecareer$', csrf_exempt(views.choosecareer), name='choosecareer'),
    url(r'^study_02/(?P<name>[\u4e00-\u9fa5]{0,})$', csrf_exempt(views.study_02), name='study_02'),
    url(r'^study_01/(?P<name>[\u4e00-\u9fa5]{0,})$', csrf_exempt(views.study_01), name='study_01'),
]