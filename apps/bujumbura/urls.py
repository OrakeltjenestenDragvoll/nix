from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^hits_pr_day/', views.hits_pr_day, name='bujumbura-hitsaday'),
    url(r'^hit_pr_day_stacked/', views.hits_pr_day_stacked, name='bujumbura-hitsadaystacked'),
    url(r'^weekday/', views.weekday, name='bujumbura-weekday'),
)