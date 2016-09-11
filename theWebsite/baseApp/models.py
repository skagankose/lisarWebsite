from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class SchoolType(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class HighSchool(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    schoolType = models.ForeignKey(SchoolType,\
        related_name="highSchools", blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.schoolType.title


class Teacher(models.Model):
    firstName = models.CharField(max_length=300, blank=True, null=True)
    lastName = models.CharField(max_length=300, blank=True, null=True)
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{12}$',\
        message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.")
    phoneNumber = models.CharField(validators=[phoneRegex], blank=True, max_length=13)
    mailAddress = models.EmailField(blank=True, null=True)
    university = models.CharField(max_length=300, blank=True, null=True)
    department = models.CharField(max_length=300, blank=True, null=True)
    degree = models.CharField(max_length=30,choices = (('lisans', 'Lisans'), ('yüksek lisans', 'Yüksek Lisans'),
        ('doktora', 'Doktora')), blank=True, null=True)
    ibanNo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.firstName + " " + self.lastName



class Classroom(models.Model):
    code = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    #courses = models.ManyToManyField(Course, blank=True, related_name="classroom")

    def __str__(self):
        return self.code

class Course(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    classroom = models.ForeignKey(Classroom, blank=True, null=True, related_name='course')
    teacher = models.ForeignKey(Teacher, blank=True, null=True, related_name='course')
    start = models.TimeField(default=timezone.now)
    end = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.name + self.classroom.code


class CourseDate(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.course.name + " " + str(self.date)


class BookPayment(models.Model):
    Months = (('eylül','Eylül'), ('ekim','Ekim'), ('kasım','Kasım'),
              ('aralık','Aralık'), ('ocak','Ocak'), ('şubat','Şubat'),
              ('mart','Mart'), ('nisan','Nisan'), ('mayıs','Mayıs'),
              ('haziran','Haziran'), ('temmuz','Temmuz'), ('ağustos','Ağustos'))
    month = models.CharField(max_length=100,choices = Months, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.month + ' ' + str(self.year)+ ' ' + str(self.cost)


class LisarSemester(models.Model):
    semester = models.CharField(max_length=300, blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.semester


class SchoolSemester(models.Model):  # soru: gerek varmı ayrı bi class a
    semester = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.semester


class Student(models.Model):
    # Personal info
    firstName = models.CharField(max_length=300)
    lastName = models.CharField(max_length=300)
    dateOfBirth = models.DateField(max_length=8, default=timezone.now)
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{12}$',\
        message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.")
    phoneNumber = models.CharField(validators=[phoneRegex], blank=True, max_length=13)
    mailAddress = models.EmailField()
    adress = models.CharField(max_length=500, blank=True, null=True)
    place = models.CharField(max_length = 10, choices = (('ev', 'Ev'), ('yurt', 'Yurt')),
        blank=True, null=True)
    reference = models.CharField(max_length=500, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    # School info
    highSchool = models.ForeignKey(HighSchool,
        related_name="students", blank=True, null=True)
    schoolSemester = models.ForeignKey(SchoolSemester,
        related_name="students", blank=True, null=True)
    teogScore = models.FloatField(blank=True, null=True)

    # Lisar info
    lisarSemester = models.ForeignKey(LisarSemester, blank=True, null=True,
        related_name="students")
    classroom = models.ForeignKey(Classroom,
        related_name="students", blank=True, null=True)

    def __str__(self):
        return self.firstName + " " + self.lastName


class StudentPayment(models.Model): # otomatik olması gerek
    student = models.ForeignKey(Student, blank=True, null=True)
    payment = models.ForeignKey(BookPayment, blank=True, null=True)
    isPaid = models.BooleanField(default=False)

    def __str__(self):
        if self.isPaid == True:
            return  "%s %s - %s PAID" %(self.student.firstName,self.student.lastName,self.payment.month)
        else:
            return "%s %s - %s notPAID" %(self.student.firstName,self.student.lastName,self.payment.month)


class Attendance(models.Model):
    student = models.ForeignKey(Student, blank=True, null=True,
        related_name="attendance")
    courseDate = models.ForeignKey(CourseDate, blank=True, null=True,
        related_name="attendance")
    isHere = models.BooleanField()

    def __str__(self):
        if self.isHere == True:
            return self.student.firstName + " HERE"
        else:
            return self.student.firstName + " ABSENT"


class CourseGrade(models.Model):
    student = models.ForeignKey(Student, blank=True, null=True)
    course = models.ForeignKey(Course, blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.grade)


class Income(models.Model):
    date = models.DateField(max_length=8, default=timezone.now)
    amount = models.FloatField()

    def __str__(self):
        return self.amount + " TL"


class Outcome(models.Model):
    date = models.DateField(max_length=8, default=timezone.now)
    amount = models.FloatField()

    def __str__(self):
        return self.amount + " TL"


class Budget(models.Model):
    totalAmount = models.FloatField() # soru: otomatik hesaplanması gerek

    def __str__(self):
        return self.totalAmount + " TL"
