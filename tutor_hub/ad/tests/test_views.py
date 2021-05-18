'''
This program will use unittest to test ad app's views.py
'''

from django.test import TestCase, Client
from django.urls import reverse
from ad.views import *

class TestViews(TestCase):
    '''
    This is a conceptual Unittest child case class for testing views.py. 
    :param TestCase: It inherits built-in child functionalities of django `unittest`, which handels all test cases.
    :type TestCase: functions
    '''
    def test_find_tutor_get(self):
        '''
        This will test the find_tutor view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual, resolve url, bool
        '''
        response = self.client.get('/find_tutor/')
        self.assertEquals(response.status_code, 200)
    
    def test_find_student_get(self):
        '''
        This will test the find_student view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual, resolve url, bool
        '''
        response = self.client.get('/find_student/')
        self.assertEquals(response.status_code, 200)
        
    def test_home_get(self):
        '''
        This will test the home view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual, resolve url, bool
        '''
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)
        