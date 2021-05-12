'''
This program is the controller that fetch data from models.py and send it to the template file. 
'''
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from ad.models import AdStudent, AdTutor
from ad.forms import AdStudentForm, AdTutorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from home.models import Student, Tutor
from django.db.models import Q


@login_required
def view_more(request, pk):
    '''
    This will redirect the url to the view_more page, where a logged in user can see details of a post on which he clicks the link View More.
    
    :param request: Takes the request to show view_more.html
    :type request: HttpResponse
    :param pk: Gets value of the selected ad's id through a link
    :type pk: int
    :return: returns a request for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    '''
    # usr = User.objects.get(username=request.user)
    # ad = AdTutor.objects.get(id=pk)
    if request.user.groups.filter(name='student').exists():
        ad = AdTutor.objects.get(id=pk)
    else:
        ad = AdStudent.objects.get(id=pk)
    # stu_ad = Ad_Student.objects.get(id=pk)
    # ad = Ad_Tutor.objects.get(id=pk)
    return render(request, 'view_more.html', {'ad': ad})
