from django.contrib import admin

from .models import Student, SchoolType, HighSchool

admin.site.register(Student)
admin.site.register(HighSchool)
admin.site.register(SchoolType)
