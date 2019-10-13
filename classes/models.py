from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, null = True, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})


	def __str__(self):
		return self.name



class Student(models.Model):

	

	Gender_CHOICES = (
	('UNDEFINED', 'Undefined'),
    ('FEMALE', 'Female'),
    ('MALE', 'Male'),
	)

	Grade_CHOICES = (
	('-', 'NoGrade'),
    ('A', 'A'),
    ('A-', 'A-'),	
    ('B+', 'B+'),
    ('B', 'B'),
    ('B-', 'B-'),	
    ('C+', 'C+'),
    ('C', 'C'),
    ('C-', 'C-'),	
    ('D+', 'D+'),
    ('D', 'D'),
    ('F', 'F'),
    ('FA', 'FA'),

	)

	name = models.CharField(max_length=120)
	date_of_birth = models.DateField(null=True, blank=True)
	gender = models.CharField(max_length=10, choices=Gender_CHOICES, default='UNDEFINED')
	exam_grade = models.CharField(max_length=2, choices=Grade_CHOICES, default='-')
	classroom = models.ForeignKey(Classroom, null = True, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

	def __str__(self):
		return self.name

	