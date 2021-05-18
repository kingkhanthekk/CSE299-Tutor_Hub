from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from django.forms import ModelForm
from home.models import Student,Tutor,ReviewAndComment
from courses.models import Class,Lecture


class CreateClassForm(ModelForm):
    """
    This is a conceptual class representation of Create Class Form for tutor to be used in template.
    
    :param ModelForm: It inherits built-in functionalities of django ModelForm, which handels all validations
    :type ModelForm: ModelForm

    """
    title = forms.CharField(label='Course Name', max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    class Meta:
        model = Class
        fields = ['title', 'description']

class CreateLectureForm(forms.ModelForm):
    """
    This is a conceptual class representation of Create lecture Form for tutor to be used in template.
    
    :param ModelForm: It inherits built-in functionalities of django `forms.ModelForm`, which handels all validations
    :type ModelForm: `forms.ModelForm`
    
    """
    class Meta:
        model = Lecture
        fields = ('name','position','description','video','ppt','notes')


class ReviewAndCommentForm(forms.ModelForm):
    """
        This is a conceptual class representation of Create lecture Form for tutor to be used in template.
        
        :param ModelForm: It inherits built-in functionalities of django `forms.ModelForm`, which handels all validations
        :type ModelForm: `forms.ModelForm`
        
    """
    comment = forms.CharField(label='subject', max_length=200, widget=forms.Textarea(
        attrs={'class': "form-control", 'placeholder': "Write Subject"}))
    class Meta:
        model = ReviewAndComment
        fields = ['comment','rate'] 