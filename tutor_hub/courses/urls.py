from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from courses import views

urlpatterns = [
    path('joinClass/', views.join_class, name='join_class'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
