from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class SchoolType(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class HighSchool(models.Model):
    name = models.CharField(max_length=500)
    schoolType = models.ForeignKey(SchoolType,\
        related_name="highSchools", blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.schoolType.title

class Student(models.Model):

    firstName = models.CharField(max_length=300)
    lastName = models.CharField(max_length=300)
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{12}$',\
        message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.")
    phoneNumber = models.CharField(validators=[phoneRegex], blank=True, max_length=13)
    mailAddress = models.EmailField()
    highSchool = models.ForeignKey(HighSchool,
        related_name="students", blank=True, null=True)
    dateOfBirth = models.DateField(max_length=8, default=timezone.now)

    def __str__(self):
        return self.firstName + " " + self.lastName


'''
class Teacher(models.Model):
    firstName
    lastName
    course(s)

class Classroom(models.Model):
    course(s)

class Course(models.Model):
    student(s)
    teaacher(s)

class CourseGrade(models.Model):
    course
    student
    grade

class CourseDate(models.Model):
    course
    date

class Attendance(models.Model):
    student
    courseDate
    isHere

class SchoolSemester(models.Model):
    student(s)

class LisarSemester(models.Model):
    student(s)

class BookPayment(models.Moodel):
    lisarSemester
    student
    payment

class Income(models.Model):
    amount
    date

class Outcome(models.Model):
    amount
    date

class Budget(models.Model):
    totalAmount
'''
