from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class CurrentDate(models.Model):
    date = models.DateField(default=timezone.now,null=Ture)

    def __str__(self):
        return str(self.pk) + "-" + str(self.date)

class HighSchool(models.Model):
    name = models.CharField(max_length=500, verbose_name="İSİM", null=True)
    schoolType = models.CharField(max_length=50, choices=(('Anadolu', 'Anadolu'), ('Fen', 'Fen'),\
        ('İmam Hatip', 'İmam Hatip'), ('Anadolu İmam Hatip', 'Anadolu İmam Hatip')), verbose_name="OKUL TİPİ", null=True)

    def __str__(self):
        return self.name + " " + self.schoolType + " Lisesi"

class School(models.Model):
    name = models.CharField(max_length=500, verbose_name="İSİM", null=True)
    schoolType = models.CharField(max_length=50, choices=(('Lisesi', 'Lise'), ('Üniversitesi', 'Üniversite')),\
        verbose_name="OKUL TİPİ", null=True)

    def __str__(self):
        return self.name + " " + self.schoolType



# START OF Teacher
class Teacher(models.Model):
    firstName = models.CharField(max_length=300, verbose_name="İSİM", null=True)
    lastName = models.CharField(max_length=300, verbose_name="SOYİSİM", null=True)
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{12}$',\
        message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.")
    phoneNumber = models.CharField(validators=[phoneRegex], blank=True, max_length=13, verbose_name="Telefon", null=True)
    mailAddress = models.EmailField(blank=True, null=True, verbose_name="EMAIL ADRESİ")
    school = models.ForeignKey(School, related_name="teachers", blank=True, null=True, verbose_name="OKUL")
    department = models.CharField(max_length=300, choices = (('bilgisayar mühendisliği', 'Bilgisayar Mühendisliği'),\
                                                             ('kimya', 'Kimya')),\
        blank=True, null=True, verbose_name="BÖLÜM")
    status = models.CharField(max_length=30, choices = (('lisans', 'Lisans'), ('yüksek lisans', 'Yüksek Lisans'),
        ('doktora', 'Doktora')), blank=True, null=True, verbose_name="STATÜ")

    IBANRegex = RegexValidator(regex=r'^\w{2}\d{24}$',\
        message="IBAN must be entered in the format: 'TR999999999999999999999999'. 24 digits allowed.")
    IBAN = models.CharField(validators=[IBANRegex], max_length=26, blank=True, null=True, verbose_name="IBAN NO")
    profilePhoto = models.ImageField(upload_to='img/', blank=True, verbose_name="FOTOĞRAF")

    def save(self, *args, **kwargs):
        try:
            this = Teacher.objects.get(pk=self.pk)
            if this.profilePhoto != self.profilePhoto and this.profilePhoto != 'img/profilePhoto.png':
                this.profilePhoto.delete(save=False)
        except: pass
        self.fullName = self.firstName + " " + self.lastName
        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return self.firstName + " " + self.lastName
# END OF Teacher



