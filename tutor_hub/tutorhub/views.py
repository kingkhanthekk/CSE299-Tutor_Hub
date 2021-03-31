from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User


def profile(request):
    return render(request, 'profile.html', {})


def edit_profile(request):
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
