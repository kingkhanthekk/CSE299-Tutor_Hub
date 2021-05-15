from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from courses.forms import CreateClassForm, CreateLectureForm, ReviewAndCommentForm
from courses.models import Class, Lecture
from home.models import Tutor, Student, ReviewAndComment, User
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def join_class(request):
    '''
    This will redirect the url to the join_class page, where a logged in student can join a new class and after successful class join student will be redirected to student dashboard

    :param request: Takes the request to show join_class.html
    :type request: HttpResponse
    :return: returns arequest for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary

    '''
    if request.method == 'POST':
        class_code = request.POST.get('class_code')
        try:
            myClass = Class.objects.get(class_code=class_code)
            student = request.user.student
            myClass.students.add(student)
            return redirect('student_dashboard')
        except Class.DoesNotExist:
            messages.info(request, "Invalid Class Code")
    context = {}
    return render(request, 'courses/join_class.html', context)


@login_required
def student_dashboard(request):
    '''
    This will redirect the url to the student_dashboard page, where a logged in student can view all of the class he/she joined

    :param request: Takes the request to show student_dashboard.html
    :type request: HttpResponse
    :return: returns arequest for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary

    '''
    student = request.user.student
    classes = Class.objects.filter(students=student)
    context = {'classes': classes}
    return render(request, 'courses/student_dashboard.html', context)


def student_lecture_list_View(request, slug):
    '''
    This will redirect the url to the student_lecture_list page, where a logged in student can view all of the lectures in a list view of a specific class

    :param request: Takes the request to show student_lecture_list_view.html
    :type request: HttpResponse
    :param slug: Takes the class slug from url to slect a particular class from class model
    :type slug: Slug
    :return: returns arequest for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary

    '''
    # student = request.user.student
    class_object = Class.objects.get(slug=slug)
    lectures = class_object.lessons.all()
    context = {'lectures': lectures, 'class': class_object}
    return render(request, 'courses/student_lecture_list_view.html', context)
