from django.urls import path
from .import  views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('mapbox/', views.MapboxView.as_view(), name='map_box'),
]
