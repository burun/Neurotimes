from django.conf.urls import patterns, include, url
from neuro import views, feeds

urlpatterns = patterns('',
                       url(r'^$', views.card, name='index'),
                       url(r'^date/$', views.date, name='date'),
                       url(r'^page/(?P<date>([0-9]{4}-[0-9]{2}-[0-9]{2}))/(?P<id>[0-9]{1,})/$', views.page, name='page'),
                       url(r'^card/$', views.card, name='card'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^message/$', views.message, name='message'),
                       url(r'^feed/', feeds.LatestPosts()),
                       )
