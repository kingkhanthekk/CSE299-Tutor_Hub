from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from courses import views

urlpatterns = [
    path('joinClass/', views.join_class, name='join_class'),
    path('studentDashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/class/<slug:slug>/', views.student_lecture_list_View,
         name='student_lecture_list_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
