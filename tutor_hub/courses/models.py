from django.db import models
from django.template.defaultfilters import slugify
from home.models import Tutor,Student
from django.db.models.signals import pre_save
from courses.utils import unique_course_code_generator,unique_slug_generator,unique_lecture_id_generator
from django.urls import reverse
import os


def save_class_image(instance,filename):
    '''
    This will save class image for a specific class when, class image is uploaded by the creator of the class

    :param instance: Takes instances of a Class object as argument to save class image
    :type request: Class
    :param filename: takes the file name of the uploaded image for class
    :type filename: string
    :return: returns a path of uploaded folder and modified filename
    :rtype: path, string

    '''
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    #get filename
    if instance.title:
        filename = 'Class_Pictures/{}.{}'.format(instance.title,ext)
    return os.path.join(upload_to, filename)

class Class(models.Model):
    """
    This is a conceptual Database representation of Class table for all the courses that to be used in the project.
    
    :param models.Model: It inherits built-in functionalities of django `models.Model`, which handels all validations in django Admin panel
    :type ModelForm: model.Model

    """
    title = models.CharField(max_length=100, null=True, blank=True)
    class_code = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(max_length=550,null=True,blank=True)
    image = models.ImageField(upload_to = save_class_image,blank=True,verbose_name ='class image')
    tutor = models.ForeignKey(Tutor, null=True, blank=True, on_delete=models.CASCADE,related_name='tutors')
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.title

def course_code_generator(sender,instance,*args,**kwargs):
    if not instance.class_code:
        instance.class_code = unique_course_code_generator(instance)

pre_save.connect(course_code_generator,sender = Class)

def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator,sender = Class)


def save_lecture_files(instance,filename):
    '''
    This will save lecture files for a specific class when, class lectures are uploaded by the creator of the class

    :param instance: Takes instances of a lecture object as argument to save lecture files
    :type request: Lecture
    :param filename: takes the file name of the uploaded files for lecture
    :type filename: string
    :return: returns a path of uploaded folder and modified filename
    :rtype: path, string

    '''
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    #get filename
    if instance.lecture_id:
        filename = 'lecture_files/{}/{}/{}.{}'.format(instance.class_content.slug,instance.position,instance.position,ext)
        if os.path.exists(filename):
            new_name = str(instance.position) + str('1')
            filename = 'lecture_files/{}/{}/{}.{}'.format(instance.class_content.slug,instance.position, new_name,ext)
    return os.path.join(upload_to, filename)

class Lecture(models.Model):
    """
    This is a conceptual Database representation of `Lectur` table for all the courses taht to be used in the project.
    
    :param models.Model: It inherits built-in functionalities of django `models.Model`, which handels all validations in django Admin panel
    :type ModelForm: model.Model

    """
    lecture_id = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=150)
    class_content= models.ForeignKey(Class, on_delete=models.CASCADE, related_name='lessons')
    description = models.TextField(max_length=550,null=True,blank=True)
    created_by = models.ForeignKey(Tutor,on_delete=models.CASCADE, related_name="teachers")
    created_at = models.DateTimeField(auto_now_add=True)
    position = models.PositiveSmallIntegerField(verbose_name= 'Lecture No')
    slug = models.SlugField(null=True,blank=True)
    video = models.FileField(upload_to=save_lecture_files,verbose_name='video',blank=True,null=True)
    ppt = models.FileField(upload_to=save_lecture_files,verbose_name='ppt',blank=True)
    notes = models.FileField(upload_to=save_lecture_files,verbose_name='notes',blank=True)

    class Meta:
        
        ordering = ['position']
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("tutor_lecture_list_view", kwargs={ 'slug':self.class_content.slug})

def lecture_id_generator(sender,instance,*args,**kwargs):
    if not instance.lecture_id:
        instance.lecture_id = unique_lecture_id_generator(instance)

pre_save.connect(lecture_id_generator,sender = Lecture)