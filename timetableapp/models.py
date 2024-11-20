from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ('', 'select'),
    ('male', 'Male'),
    ('female', 'Female'),
]

DEPARTMENT_CHOICES = [
    ('Cse-H', "CSE-H"),
    ('Cse', 'CSE'),
    ('Csit', 'CSIT'),
    ('Aids', 'AIDS'),
    ('Ece', 'ECE'),
    ('Eee', 'EEE'),
    ('BBA', 'BBA'),
    ('Mechanical', 'Mechanical'),
    ('Biotechnology', 'Biotechnology'),
    ('Civil', 'Civil'),
    ('Mba', 'MBA'),
    ('B.arch', 'B.Arch'),
]

BATCH_CHOICES = [
    ('', 'select batch'),
    ('2019-2023', 'Y19-batch'),
    ('2020-2024', 'Y20-batch'),
    ('2021-2025', 'Y21-batch'),
    ('2022-2026', 'Y22-batch'),
    ('2023-2027', 'Y23-batch'),
    # Add more choices here
]

SEMESTER_CHOICES = [
    ('', 'select'),
    ('odd', 'Odd'),
    ('even', 'Even'),
    ('summer', 'Summerterm'),
]

PRESENT_YEAR_CHOICES = [
    ('', 'select year'),
    ('1', '1st'),
    ('2', '2nd'),
    ('3', '3rd'),
    ('4', '4th'),
    # Add more choices here
]

DESIGNATION_CHOICES = [
    ('associate_professor', 'Associate Professor'),
    ('professor', 'Professor'),
    ('assistant_professor', 'Assistant Professor'),
    ('lecturer', 'Lecturer'),
]

QUALIFICATION_CHOICES = [
    ('M.Tech', 'M.TECH'),
    ('PhD', 'PhD'),
    ('Masters', "Master's"),
    ('Msc', 'M.Sc'),
    ('Bsc', 'B.Sc'),
    ('Bed', 'B.Ed'),
]


# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=10, default=None)
    course_title = models.CharField(max_length=100, default=None)
    batch = models.CharField(max_length=10, choices=BATCH_CHOICES, default=None)
    year = models.CharField(max_length=10, choices=PRESENT_YEAR_CHOICES, default=None)
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES, default=None)
    credits = models.DecimalField(max_digits=4, decimal_places=2, default=None)
    L = models.IntegerField(default=None)
    T = models.IntegerField(default=None)
    P = models.IntegerField(default=None)
    S = models.IntegerField(default=None)
    # Add other fields as needed

    def __str__(self):
        return self.course_code + "-" + self.course_title


class Faculty(models.Model):
    faculty_id = models.IntegerField(unique=True, default=None)
    name = models.CharField(max_length=100, default=None)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='prefer_not_to_say')
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default=None)
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES, default=None)
    qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES, default=None)
    contact = models.BigIntegerField(unique=True, default=None)
    email = models.EmailField(default=None)
    password = models.CharField(max_length=30,default='klu123')
    # Add other fields as needed


# def __str__(self):
#    return self.faculty_id+"-"+self.name


class Student(models.Model):
    student_id = models.IntegerField(unique=True, default=None)
    name = models.CharField(max_length=100, default=None)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='prefer_not_to_say')
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default=None)
    batch = models.CharField(max_length=10, choices=BATCH_CHOICES, default=None)
    present_year = models.CharField(max_length=10, choices=PRESENT_YEAR_CHOICES, default=None)
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES, default=None)
    contact = models.BigIntegerField(unique=True, default=None)
    password = models.CharField(max_length=30, default='klu123')
    # Add other fields as needed


# def __str__(self):
#    return self.student_id+"-"+self.name

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128, default='klu123')

    def __str__(self):
        return self.name
