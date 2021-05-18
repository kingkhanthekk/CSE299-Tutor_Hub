'''
This program will be used to unittest test courses app's urls.py
'''
from django.test import SimpleTestCase
from django.urls import resolve,reverse
from courses.views import (tutor_dashboard,student_dashboard,tutor_lecture_detail_View,
tutor_lecture_list_View,student_lecture_detail_View,student_lecture_list_View,
LectureDeleteView,LectureUpdateView,enrolled_students,create_lecture_view,create_class,
join_class)
class TestUrls(SimpleTestCase):
    '''
    This is a conceptual Unittest child case for testing urls.py. 
    :param SimpleTestCase: It inherits built-in child functionalities of django `unittest`, which handels all test cases.
    :type SimpleTestCase: functions
    '''
    def test_create_class_url_is_resolves(self):
        '''
        This will test the create_class url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('create_class')
        print(resolve(url))
        self.assertEquals(resolve(url).func,create_class)
    
    def test_join_class_url_is_resolves(self):
        '''
        This will test the join_class url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('join_class')
        print(resolve(url))
        self.assertEquals(resolve(url).func,join_class)
    
    def test_student_dashboard_url_is_resolves(self):
        '''
        This will test the student_dashboard url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('student_dashboard')
        print(resolve(url))
        self.assertEquals(resolve(url).func,student_dashboard)
    
    def test_tutor_dashboard_url_is_resolves(self):
        '''
        This will test the tutor_dashboard url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('tutor_dashboard')
        print(resolve(url))
        self.assertEquals(resolve(url).func,tutor_dashboard)
    
    def test_student_lecture_list_view_url_is_resolves(self):
        '''
        This will test the student_lecture_list url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('student_lecture_list_view',args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,student_lecture_list_View)
    
    def test_tutor_lecture_list_view_url_is_resolves(self):
        '''
        This will test the tutor_lecture_list url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('tutor_lecture_list_view',args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,tutor_lecture_list_View)
    
    def test_create_lecture_url_is_resolves(self):
        '''
        This will test the create_lecture url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('create_lecture',args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,create_lecture_view)

    def test_enrolled_students_url_is_resolves(self):
        '''
        This will test the enrolled_students url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('enrolled_students',args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,enrolled_students)
    
    def test_student_lecture_details_url_is_resolves(self):
        '''
        This will test the student_lecture_details url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('student_lecture_details',args=['some-string','some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,student_lecture_detail_View)

    def test_tutor_lecture_details_url_is_resolves(self):
        '''
        This will test the tutor_lecture_details url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('tutor_lecture_details',args=['some-string','some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,tutor_lecture_detail_View)
    
    def test_tutor_lecture_update_url_is_resolves(self):
        '''
        This will test the lecture_update url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('tutor_lecture_update',args=['some-string','some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,LectureUpdateView)
    
    def test_tutor_lecture_delete_url_is_resolves(self):
        '''
        This will test the delete_lecture url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('tutor_lecture_delete',args=['some-string','some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,LectureDeleteView)