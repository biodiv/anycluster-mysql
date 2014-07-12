from django.conf.urls import patterns, url
from anycluster import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^grid/(\d+)/(\d+)/$', views.getGrid, name='getGrid'),
    url(r'^kmeans/(\d+)/(\d+)/$', views.getPins, name='getPins'),
    url(r'^centroid/(\d+)/(\d+)/$', views.getCentroids, name='getCentroids'),
    url(r'^getClusterContent/kmeans/(\d+)/(\d+)/$', views.getClusterContent, name='getClusterContent'),
    url(r'^getClusterContent/centroid/(\d+)/(\d+)/$', views.getCentroidContent, name='getCentroidContent'),
    url(r'^getAreaContent/(\d+)/(\d+)/$', views.getAreaContent, name='getAreaContent'),
)
