from django import forms
from django.forms import ModelForm, fields
from .models import Ad_Student, Ad_Tutor


class Ad_Student_Form(ModelForm):
    class Meta:
        model = Ad_Student
        fields = '__all__'
        
class Ad_Tutor_Form(ModelForm):
    class Meta:
        model = Ad_Tutor
        fields = '__all__'
    