'''
This program will create necessary html hyperlinks to show contents. 
'''
from django.urls import path
from . import views

urlpatterns = [
    path('view_more/<int:pk>/',
         views.view_more, name='view_more'),
]
