from django.forms import ModelForm
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class AddHighSchool(ModelForm):
    class Meta:
        model = HighSchool
        fields = ['name', 'schoolType']

class AddUniversity(ModelForm):
    class Meta:
        model = School
        fields = ['name', 'schoolType']

# Create the form class.
class OgrenciKayit(ModelForm):
  class Meta:
    model = Student
    fields = ['firstName', 'lastName', 'dateOfBirth', 'phoneNumber',
    'mailAddress', 'adress', 'residence', 'reference', 'admissionCause',
    'highSchool', 'schoolLevel', 'TEOGScore',
    'lisarLevel','profilePhoto']
    widgets = {
        'dateOfBirth': DateInput(),
    }

class OgretmenKayit(ModelForm):
  class Meta:
    model = Teacher
    fields = ['firstName', 'lastName', 'phoneNumber', 'school', 'department',
    'status', 'mailAddress', 'IBAN', 'profilePhoto']

class DersKayit(ModelForm):
  class Meta:
    model = Course
    fields = ['name', 'code', 'teacher', 'classroom', 'lisarLevel', 'start', 'end', 'students']

class DonemKayit(ModelForm):
  class Meta:
    model = LisarSemester
    fields = ['semester', 'start', 'end']

class SinifKayit(ModelForm):
  class Meta:
    model = Classroom
    fields = ['code', 'location']

class CreateAttendanceForm(ModelForm):
  class Meta:
    model = CreateAttendance
    fields = ['date', 'course']

# Unused
class GelirKayit(ModelForm):
  class Meta:
    model = Income
    fields = ['date', 'amount']
    widgets = {
            'date': DateInput(),
        }

class GiderKayit(ModelForm):
  class Meta:
    model = Outcome
    fields = ['date', 'amount']
    widgets = {
            'date': DateInput(),
        }

class KitapOdemesiKayit(ModelForm):
  class Meta:
    model = BookPayment
    fields = ['month', 'cost']
