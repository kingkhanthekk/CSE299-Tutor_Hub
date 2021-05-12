from django.db import models
from django.contrib.auth.models import User
import os
import os
import math
from django.db.models import Count,Sum,Avg
import geocoder
# Create your models here.

mapbox_access_token = 'pk.eyJ1Ijoibm8tbWFuIiwiYSI6ImNrbzVrNWsybDFkM3oyeGxwNDlnb2NuejcifQ._l4WdUmj555QaAsHY3XQkA'


def path_and_rename(instance, filename):
    upload_to = 'images/'
    extension = filename.split('.')[-1]

    #get filename
    if instance.user.username:
        filename = 'User_profile_pictures/{}.{}'.format(instance.user.username, extension)
    
    return os.path.join(upload_to,filename)
     

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    institution= models.CharField(max_length=150, null=True, blank=True)
    department= models.CharField(max_length=150, null=True, blank=True)
    class_level= models.CharField(max_length=150, null=True, blank=True)
    address= models.CharField(max_length=150, null=True, blank=True)
    area= models.CharField(max_length=150, null=True, blank=True)
    city= models.CharField(max_length=150, null=True, blank=True)
    lat = models.FloatField(null=True,blank=True)
    lon = models.FloatField(null=True,blank=True)

    male ='male'
    female = 'female'
    other = 'other'
    genders = [
        (male,'male'),
        (female,'female'),
        (other,'other'),
    ]
    gender = models.CharField(max_length=15, choices=genders,default=male,null=True,blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    bio = models.CharField(max_length=450, blank=True,null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)

    def save(self,*args, **kwargs):
        g=geocoder.mapbox(self.address,key=mapbox_access_token)
        g=g.latlng #(laitude,longitude)
        self.lat= g[0] 
        self.lon= g[1]
        return super(Student, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.user.username

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    institution= models.CharField(max_length=150, null=True, blank=True)
    subject_teach= models.CharField(max_length=150, null=True, blank=True)
    address= models.CharField(max_length=150, null=True, blank=True)
    area= models.CharField(max_length=150, null=True, blank=True)
    city= models.CharField(max_length=150, null=True, blank=True)
    salary_per_month= models.CharField(max_length=150, null=True, blank=True)
    preffered_area= models.CharField(max_length=150, null=True, blank=True)
    online_teach_exp = models.FloatField(max_length=100, null=True, blank=True)
    total_teach_exp = models.FloatField(max_length=100, null=True, blank=True)
    qualification = models.CharField(max_length=250,null=True,blank=True)
    lat = models.FloatField(null=True,blank=True)
    lon = models.FloatField(null=True,blank=True)


    inhouse ='Inhouse'
    online = 'Online'
    both = 'Inhouse & Online'
    tutor_types = [
        (inhouse,'Inhouse'),
        (online,'Online'),
        (both,'Inhouse & Online'),
    ]
    tutor_type = models.CharField(max_length=25, choices=tutor_types,default=inhouse,null=True,blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    bio = models.CharField(max_length=450, blank=True,null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)   

    def save(self,*args, **kwargs):
        g=geocoder.mapbox(self.address,key=mapbox_access_token)
        g=g.latlng #(laitude,longitude)
        self.lat= g[0] 
        self.lon= g[1]
        return super(Tutor, self).save(*args,**kwargs)

    def __str__(self):
        return self.user.username
    
    def average_review(self):
        reviews = ReviewAndComment.objects.filter(tutor=self,status='New').aggregate(average=Avg('rate'))
        avg=0
        if reviews['average'] is not None:
            avg =math.floor(float(reviews['average']))
            print(avg)
            return avg
        else:
            return avg
    def total_review(self):
        reviews = ReviewAndComment.objects.filter(tutor=self,status='New').aggregate(count=Count('id'))
        count=0
        if reviews['count'] is not None:
            count = math.floor(float(reviews['count']))
            return count
        else:
            return count
    

class ReviewAndComment(models.Model):

    status=(
        ('New','New'),
        ('True','True'),
        ('False','False'),
    )
    tutor= models.ForeignKey(Tutor,on_delete=models.CASCADE)
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    comment=models.CharField(max_length=500, blank=True,null=True)
    rate= models.IntegerField(default=1)
    ip=models.CharField(max_length=100,blank=True)
    status=models.CharField(max_length=40,choices=status,default='New')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


