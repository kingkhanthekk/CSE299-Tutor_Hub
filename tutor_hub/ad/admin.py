'''
This program will create visual database pages in Admin panel.
'''
from django.contrib import admin
from .models import AdTutor, AdStudent

admin.site.register(AdStudent)
admin.site.register(AdTutor)