class BookPayment(models.Model):
    Months = (('eylül','Eylül'), ('ekim','Ekim'), ('kasım','Kasım'),
              ('aralık','Aralık'), ('ocak','Ocak'), ('şubat','Şubat'),
              ('mart','Mart'), ('nisan','Nisan'), ('mayıs','Mayıs'),
              ('haziran','Haziran'), ('temmuz','Temmuz'), ('ağustos','Ağustos'))
    month = models.CharField(max_length=100,choices = Months, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.month + ' ' + str(self.cost)


# START OF Student
class Student(models.Model):

    firstName = models.CharField(max_length=300, verbose_name="İSİM")
    lastName = models.CharField(max_length=300, verbose_name="SOYİSİM")
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{12}$',\
        message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.")
    phoneNumber = models.CharField(validators=[phoneRegex], blank=True, null=True, max_length=13, verbose_name="TELEFON")
    dateOfBirth = models.DateField(max_length=8, default=timezone.now, verbose_name="DOĞUM TARİHİ")
    parentMailAddress = models.EmailField(default="2beordinary@gmail.com", blank=True,null=True, verbose_name="VELİ EMAIL ADRESİ")
    mailAddress = models.EmailField(blank=True,null=True, verbose_name="EMAIL ADRESİ")

    adress = models.CharField(max_length=500, blank=True, null=True, verbose_name="ADRES")
    residence = models.CharField(max_length=10, choices=(('Ev', 'Ev'), ('Yurt', 'Yurt')),\
        blank=True, null=True, verbose_name="KALDIĞI YER")
    reference = models.TextField(blank=True, null=True, verbose_name="REFERANSLAR")
    admissionCause = models.TextField(blank=True, null=True, verbose_name="BAŞVURU SEBEBİ")

    TEOGScore = models.FloatField(blank=True, null=True, verbose_name="TEOG SKORU")

    highSchool = models.ForeignKey(HighSchool, related_name="students", blank=True, null=True, verbose_name="LİSE")
    schoolLevel = models.CharField(max_length=10, choices=(('9', '9'), ('10', '10'), ('11', '11'),\
        ('12', '12'), ('13', 'Mezun')), default="9", verbose_name="SINIF")

    lisarLevel = models.CharField(max_length=10, choices=(('1', '1'), ('2', '2'), ('3', 'Mezun')),\
        default="1", verbose_name="LİSAR KADEMESİ")

    profilePhoto = models.ImageField(upload_to='img/', blank=True, verbose_name="FOTOĞRAF")

    def save(self, *args, **kwargs):
        try:
            this = Student.objects.get(pk=self.pk)
            if this.profilePhoto != self.profilePhoto and this.profilePhoto != 'img/profilePhoto.png':
                this.profilePhoto.delete(save=False)
        except: pass
        self.fullName = self.firstName + " " + self.lastName
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.firstName + " " + self.lastName
# END OF Student

class Classroom(models.Model):
    code = models.CharField(max_length=300, verbose_name="KOD", null=True)
    location = models.CharField(max_length=300, blank=True, null=True, verbose_name= "YER")
    students = models.ManyToManyField(Student, related_name='classroom', blank=True,verbose_name= "ÖĞRENCİLER")

    def __str__(self):
        return self.code

# START OF Course
class Course(models.Model):
    name = models.CharField(max_length=300, verbose_name="İSİM", null=True)
    code = models.CharField(max_length=300, verbose_name="KOD", null=True)
    teacher = models.ForeignKey(Teacher, verbose_name="ÖĞRETMEN", null=True)
    classroom = models.ForeignKey(Classroom, null=True, related_name='courses', verbose_name="SINIF")
    lisarLevel = models.CharField(max_length=10, choices=(('1.', '1.'), ('2.', '2.')),\
        verbose_name="LİSAR KADEMESİ", null=True)
    start = models.TimeField(default=timezone.now, verbose_name="BAŞLANGIÇ SAATİ")
    end = models.TimeField(default=timezone.now, verbose_name="BİTİŞ SAATİ")


    def __str__(self):
        return self.name + " / " + self.classroom.code
# END OF Course

class StudentPayment(models.Model):
    student = models.ForeignKey(Student, blank=True, null=True)
    payment = models.ForeignKey(BookPayment, blank=True, null=True)
    isPaid = models.BooleanField(default=False)

    def __str__(self):
        if self.isPaid == True:
            return  "%s %s - %s PAID" %(self.student.firstName,self.student.lastName,self.payment.month)
        else:
            return "%s %s - %s notPAID" %(self.student.firstName,self.student.lastName,self.payment.month)

# START OF Attendance
class CreateAttendance(models.Model):
    date = models.DateField(max_length=8, default=timezone.now, verbose_name="TARİH")
    course = models.ForeignKey(Course, verbose_name="DERS", null=True)

    def __str__(self):
        return  str(self.course)+ " " + str(self.date)
# END OF Attendance

# START OF individualAttendance
class Attendance(models.Model):
    student = models.ForeignKey(Student, null=True, related_name="attendance", verbose_name="ÖĞRENCİ")
    course = models.ForeignKey(Course, null=True, related_name="attendance")
    date = models.DateField(max_length=8, default=timezone.now)
    isHere = models.BooleanField(default=False)
    isCancelled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.course) + " - " + str(self.date) + " - " + self.student.firstName

# START OF individualAttendance
# START OF Not Neccesseary for Now
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
# END OF Not Neccesseary for Now
