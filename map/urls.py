from django.urls import path
from map import views

app_name="map"

urlpatterns=[
    path('',views.index_map,name='index-map'),
    path('heat-map',views.heat_map,name='heat-map'),
    path('cluster-map',views.cluster_map,name='cluster-map'),
    path('env-map',views.env_map,name='env-map'),
    path('analyze',views.analyze,name='analyze'),
]