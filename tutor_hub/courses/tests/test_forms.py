'''
This program will be used to unittest test courses app's forms.py
'''
from django.test import SimpleTestCase
from courses.forms import CreateClassForm,CreateLectureForm
from unittest import mock
from django.core.files import File
from unittest.mock import MagicMock
class TestForms(SimpleTestCase):
    '''
    This is a conceptual Unittest child case for testing forms.py. 
    :param SimpleTestCase: It inherits built-in child functionalities of django `unittest`, which handels all test cases.
    :type SimpleTestCase: functions
    '''
    def test_create_class_form_with_valid_data(self):
        '''
        This will test the CreateClass form with valid input .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the forms field. 
        :rtype: assertEqual , bool
        '''
        form =CreateClassForm(data={
            'title':'class1',
            'description':'description'
        })
        self.assertTrue(form.is_valid())
    def test_create_class_form_with_no_data(self):
        '''
        This will test the CreateClass form with invalidvalid input .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the forms field. 
        :rtype: assertEqual , bool
        '''
        form =CreateClassForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
    
    def test_create_lecture_form_with_valid_data(self):
        '''
        This will test the CreteLecture form with valid input .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the forms field. 
        :rtype: assertEqual , bool
        '''
        file_mock = mock.MagicMock(spec=File, name='FileMock')
        form =CreateLectureForm(data={
            'name':'Lecture1',
            'position':1,
            'description':'description',
            'video': file_mock,
            'ppt':file_mock,
            'notes':file_mock
        })
        self.assertTrue(form.is_valid())
    
    def test_create_lecture_form_with_no_data(self):
        '''
        This will test the CreateClass form with invalidvalid input .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the forms field. 
        :rtype: assertEqual , bool
        '''
        form =CreateClassForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
      
