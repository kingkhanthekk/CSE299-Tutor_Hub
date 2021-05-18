from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from courses import views

urlpatterns = [
    path('createClass/',views.create_class, name='create_class'),
    path('joinClass/',views.join_class, name='join_class'),
    path('studentDashboard/',views.student_dashboard, name='student_dashboard'),
    path('tutorDashboard/',views.tutor_dashboard, name='tutor_dashboard'),
    path('student/class/<slug:slug>/',views.student_lecture_list_View, name='student_lecture_list_view'),
    path('tutor/class/<slug:slug>/',views.tutor_lecture_list_View, name='tutor_lecture_list_view'),
    path('tutor/class/<slug:slug>/newLecture',views.create_lecture_view, name='create_lecture'),
    path('tutor/class/<slug:slug>/enrolledStudents',views.enrolled_students, name='enrolled_students'),
    path('student/class/<str:class_slug>/<slug:slug>/detail',views.student_lecture_detail_View, name='student_lecture_details'),
    path('tutor/class/<str:class_slug>/<slug:slug>/detail',views.tutor_lecture_detail_View, name='tutor_lecture_details'),
    path('tutor/class/<str:class_slug>/<slug:slug>/update',views.LectureUpdateView.as_view(), name='tutor_lecture_update'),
    path('tutor/class/<str:class_slug>/<slug:slug>/delete',views.LectureDeleteView.as_view(), name='tutor_lecture_delete'),
    path('review/<str:tutor_id>/',views.tutor_review,name='review_tutor'),
    path('reviews/<str:tutor_id>/',views.view_tutor_review,name='view_reviews'),
     #path('tutor/createLecture',views.create_lecture_view, name='create_lecture'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
