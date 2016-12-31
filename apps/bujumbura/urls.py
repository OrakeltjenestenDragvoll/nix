from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hits_pr_day/$', views.hits_pr_day, name='bujumbura-hitsaday'),
    url(r'^hit_pr_day_stacked/$', views.hits_pr_day_stacked, name='bujumbura-hitsadaystacked'),
    url(r'^weekday/$', views.weekday, name='bujumbura-weekday'),
    url(r'^api/report/$', views.report, name='bujumbura-report'),
    url(r'^keys/$', views.get_key, name='bujumbura-key'),
    url(r'^get_hits_last_month/$', views.get_last_monthly, name='get_last_monthly'),


]