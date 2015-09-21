from django.conf.urls import patterns, url
from neuro import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^page/(?P<date>([0-9]{4}-[0-9]{2}-[0-9]{2}))/(?P<order>[0-9]{2})/$', views.page, name='page'),
                       )
