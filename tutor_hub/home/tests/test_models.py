from django.test import TestCase
from home.models import Student, Tutor

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            institution=VNS,
            department =Science,
            phone = 12345,
            class_level= 5,
            address = Dhaka,
            area = Bashundhara,
            city = Dhaka,
            gender= Female,
        )
        Student.objects.create(
        institution=NSU,
        department =CSE,
        phone = 54214,
        address = Dhaka,
        area = Uttara,
        city = Dhaka,
        gender= Female,
        )
        def test_student_info(self):
            qs = Student.objects.all()
            self.assertEqual(qs.count(),2)
            s1 = Student.objects.get(institute ='VNS')
            s1 = Student.objects.get(institute ='NSU')
            self.assertEqual(s1.get_phone(),12345)
            self.assertEqual(s2.get_phone(),54214)

class TutorTestCase(TestCase):
    def setUp(self):
        Tutor.objects.create(
            institution= Harvard,
            department = Law,
            phone = 455567,
            address = USA,
            area = USA,
            city = USA,
            gender= Male,
            total_teach_exp = 10,
        )
        Tutor.objects.create(
        institution= NSU,
        department =EEE,
        phone = 54214445,
        address = Dhaka,
        area = Badda,
        city = Dhaka,
        gender= Male,
        total_teach_exp = 9,
        )
        def test_tutor_info(self):
            ab = Tutor.objects.all()
            self.assertEqual(ab.count(),2)
            t1 = Tutor.objects.get(institute ='Harvard')
            t2 = Tutor.objects.get(institute ='NSU')
            self.assertEqual(t1.get_phone(),455567)
            self.assertEqual(t2.get_phone(),54214445)

