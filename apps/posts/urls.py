from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.post, name='post'),
    url(r'^order/$', views.order, name='order'),
    url(r'^confirm_order/$', views.confirm_order, name='order'),
    url(r'^(?P<post_id>\d+)/delete/$', views.delete, name='delete_post'),
]