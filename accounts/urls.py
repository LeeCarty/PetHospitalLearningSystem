# coding: utf-8
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^$', csrf_exempt(views.login), name='login'),
    url(r'^register$', csrf_exempt(views.register), name='register'),
    url(r'^password_modify$', csrf_exempt(views.password_modify), name='password_modify'),
    url(r'^email_confirm$', csrf_exempt(views.email_confirm), name='email_confirm'),
]