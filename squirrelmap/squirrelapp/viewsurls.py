from django.urls import path, re_path
  
from . import views

app_name = 'squirrelapp'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('add/',views.sightingsadd,name = 'add'),
    path('stats/',views.sightingsstats),
    path('<slug:squirrel_id>/', views.update, name='update'),
    ]
