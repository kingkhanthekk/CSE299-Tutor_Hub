'''
This program will create a django model form.
'''

from django import forms
from django.forms import ModelForm, fields
from .models import AdStudent, AdTutor


class AdStudentForm(ModelForm):
    '''
    This is a conceptual Form representation of Class table for student ads.
    :param ModelForm: It creates built-in html form of django, which handels all validations in django Admin panel.
    :type ModelForm: model, fields
    '''
    class Meta:
        model = AdStudent
        fields = '__all__'
        
class AdTutorForm(ModelForm):
    '''
    This is a conceptual Form representation of Class table for tutor ads.
    :param ModelForm: It creates built-in html form of django, which handels all validations in django Admin panel.
    :type ModelForm: model, fields
    '''
    class Meta:
        model = AdTutor
        fields = '__all__'
    