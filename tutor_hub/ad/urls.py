'''
This program will create necessary html hyperlinks to show contents. 
'''
from django.urls import path
from . import views

urlpatterns = [
    path('find_tutor/', views.student_ad, name='find_tutor'),
    path('find_student/', views.tutor_ad, name='find_student'),
    path('home/', views.home, name='home'),
    path('profile/user/<int:user_pk>', views.ad_profile, name='profile_user'),
    path('my_ad/', views.my_ad, name='my_ad'),
    path('myAd/delete/student/post/<int:post_pk>', views.delete_post_student, name='delete_post_student'),
    path('myAd/delete/tutor/post/<int:post_pk>', views.delete_post_tutor, name='delete_post_tutor'),
]