from django.forms import ModelForm
from .models import *

# Create the form class.
class OgrenciKayit(ModelForm):
  class Meta:
    model = Student
    fields = ['firstName', 'lastName', 'dateOfBirth', 'phoneNumber',
    'mailAddress', 'adress', 'residence', 'reference', 'admissionCause',
    'highSchool', 'schoolLevel', 'TEOGScore',
    'lisarLevel','profilePhoto']

class OgretmenKayit(ModelForm):
  class Meta:
    model = Teacher
    fields = ['firstName', 'lastName', 'phoneNumber', 'school', 'department',
    'status', 'mailAddress', 'IBAN', 'profilePhoto']

class DersKayit(ModelForm):
  class Meta:
    model = Course
    fields = ['name', 'teacher', 'classroom', 'start', 'end']

class DonemKayit(ModelForm):
  class Meta:
    model = LisarSemester
    fields = ['semester', 'start', 'end']

class SinifKayit(ModelForm):
  class Meta:
    model = Classroom
    fields = ['code', 'location']
