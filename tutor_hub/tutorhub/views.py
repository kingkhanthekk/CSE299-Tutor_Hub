from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User
from django.urls import reverse_lazy


def profile(request):
    '''
    This will redirect the url to the profile page
    :type request: HttpResponse
    :param request: Takes the request to show profile.html

    '''
    return render(request, 'profile.html', {})


def edit_profile(request):
    '''
    This will redirect the url to the edit profile page
    :type request: HttpResponse
    :param request: Takes the request to show edit_profile.html

    '''
    if request.method == "POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]

        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        usr.save()
    return render(request, 'edit_profile.html', {})


def delete_profile(request):
    '''
    This will redirect the url to the delete profile page
    :type request: HttpResponse
    :param request: Takes the request to show delete_profile.html

    '''
    usr = User.objects.get(id=request.user.id)
    if request.method == "POST":
        usr.delete()
    # success_url = reverse_lazy('Signup')
    return render(request, 'delete_profile.html', {})
