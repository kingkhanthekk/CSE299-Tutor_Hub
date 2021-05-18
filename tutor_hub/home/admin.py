'''
This program will display models in the Django Admin panel.
'''

from django.contrib import admin
from .models import User, Student, Tutor


admin.site.register(Student)
admin.site.register(Tutor)