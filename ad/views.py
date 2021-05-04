from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Ad_Student, Ad_Tutor
from .forms import Ad_Student_Form, Ad_Tutor_Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from home.models import Student,Tutor
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# feature - 1
def student_Ad(request):
    User = get_user_model()
    users = User.objects.all()
    if request.method == 'GET':
        return render(request, 'ad/student_ad.html', {'form': Ad_Student_Form() })
    else:
        try: 
            form = Ad_Student_Form(request.POST)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'ad/student_ad.html', {'form': Ad_Student_Form(), 'error': 'Limit is Crossed' })



def tutor_Ad(request):
    User = get_user_model()
    users = User.objects.all()
    if request.method == 'GET':
        return render(request, 'ad/tutor_ad.html', {'form': Ad_Tutor_Form() })
    else:
        try: 
            form = Ad_Tutor_Form(request.POST)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'ad/tutor_ad.html', {'form': Ad_Tutor_Form(), 'error': 'Limit is Crossed' })


def home(request):
    studentAd_list = Ad_Student.objects.order_by('-ad_created')
    tutorAd_list = Ad_Tutor.objects.order_by('-ad_created')
    
    #Paginator for Student Posts
    paginator = Paginator(studentAd_list, 5)
    page = request.GET.get('page')
    try:
        studentAds = paginator.page(page)
    except PageNotAnInteger:
        studentAds = paginator.page(1)
    except EmptyPage:
        studentAds = paginator.page(paginator.num_pages)
    
    #Paginator for Tutor Posts
    paginator = Paginator(tutorAd_list, 5)
    page = request.GET.get('page')
    try:
        tutorAds = paginator.page(page)
    except PageNotAnInteger:
        tutorAds = paginator.page(1)
    except EmptyPage:
        tutorAds = paginator.page(paginator.num_pages)
        
    return render(request, 'ad/home.html', {'studentAds': studentAds, 'tutorAds': tutorAds})


# feature - 2
def myAd(request):
    '''
    This will redirect the url to the myAd page
    :type request: HttpResponse
    :param request: Takes the request to show myad.html
    '''
    myStudentAds = Ad_Student.objects.filter(user=request.user).order_by('-ad_created')
    myTutorAds = Ad_Tutor.objects.filter(user=request.user).order_by('-ad_created')
    return render(request, 'ad/myad.html', {'myStudentAds': myStudentAds, 'myTutorAds': myTutorAds})



def delete_post_Student(request,post_pk):
    '''
    This will redirect the url to the delete page
    :type request: HttpResponse
    :param request: Takes the request to show delete_post.html
    :param post_pk: Gets value of id of the selected ad
    '''
    student_post = Ad_Student.objects.get(id=post_pk)
    if request.method == 'POST':
        student_post.delete()
        return redirect('myAd')
    return render(request, 'ad/delete_post_student.html', {'student_post': student_post})


def delete_post_Tutor(request,post_pk):
    '''
    This will redirect the url to the delete page
    :type request: HttpResponse
    :param request: Takes the request to show delete_post.html
    :param post_pk: Gets value of id of the selected ad
    '''
    tutor_post = Ad_Tutor.objects.get(id=post_pk)
    if request.method == 'POST':
        tutor_post.delete()
        return redirect('myAd')
    return render(request, 'ad/delete_post_tutor.html', {'tutor_post': tutor_post})


def ad_profile(request, user_pk):
    '''
    This will redirect the url to the profile page
    :type request: HttpResponse
    :param request: Takes the request to show ad_profile.html
    :param user_pk: Gets value of user id of the specific user 
    '''
    User = get_user_model()
    user = User.objects.get(id=user_pk)
    return render(request, 'ad/ad_profile.html', {'user': user})
    
    
    