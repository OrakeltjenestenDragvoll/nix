from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^update/$', views.update, name='update'),
    url(r'^printmon/$', views.printmon, name='printmon'),
    url(r'^logs/$', views.logs, name='logs'),
]