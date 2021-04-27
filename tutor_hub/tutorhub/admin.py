'''
This program is used to view the database from admin panel. 
Administrator can modify & see the database from that panel.
'''
from django.contrib import admin
from .models import Ad_Student


admin.site.register(Ad_Student)
