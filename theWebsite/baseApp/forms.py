from django.forms import ModelForm
from .models import Student, Teacher, Course

# Create the form class.
class OgrenciKayit(ModelForm):
  class Meta:
    model = Student
    fields = ['firstName', 'lastName', 'dateOfBirth', 'phoneNumber',
    'mailAddress', 'adress', 'place', 'reference', 'reason',
    'highSchool', 'schoolSemester', 'teogScore',
    'lisarSemester', 'classroom' ]

class OgretmenKayit(ModelForm):
  class Meta:
    model = Teacher
    fields = ['firstName', 'lastName', 'phoneNumber', 'university', 'department', 'degree',
    'mailAddress', 'ibanNo']

class DersKayit(ModelForm):
  class Meta:
    model = Course
    fields = ['name', 'teacher', 'classroom', 'start', 'end']
