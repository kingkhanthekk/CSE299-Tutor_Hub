from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createPostView, name='createAd'),
    path('home/', views.home, name='home'),
]