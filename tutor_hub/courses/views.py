from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import  redirect,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from courses.forms  import  CreateClassForm,CreateLectureForm,ReviewAndCommentForm
from courses.models import Class,Lecture
from home.models import Tutor,Student,ReviewAndComment,User
from django.views.generic import TemplateView,DetailView,ListView,FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

def create_class(request):
    '''
    This will redirect the url to the create_class page, where a logged in tutor can create a new class and after successful class creation tutor will be redirected to tutor dashboard
    
    :param request: Takes the request to show create_class.html
    :type request: HttpResponse
    :return: returns arequest for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    
    '''
    form = CreateClassForm()
    if request.method == 'POST':
        form = CreateClassForm(request.POST,request.FILES)
        if form.is_valid():
            new_class = form.save()
            new_class.tutor = request.user.tutor
            new_class.save()
            return redirect('tutor_dashboard')
    context = {'form': form}
    return render(request, 'courses/create_class.html', context)

@login_required
def tutor_dashboard(request):
    '''
    This will redirect the url to the tutor_dashboard page, where a logged in tutor can view all of the class he/she created
    
    :param request: Takes the request to show tutor_dashboard.html
    :type request: HttpResponse
    :return: returns arequest for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    
    '''
    tutor = request.user.tutor
    classes = Class.objects.filter(tutor=tutor)
    context = {'classes': classes}
    return render(request, 'courses/tutor_dashboard.html', context)



def tutor_lecture_list_View(request, slug):
    '''
    This will redirect the url to the tutor_lecture_list page, where a logged in tutor can view all of the lectures in a list view of a specific class
    
    :param request: Takes the request to show tutor_lecture_list_view.html
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
    return render(request, 'courses/tutor_lecture_list_view.html', context)




def create_lecture_view(request,slug):
    '''
    This will redirect the url to the create_lecture page, where a logged in tutor can fillup a form to create a lecture of a specific class
    
    :param request: Takes the request to show create_lecture.html
    :type request: HttpResponse
    :param slug: Takes the class slug from url to slect a particular class from class model
    :type slug: Slug
    :return: returns arequest for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    
    '''
    form = CreateLectureForm()
    class_object = Class.objects.get(slug=slug)
    if request.method == 'POST':
        form = CreateLectureForm(request.POST,request.FILES)
        if form.is_valid():
            new_lecture = form.save(commit=False)
            new_lecture.created_by = request.user.tutor
            new_lecture.class_content=Class.objects.get(slug=slug)
            new_lecture.save()
            return redirect('tutor_dashboard')
    context = {'form': form, 'class':class_object }
    return render(request, 'courses/create_lecture.html', context)

def enrolled_students(request, slug):
    '''
    This will redirect the url to the enrolled_student page, where a logged in tutor can view list of enrolled students
    
    :param request: Takes the request to show enrolled_students.html
    :type request: HttpResponse
    :param slug: Takes the class slug from url to slect a particular class from class model
    :type slug: Slug
    :return: returns arequest for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    
    '''
    # teacher = request.user.teacher
    class_object = Class.objects.get(slug=slug)
    students = class_object.students.all()
    context = {'students': students, 'class': class_object}
    return render(request, 'courses/enrolled_students.html', context)

def tutor_lecture_detail_View(request,class_slug,slug):
    '''
    This will redirect the url to the lecture_detaails page, where a logged in tutor can view lecture details of a specific lecture of a certain course
    
    :param request: Takes the request to show enrolled_students.html
    :type request: HttpResponse
    :param class_slug: Takes the class slug from url to slect a particular class from class model
    :type slug: Slug
    :param slug: Takes the lecture slug of a specific class from url to slect a particular lecture from Lecture model
    :type slug: Slug
    :return: returns arequest for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    
    '''
    # student = request.user.student
    class_object = Class.objects.get(slug=class_slug)
    lectures = class_object.lessons.filter(slug=slug)
    context = {'lectures': lectures, 'class': class_object}
    return render(request, 'courses/tutor_lecture_detail_view.html', context)



class LectureUpdateView(UpdateView):
    '''
    This will redirect the url to the lecture_list page, where a logged in tutor can view all the lecture list of a specific class
    
    :param UpdateView: Takes the request to show update_lecture.html
    :type UpdateView: UpdateView
    :return: returns arequest for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    
    '''
    fields =('name','position','description','video','ppt','notes')
    model=Lecture
    template_name='courses/lecture_update.html'
   

class LectureDeleteView(DeleteView):
    '''
    This will redirect the url to the lecture_list page, where a logged in tutor can view all the lecture list of a specific class
    
    :param DeleteView: Takes the request to show delete_lecture.html
    :type UpdateView: UpdateView
    :return: returns arequest for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    
    '''
    model=Lecture
    template_name='courses/lecture_delete.html'

    def get_success_url(self):
        Class= self.object.class_content.slug
        Lecture = self.object.slug
        return reverse_lazy('tutor_lecture_list_view',kwargs={'slug':self.object.class_content.slug})

