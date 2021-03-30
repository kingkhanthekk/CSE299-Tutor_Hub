from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


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
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
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
def home(request):
    '''
    This will redirect the url to the homepage
    :type request: HttpResponse
    :param request: Takes the request to show home.html
    
    '''
    return render(request, 'home/home.html')