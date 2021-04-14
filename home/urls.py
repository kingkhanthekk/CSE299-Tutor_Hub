from django.urls import path
from . import views
from ad import views as ad_View

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('home/', ad_View.home, name='home'),
    path('signout/', views.signout, name='signout'),
]


