from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.posts import views as post_views
from apps.feide import views as feide_views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', include('apps.posts.urls')),
    url(r'^printers/', include('apps.printers.urls')),
    #url(r'^bujumbura/', include('apps.bujumbura.urls')),
    url(r'^auth/', include('apps.auth.urls')),

    url(r'^post/', post_views.post, name='post'),
    url(r'^order/', post_views.order, name='order'),
    url(r'^confirm_order/', post_views.confirm_order, name='order'),
    url(r'^(?P<post_id>\d+)/delete/', post_views.delete, name='delete_post'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^login/', feide_views.login),
    url(r'^logout/', feide_views.logout),
)
