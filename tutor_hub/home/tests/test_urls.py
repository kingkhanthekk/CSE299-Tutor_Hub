from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import profile, edit_profile_tutor, edit_profile_student, delete_profile

class TestUrls(SimpleTestCase):
    def test_profile_url_is_resolved(self):
        url= reverse('profile')
        self.assertEqual(resolve(url).func, profile)


    def test_edit_profile_tutor_url_is_resolved(self):
        url= reverse('edit_profile_tutor')
        self.assertEqual(resolve(url).func, edit_profile_tutor)


    def test_edit_profile_student_url_is_resolved(self):
        url= reverse('edit_profile_student')
        self.assertEqual(resolve(url).func, edit_profile_student)


    def test_delete_profile_url_is_resolved(self):
        url= reverse('delete_profile')
        self.assertEqual(resolve(url).func, delete_profile)