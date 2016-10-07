from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^aboutUs/$', views.aboutUs, name='aboutUs'),
    url(r'^emailAndHome/(?P<pk>[0-9]+)/$', views.emailAndHome, name='emailAndHome'),

    # Login
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html',},  name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

    # Classroom
    url(r'^classrooms/$', views.classrooms, name='classrooms'),
    url(r'^classroomDetails/(?P<pk>[0-9]+)/$', views.classroomDetails, name='classroomDetails'),

    # Students
    url(r'^students/$', views.students, name='students'),
    url(r'^studentDetails/(?P<pk>[0-9]+)/$', views.studentDetails, name='studentDetails'),

    # Teachers
    url(r'^teachers/$', views.teachers, name='teachers'),
    url(r'^teacherDetails/(?P<pk>[0-9]+)/$', views.teacherDetails, name='teacherDetails'),

    # Courses
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^courseDetails/(?P<pk>[0-9]+)/$', views.courseDetails, name='courseDetails'),

    # Edit Pages
    url(r'^studentDetails/(?P<pk>[0-9]+)/edit/$', views.studentDetailsEdit, name='studentDetailsEdit'),
    url(r'^teacherDetails/(?P<pk>[0-9]+)/edit/$', views.teacherDetailsEdit, name='teacherDetailsEdit'),
    url(r'^courseDetails/(?P<pk>[0-9]+)/edit/$', views.courseDetailsEdit, name='courseDetailsEdit'),
    url(r'^classroomDetails/(?P<pk>[0-9]+)/edit/$', views.classroomDetailsEdit, name='classroomDetailsEdit'),

    # Registrations
    url(r'^ogrencikaydi/$', views.ogrencikaydi, name='ogrencikaydi'),
    url(r'^ogretmenkaydi/$', views.ogretmenkaydi, name='ogretmenkaydi'),
    url(r'^derskaydi/$', views.derskaydi, name='derskaydi'),
    url(r'^sinifkaydi/$', views.sinifkaydi, name='sinifkaydi'),
    url(r'^gelirkaydi/$', views.gelirkaydi, name='gelirkaydi'),
    url(r'^giderkaydi/$', views.giderkaydi, name='giderkaydi'),
    url(r'^kitapodemesikaydi/$', views.kitapodemesikaydi, name='kitapodemesikaydi'),
    url(r'^unikaydi/$', views.unikaydi, name='unikaydi'),
    url(r'^lisekaydi/$', views.lisekaydi, name='lisekaydi'),

    # Attendace
    url(r'^createAttendance/$', views.createAttendance, name='createAttendance'),
    url(r'^attendance/(?P<pk>[0-9]+)/$', views.attendance, name='attendance'),
    url(r'^cancelAttendance/(?P<pk>[0-9]+)/$', views.cancelAttendance, name='cancelAttendance'),
    url(r'^markAttendance/(?P<capk>[0-9]+)/(?P<spk>[0-9]+)/$', views.markAttendance, name='markAttendance'),
    url(r'^studentAttendance/(?P<pk>[0-9]+)/$', views.studentAttendance, name='studentAttendance'),
    url(r'^attendanceTaken/$', views.attendanceTaken, name='attendanceTaken'),
    url(r'^attendances/$', views.attendances, name='attendances'),
    url(r'^attendanceDetails/(?P<pk>[0-9]+)/$', views.attendanceDetails, name='attendanceDetails'),


]
