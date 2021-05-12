from django import template
from django.contrib.auth.models import Group
from home.models import Student, Tutor

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group):
    return user.groups.filter(name=group).exists()
