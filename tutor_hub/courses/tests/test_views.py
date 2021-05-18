'''
This program will be used to unittest test courses app's views.py
'''
from django.test import TestCase,Client
from django.urls import reverse
from courses.models import Lecture,Class
from home.models import Tutor,Student,User
from django.contrib.auth.models import Group
import json

class TestViews(TestCase):
    '''
    This is a conceptual Unittest child case for testing forms.py. 
    :param TestCase: It inherits built-in child functionalities of django `unittest`, which handels all test cases.
    :type TestCase: functions
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
        self.client = Client()
        self.create_class_url = reverse('create_class')
        self.join_class_url = reverse('join_class')
        self.tutor_dashboard_url = reverse('tutor_dashboard')
        self.student_dashboard_url = reverse('student_dashboard')
        self.student_lecture_list_view_url = reverse('student_lecture_list_view',args=['class1'])
        self.tutor_lecture_list_view_url = reverse('tutor_lecture_list_view',args=['class1'])
        self.create_lecture_view_url = reverse('create_lecture',args=['class1'])
        self.enrolled_students_url = reverse('enrolled_students',args=['class1'])
        self.tutor_lecture_detail_View_url = reverse('tutor_lecture_details',args=['class1','lecture1'])
        self.student_lecture_detail_View_url = reverse('student_lecture_details',args=['class1','lecture1'])
        
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
            slug="class1",
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

    def test_create_class_GET(self):
        '''
        This will test the Create_classs view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual ,resolve url, bool
        '''
        response =self.client.get(self.create_class_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'courses/create_class.html')
    
    def test_join_class_GET(self):
        '''
        This will test the join_classs view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual ,resolve url, bool
        '''
        
        response =self.client.get(self.join_class_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'courses/join_class.html')
    
    def test_tutor_dashboard_GET(self):
        '''
        This will test the tutor_dashboard view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual ,resolve url, bool
        '''
        self.user3 = User.objects.create(
            username='user3',
            first_name='Mr',
            last_name='user3',
            email='user3@gmail.com',
            password = 'Noman321'
        )
        self.user3.groups.add(self.group2)
        self.user3.save()
        self.tutor2 = Tutor.objects.create(
            user=self.user3,
        )
        self.tutor2.save()

        login = self.client.force_login(self.user3)
    
        response =self.client.get(self.tutor_dashboard_url)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'courses/tutor_dashboard.html')
    
    def test_student_dashboard_GET(self):
        '''
        This will test the student_dashboard view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual ,resolve url, bool
        '''
        self.user4 = User.objects.create(
            username='user4',
            first_name='Mr',
            last_name='user4',
            email='user4@gmail.com',
            password = 'Noman321'
        )
        self.user4.groups.add(self.group1)
        self.user4.save()
        self.student2 = Student.objects.create(
            user=self.user4,
        )
        self.student2.save()

        login = self.client.force_login(self.user4)
    
        response =self.client.get(self.student_dashboard_url)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'courses/student_dashboard.html')
    

    def test_student_lecture_list_view_GET(self):
        '''
        This will test the student_lecture_list view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual ,resolve url, bool
        '''
        response =self.client.get(self.student_lecture_list_view_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'courses/student_lecture_list_view.html')
    
    def test_tutor_lecture_list_view_GET(self):
        '''
        This will test the tutor_lecture_list view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual ,resolve url, bool
        '''
        response =self.client.get(self.tutor_lecture_list_view_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'courses/tutor_lecture_list_view.html')
    
    def test_create_lecture_view_GET(self):
        '''
        This will test the create_lecture view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual ,resolve url, bool
        '''
        response =self.client.get(self.create_lecture_view_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'courses/create_lecture.html')
    
    def test_enrolled_students_GET(self):
        '''
        This will test the enrolled_student view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual ,resolve url, bool
        '''
        response =self.client.get(self.enrolled_students_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'courses/enrolled_students.html')

    def test_tutor_lecture_detail_view_GET(self):
        '''
        This will test the tutor_lecture_detail view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual ,resolve url, bool
        '''
        response =self.client.get(self.tutor_lecture_detail_View_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'courses/tutor_lecture_detail_view.html')
    
    def test_student_lecture_detail_view_GET(self):
        '''
        This will test the atudent_lecture_detail view with proper request .
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the template via view. 
        :rtype: assertEqual ,resolve url, bool
        '''
        response =self.client.get(self.student_lecture_detail_View_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'courses/student_lecture_detail_view.html')
    
