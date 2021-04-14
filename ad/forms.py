from django import forms
from django.forms import ModelForm, fields
from .models import Ad_Student


class Ad_Student_Form(ModelForm):
    class Meta:
        model = Ad_Student
        fields = '__all__'
    