from django.urls import path
from . import views

urlpatterns = [
    path('findTutor/', views.student_Ad, name='findTutor'),
    path('findStudent/', views.tutor_Ad, name='findStudent'),
    path('home/', views.home, name='home'),
    path('myAd/', views.myAd, name='myad')
]