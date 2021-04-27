'''
This program is used to take the data from the model to the templates. 
It controls the data, and returns to the template to show necessary output.
'''
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Profile
from django.contrib.auth.models import User
from .models import Ad_Student
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from django.urls import reverse


@login_required
def profile(request):
    '''
    This will redirect the url to the profile page
    :type request: HttpResponse
    :param request: Takes the request to show profile.html

    '''
    return render(request, 'profile.html', {})


@login_required
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


@login_required
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


@login_required
def view_more(request, pk):
    '''
    This will redirect the url to the view more page
    :type request: HttpResponse
    :param request: Takes the request to show view_more.html

    '''
    ad = Ad_Student.objects.get(id=pk)
    return render(request, 'view_more.html', {'ad': ad})


@login_required
def home(request):
    '''
    This will redirect the url to the home page
    :type request: HttpResponse
    :param request: Takes the request to show home.html
    '''
    ads = Ad_Student.objects.order_by('-ad_created')
    context = {}
    context["ads"] = ads
    if "area" in request.GET:
        a = request.GET["area"]
        s = request.GET["salary"]
        sub = request.GET["subject"]
        g = request.GET["gender"]
        # result = Ad_Student.objects.filter(area__icontains=a)
        result = Ad_Student.objects.filter(
            Q(area__icontains=a) & Q(salary__gte=s)
            & Q(subject__icontains=sub) & Q(gender=g))
        context["ads"] = result
        context["search"] = "search"

    return render(request, 'home.html', context)
