'''
This program will be used to unittest test courses app's models.py
'''
from django.test import TestCase
from django.urls import reverse
from courses.models import Lecture,Class
from home.models import Tutor,Student,User
from django.contrib.auth.models import Group
from unittest import mock
from django.core.files import File
from unittest.mock import MagicMock
class TestModels(TestCase):
    '''
        This is a conceptual Unittest child case for testing forms.py. 
        :param TestCase: It inherits built-in child functionalities of django `unittest`, which handels all test cases.
        :type SimpleTestCase: functions
    '''
    def setUp(self):
        '''
        This will be used to initialize to create object of models for testing purpose
        and this will be intialize before tetsting starts .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a nothing. 
        :rtype: none.
        '''
        #create permissions group
        group_name1 = "student"
        group_name2 = "tutor"
        self.group1 = Group(name=group_name1)
        self.group1.save()
        self.group2 = Group(name=group_name2)
        self.group2.save()

        self.user1 = User.objects.create(
            username='user1',
            first_name='Mr',
            last_name='user1',
            email='user1@gmail.com',
            password = 'Noman321'
        )
        self.user1.groups.add(self.group1)
        self.user1.save()


        self.user2 = User.objects.create(
            username='user2',
            first_name='Mr',
            last_name='user',
            email='user2@gmail.com',
            password = 'Noman321'
        )
        self.user2.groups.add(self.group2)
        self.user2.save()

        self.student1 = Student.objects.create(
            user=self.user1,
        )
        
        self.tutor1 = Tutor.objects.create(
            user=self.user2,
        )
        

        self.class1 = Class.objects.create(
            title ='class1',
            description ='description',
            tutor = self.tutor1,
        )
        self.class1.students.add(self.student1)
        self.class1.save()

        self.lecture1 = Lecture.objects.create(
            name ='lecture1',
            class_content=self.class1,
            description ='description',
            created_by =self.tutor1,
            position = 2
        )
        self.lecture1.save()

    def test_class_slug_on_creation(self):
        '''
        This will test the class_slug function to initialize sulg_field .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the forms field. 
        :rtype: assertEqual , bool
        '''
        self.assertEquals(self.class1.slug, 'class1')
    
    def test_class_image_files(self):
        '''
        This will test the class_image_file function to store class image .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the forms field. 
        :rtype: assertEqual , bool
        '''
        file_mock = mock.MagicMock(spec=File, name='FileMock')
        self.class1.image=file_mock
        self.assertEqual(Class.objects.count(), 1)  
    
    def test_lecture_slug_on_creation(self):
        '''
        This will test the lecture_slug function to initialize sulg_field .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the forms field. 
        :rtype: assertEqual , bool
        '''
        self.assertEquals(self.lecture1.slug, 'lecture1')

    def test_lecture_files(self):
        '''
        This will test the lecture_files function to store lecture files .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the forms field. 
        :rtype: assertEqual , bool
        '''
        file_mock = mock.MagicMock(spec=File, name='FileMock')
        self.lecture1.video=file_mock
        self.assertEqual(Lecture.objects.count(), 1) 

        