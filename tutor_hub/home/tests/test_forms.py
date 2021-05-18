from django.contrib.auth.models import User
from django.test import TestCase
from home.forms import EditForm_Tutor, EditForm_Student

class TestForms(TestCase):
    def test_EditForm_Tutor_valid_data(self):
        tu1 = User.objects.create_user(username="David", email="david_malan@gmail.com", password="12254")
        form = EditForm_Tutor(data={
            'user': tu1, 
            'institutiom':'Harvard',
            'area': 'USA', 
            'subject': 'CSE', 
            'salary': '60000',
            'gender': 'Male',
        })
        self.assertTrue(form.is_valid())
    
    def test_EditForm_Student_valid_data(self):
        stu1 = User.objects.create_user(username="Bill", email="bill_101n@gmail.com", password="12254")
        form = EditForm_Tutor(data={
            'user': stu1, 
            'institutiom':'Harvard',
            'area': 'USA', 
            'address': '24 New York',
            'gender': 'Male',
        })
        self.assertTrue(form.is_valid())