from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import EditForm_Tutor, EditForm_Student
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth.models import Group, User
from home.models import Student,Tutor


def landing(request):
    '''
    This will redirect the url to the landing page
    :type request: HttpResponse
    :param request: Takes the request to show home.html
    
    '''
    return render(request, 'home/landing.html')



def signup(request):
    '''
    This will redirect the url to the signup
    :type request: HttpResponse
    :param request: Takes the request to show signup.html
    '''
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(data=request.POST)      
        if form.is_valid():
            user = form.save()
            group_name = str(form.cleaned_data.get('group'))
            print(group_name)
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            if group_name == 'student':
                Student.objects.create(user=user)
                
                messages.success(request, 'Account Successfully Created !')
                return redirect('signin')
            
            else:
                Tutor.objects.create(user=user)

                messages.success(request, 'Account Successfully Created !')
                return redirect('signin')
            
        
        context = {'form':form}
        return render(request, 'home/signup.html', context)
    

def signin(request):
    '''
    This will redirect the url to the signin
    :type request: HttpResponse
    :param request: Takes the request to show signin.html
    
    '''
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is wrong')
            
        return render(request, 'home/signin.html')


def signout(request):
    '''
    This will logout the user & redirect to the landing page
    :type request: HttpResponse
    :param request: Takes the request to show landing.html
    
    '''
    logout(request)
    return redirect('landing')


@login_required
def profile(request):
    '''
    This will redirect the url to the profile page
    :type request: HttpResponse
    :param request: Takes the request to show profile.html
    '''
    return render(request, 'profile/profile.html', {})


def edit_profile_tutor(request):
	tutor= request.user.tutor
	form = EditForm_Tutor(instance=tutor)
    

	if request.method == 'POST':
		form = EditForm_Tutor(request.POST, request.FILES,instance=tutor)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'profile/edit_profile_tutor.html', context)


def edit_profile_student(request):
	student= request.user.student
	form = EditForm_Student(instance=student)
	if request.method == 'POST':
		form = EditForm_Student(request.POST, request.FILES,instance=student)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'profile/edit_profile_student.html', context)

def delete_profile(request):
    '''
    This will redirect the url to the delete profile page
    :type request: HttpResponse
    :param request: Takes the request to show delete_profile.html
    '''
    user =  User.objects.get(id=request.user.id)
    if request.method == "POST":
        user.delete()
   
    return render(request, 'profile/delete_profile.html', {})


