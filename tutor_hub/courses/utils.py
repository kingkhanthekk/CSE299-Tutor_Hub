import string
import random
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """
    This is for a Django project and it is used to create a random string of 10 character

    :param size: Takes a integer of value 10
    :type size: int
    :param chars: Takes ascii lowercase and digits and concate them as strings
    :return: it returns a random string of 10 character
    "rtype: string

    """
    return ''.join(random.choice(chars) for _ in range(size))


def unique_course_code_generator(instance):
    """
    This is for a Django project and it assumes your instance 
    has a model with a class_code field.

    :param instance: Takes a instance of a `Class` model's object
    :type instance: instance
    :return: it returns a random string of 10 character
    "rtype: string

    """
    new_class_code = random_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(class_code=new_class_code).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return new_class_code
