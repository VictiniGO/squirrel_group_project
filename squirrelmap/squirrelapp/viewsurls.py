from django.urls import path
  
from . import views
urlpatterns = [
    path('',views.sightingslist),
    path('add/',views.sightingsadd),
    path('stats/',views.sightingsstats),
    # Need to find out how to direct to path /sightings/<unique-squirrel-id>
    # path('',views.sightingslist),
    ]
