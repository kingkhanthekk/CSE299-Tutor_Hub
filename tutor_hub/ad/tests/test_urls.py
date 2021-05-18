'''
This program will use unittest to test ad app's urls.py
'''

from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ad.views import student_ad, tutor_ad, home

class TestUrls(SimpleTestCase):
    '''
    This is a conceptual Unittest child case for testing urls.py. 
    :param SimpleTestCase: It inherits built-in child functionalities of django `unittest`, which handels all test cases.
    :type SimpleTestCase: functions
    '''
    def test_find_tutor_url_is_resolved(self):
        '''
        This will test the find_tutor url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('find_tutor')
        self.assertEqual(resolve(url).func, student_ad)
        
    def test_find_student_url_is_resolved(self):
        '''
        This will test the find_tutor url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('find_student')
        self.assertEqual(resolve(url).func, tutor_ad)
        
    def test_home_url_is_resolved(self):
        '''
        This will test the home url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)
    