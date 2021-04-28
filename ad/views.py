from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Ad_Student, Ad_Tutor
from .forms import Ad_Student_Form, Ad_Tutor_Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from home.models import Student,Tutor


@login_required
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


@login_required
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

@login_required
def home(request):
    studentAds = Ad_Student.objects.order_by('-ad_created')
    tutorAds = Ad_Tutor.objects.order_by('-ad_created')
    return render(request, 'ad/home.html', {'studentAds': studentAds, 'tutorAds': tutorAds})

@login_required
def myAd(request):
    myStudentAds = Ad_Student.objects.filter(user=request.user).order_by('-ad_created')
    myTutorAds = Ad_Tutor.objects.filter(user=request.user).order_by('-ad_created')
    return render(request, 'ad/myad.html', {'myStudentAds': myStudentAds, 'myTutorAds': myTutorAds})