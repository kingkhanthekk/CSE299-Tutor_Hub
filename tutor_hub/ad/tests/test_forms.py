'''
This program will use unittest to test ad app's forms.py.
'''
from django.contrib.auth.models import User
from django.test import TestCase
from ad.forms import AdStudentForm, AdTutorForm

class TestForms(TestCase):
    '''
    This is a conceptual Unittest child case class for testing forms.py. 
    :param SimpleTestCase: It inherits built-in child functionalities of django `unittest`, which handels all test cases.
    :type SimpleTestCase: functions
    '''
    def test_AdStudentForm_valid_data(self):
        '''
        This will test the AdStudentForm form with valid input.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the forms field. 
        :rtype: assertEqual , bool
        '''
        user1 = User.objects.create_user(username="name", email="email@mail.com", password="Pass12345")
        form = AdStudentForm(data={
            'user': user1, 
            'title': 'Title', 
            'area': 'Mirpur', 
            'subject': 'CSE', 
            'class_level': 'Bsc',
            'days': 5,
            'salary': '6000',
            'gender': 'male',
            'description': 'demo description'
        })
        self.assertTrue(form.is_valid())
        
    def test_AdStudentForm_no_data(self):
        '''
        This will test the AdStudentForm form with invalid/blank input.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the forms field. 
        :rtype: assertEqual , bool
        '''
        form = AdStudentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
    
    
    def test_AdTutorForm_valid_data(self):
        '''
        This will test the AdTutorForm form with valid input.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the forms field. 
        :rtype: assertEqual , bool
        '''
        user2 = User.objects.create_user(username="name", email="email@mail.com", password="Pass12345")
        form = AdTutorForm(data={
            'user': user2, 
            'title': 'Title', 
            'expected_area': 'Mirpur', 
            'subject': 'CSE', 
            'class_level': 'BSC',
            'days': 5,
            'expected_salary': '6000',
            'gender': 'male',
            'description': 'demo description'
        })
        self.assertTrue(form.is_valid())
        
    def test_AdTutorForm_no_data(self):
        '''
        This will test the AdTutorForm form with invalid/blank input.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the forms field. 
        :rtype: assertEqual , bool
        '''
        form = AdTutorForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
    