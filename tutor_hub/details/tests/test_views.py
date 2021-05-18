'''
This program will use unittest to test ad app's views.py
'''

from django.test import TestCase, Client
from django.urls import reverse
from details.views import view_more


class TestViews(TestCase):
    '''
    This is a conceptual Unittest child case class for testing views.py. 
    :param TestCase: It inherits built-in child functionalities of django `unittest`, which handels all test cases.
    :type TestCase: functions
    '''

    def test_view_more_get(self):
        '''
        This will test the view_more view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual, resolve url, bool
        '''
        response = self.client.get('/view_more/')
        self.assertEquals(response.status_code, 404)
