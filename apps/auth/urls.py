# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import logout,login

urlpatterns = [
        url(r'^login/$', login, name='auth_login'),
        url(r'^logout/$', logout, name='auth_logout')
]
