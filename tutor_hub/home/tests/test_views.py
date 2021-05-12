from django.test import TestCase, Client
from django.urls import reverse
from home.models import Student, Tutor

class TestViews(TestCase):
    '''
    This is a conceptual Unittest child case class for testing views.py. 
    
    :param TestCase: It inherits built-in child functionalities of django `unittest`, which handels all test cases.
    :type TestCase: functions
    '''
    def test_profile_GET(self):
        '''
        This will test the find_tutor view with proper request .
        
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual, resolve url, bool
        '''
        client = Client()
        response = self.client.get('/edit_profile_tutor/')
        self.assertEquals(response.status_code ,302)
        self.assertTemplateUsed(response, 'profile/profile.html')
    
    def test_edit_profile_tutor_GET(self):
        '''
        This will test the find_tutor view with proper request .
        
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual, resolve url, bool
        '''
        client = Client()
        response = self.client.get('/edit_profile_tutor/')
        self.assertEquals(response.status_code ,302)
        self.assertTemplateUsed(response, 'profile/edit_profile_tutor.html')

    
    def test_edit_profile_student_GET(self):
        '''
        This will test the find_tutor view with proper request .
        
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual, resolve url, bool
        '''
        client = Client()
        response = self.client.get('/edit_profile_student/')
        self.assertEquals(response.status_code ,302)
        self.assertTemplateUsed(response, 'profile/edit_profile_student.html')
    

