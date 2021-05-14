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
