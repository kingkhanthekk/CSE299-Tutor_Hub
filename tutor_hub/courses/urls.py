from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from courses import views

urlpatterns = [
    path('createClass/',views.create_class, name='create_class'),
    path('tutorDashboard/',views.tutor_dashboard, name='tutor_dashboard'),
    path('tutor/class/<slug:slug>/',views.tutor_lecture_list_View, name='tutor_lecture_list_view'),
    path('tutor/class/<slug:slug>/newLecture',views.create_lecture_view, name='create_lecture'),
    path('tutor/class/<slug:slug>/enrolledStudents',views.enrolled_students, name='enrolled_students'),
    path('tutor/class/<str:class_slug>/<slug:slug>/detail',views.tutor_lecture_detail_View, name='tutor_lecture_details'),
    path('tutor/class/<str:class_slug>/<slug:slug>/update',views.LectureUpdateView.as_view(), name='tutor_lecture_update'),
    path('tutor/class/<str:class_slug>/<slug:slug>/delete',views.LectureDeleteView.as_view(), name='tutor_lecture_delete'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
