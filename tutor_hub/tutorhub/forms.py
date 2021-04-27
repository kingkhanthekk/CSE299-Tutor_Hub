'''
This program is used to create a form that will save take the input
and save into the database.
'''
from django import forms
from django.forms import ModelForm, fields
from .models import Ad_Student


class Ad_Student_Form(ModelForm):
    '''
    This class will create a form Ad_Student_Form.
    '''
    class Meta:
        model = Ad_Student
        fields = '__all__'
