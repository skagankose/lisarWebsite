from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone



class HighSchool(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    schoolType = models.CharField(max_length=10, choices=(('Anadolu', 'Anadolu'), ('Fen', 'Fen'),\
        ('İmam Hatip', 'İmam Hatip')), blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.schoolType + " Lisesi"


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

    def __str__(self):
        return self.code

class Course(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, blank=True, null=True)
    classroom = models.ForeignKey(Classroom, blank=True, null=True, related_name='course')
    start = models.TimeField(default=timezone.now)
    end = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.classroom.code + " " + self.name

class CourseDate(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True)
    date = models.DateField(default=timezone.now)
    start = models.TimeField(default=timezone.now)
    end = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.course.name + " " + str(self.date)

class BookPayment(models.Model):
    Months = (('eylül','Eylül'), ('ekim','Ekim'), ('kasım','Kasım'),
              ('aralık','Aralık'), ('ocak','Ocak'), ('şubat','Şubat'),
              ('mart','Mart'), ('nisan','Nisan'), ('mayıs','Mayıs'),
              ('haziran','Haziran'), ('temmuz','Temmuz'), ('ağustos','Ağustos'))
    month = models.CharField(max_length=100,choices = Months, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.month + ' ' + str(self.cost)


class LisarSemester(models.Model):
    semester = models.CharField(max_length=300, blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.semester


class SchoolSemester(models.Model):
    semester = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.semester

# START OF Student
class Student(models.Model):

    firstName = models.CharField(max_length=300, verbose_name="İsim")
    lastName = models.CharField(max_length=300, verbose_name="Soyisim")
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{12}$',\
        message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.")
    phoneNumber = models.CharField(validators=[phoneRegex], blank=True, max_length=13, verbose_name="Telefon")
    dateOfBirth = models.DateField(max_length=8, default=timezone.now, verbose_name="Doğum Tarihi")
    mailAddress = models.EmailField(verbose_name="Email Adresi")

    adress = models.CharField(max_length=500, blank=True, null=True, verbose_name="Adres")
    residence = models.CharField(max_length=10, choices=(('Ev', 'Ev'), ('Yurt', 'Yurt')),\
        blank=True, null=True, verbose_name="Kaldığı Yer")
    reference = models.TextField(blank=True, null=True, verbose_name="Referanslar")
    admissionCause = models.TextField(blank=True, null=True, verbose_name="Başvuru Sebebi")

    TEOGScore = models.FloatField(blank=True, null=True, verbose_name="TEOG Skoru")

    highSchool = models.ForeignKey(HighSchool, related_name="students", blank=True, null=True, verbose_name="Lise")
    schoolLevel = models.CharField(max_length=10, choices=(('9.', '9.'), ('10.', '10.'), ('11.', '11.'), ('12.', '12.')),\
        blank=True, null=True, verbose_name="Sınıf")

    lisarLevel = models.CharField(max_length=10, choices=(('1.', '1.'), ('2.', '2.')),\
        blank=True, null=True, verbose_name="Lisar Kademesi")

    profilePhoto = models.ImageField(upload_to='img/', blank=True, verbose_name="Fotoğraf")

    def save(self, *args, **kwargs):
        try:
            this = Student.objects.get(pk=self.pk)
            if this.profilePhoto != self.profilePhoto and this.profilePhoto != 'img/profilePhoto.png':
                this.profilePhoto.delete(save=False)
        except: pass
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + " " + self.firstName + " " + self.lastName

# END OF Student


class StudentPayment(models.Model):
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
    totalAmount = models.FloatField()

    def __str__(self):
        return self.totalAmount + " TL"
