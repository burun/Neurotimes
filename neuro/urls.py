from django.conf.urls import patterns, url
from neuro import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^page/', views.page, name='page'),
                       )
