'''
This program will create database file for Advertise feature.
'''
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse     

class AdStudent(models.Model):
    '''
    This is a conceptual Database representation of Class table for student ads.
    
    :param models.Model: It inherits built-in functionalities of django `models.Model`, which handels all validations in django Admin panel.
    :type models.Model: database model
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    area = models.CharField(max_length=150, null=True, blank=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    class_level = models.CharField(max_length=150, null=True, blank=True)
    days = models.DecimalField(decimal_places=0, max_digits=2, default=2)
    salary = models.CharField(max_length=10,default=3000)
    male ='male'
    female = 'female'
    other = 'other'
    genders = [
        (male,'male'),
        (female,'female'),
        (other,'other'),
    ]
    gender = models.CharField(max_length=15, choices=genders,default=male,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    request_confirmation = models.BooleanField(default=False)
    ad_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        '''
        This will show the title of students's ad in the admin panel.
        
        :param self: Takes the self's variable name. 
        :type self: string
        :return: returns a reference to the instance object on which it was called.
        :rtype: model variable name
        '''
        return self.title

class AdTutor(models.Model):
    '''
    This is a conceptual Database representation of Class table for tutor ads.
    
    :param models.Model: It inherits built-in functionalities of django `models.Model`, which handels all validations in django Admin panel.
    :type models.Model: database model
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    expected_area = models.CharField(max_length=150, null=True, blank=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    class_level = models.CharField(max_length=150, null=True, blank=True)
    days = models.DecimalField(decimal_places=0, max_digits=7, default=2)
    expected_salary = models.CharField(max_length=10,default=3000)
    male ='male'
    female = 'female'
    other = 'other'
    genders = [
        (male,'male'),
        (female,'female'),
        (other,'other'),
    ]
    gender = models.CharField(max_length=15, choices=genders,default=male,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    request_confirmation = models.BooleanField(default=False)
    ad_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        '''
        This will show the title of tutor's ad in the admin panel.
        
        :param self: Takes the self's variable name. 
        :type self: string
        :return: returns a reference to the instance object on which it was called.
        :rtype: self .model variable name
        '''
        return self.title
    
    
    
