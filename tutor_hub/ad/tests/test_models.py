'''
This program will use unittest to test ad app's models.py
'''
from django.test import TestCase
from ad.models import AdStudent, AdTutor
from django.contrib.auth.models import User

class TestModels(TestCase):
    '''
    This is a conceptual Unittest child case class for testing models.py. 
    :param TestCase: It inherits built-in child functionalities of django `unittest`, which handels all test cases.
    :type SimpleTestCase: functions
    '''
    def setUp(self):
        '''
        This will create some objects of student ad model and tutor ad model.
        :param self: Takes the self content and pass. 
        :type self: object
        :return: returns object to check models are working properly. 
        :rtype: object
        '''
        user1 = User.objects.create_user(username="user1", email="email1@mail.com", password="Pass12345")
        user2 = User.objects.create_user(username="user2", email="email2@mail.com", password="Pass@12345")
        AdStudent.objects.create(
            user= user1, 
            title= 'Title', 
            area= 'Mirpur', 
            subject= 'CSE', 
            class_level= 'Bsc',
            days= 5,
            salary= '16000',
            gender= 'male',
            description= 'demo description' 
        )
        AdStudent.objects.create(
            user= user2, 
            title= 'Demo', 
            area= 'Uttara', 
            subject= 'BBA', 
            class_level= 'BS',
            days= 4,
            salary= '12000',
            gender= 'female',
            description= 'description'
        )
        AdTutor.objects.create(
            user= user1, 
            title= 'Title', 
            expected_area= 'Mirpur', 
            subject= 'CSE', 
            class_level= 'Bsc',
            days= 5,
            expected_salary= '16000',
            gender= 'male',
            description= 'demo description'
        )
        AdTutor.objects.create(
            user= user2, 
            title= 'Demo', 
            expected_area= 'Uttara', 
            subject= 'BBA', 
            class_level= 'BS',
            days= 4,
            expected_salary= '12000',
            gender= 'female',
            description= 'description'
        )
        
    def test_model_object_student(self):
        '''
        This will test all the objects of student ad model.
        :param self: Takes the self content and pass. 
        :type self: int
        :return: returns a request to check the title value. 
        :rtype: assertEqual , bool
        '''
        obj = AdStudent.objects.all()
        self.assertEqual(obj.count(),2)
        
    def test_model_string_student(self):
        '''
        This will test the __str__ function to store student ad title.
        :param self: Takes the self content and pass. 
        :type self: string
        :return: returns a request to check the title value. 
        :rtype: assertEqual , bool
        '''
        user3 = User.objects.create_user(username="user3", email="email3@mail.com", password="Pass12345")
        title = AdStudent(user=user3, title='Django Testing 1')
        title.save()
        self.assertEqual(str(title), 'Django Testing 1')
        
    def test_model_object_tutor(self):
        '''
        This will test all the objects of tutor ad model.
        :param self: Takes the self content and pass. 
        :type self: int
        :return: returns a request to check the title value. 
        :rtype: assertEqual , bool
        '''
        obj = AdTutor.objects.all()
        self.assertEqual(obj.count(),2)
        
    def test_model_string_tutor(self):
        '''
        This will test the __str__ function to store tutor ad title.
        :param self: Takes the self content and pass. 
        :type self: string
        :return: returns a request to check the title value. 
        :rtype: assertEqual , bool
        '''
        user4 = User.objects.create_user(username="user4", email="email4@mail.com", password="Pass12345")
        title = AdTutor(user=user4, title='Django Testing 2')
        title.save()
        self.assertEqual(str(title), 'Django Testing 2')
