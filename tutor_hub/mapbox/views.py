from django.shortcuts import render
from django.contrib.auth.models import Group, User
from home.models import Student,Tutor
from django.views.generic.base import TemplateView
# Create your views here.

class MapboxView(TemplateView):
    template_name = 'mapbox/mapbox.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token']='pk.eyJ1Ijoibm8tbWFuIiwiYSI6ImNrbzVrNWsybDFkM3oyeGxwNDlnb2NuejcifQ._l4WdUmj555QaAsHY3XQkA'
        context['addresses_tutor']=Tutor.objects.all()
        context['addresses_student']=Student.objects.all()
        return context
