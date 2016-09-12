from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),

    # Students List
    url(r'^students/$', views.students, name='students'),

    # Students Details
    url(r'^studentDetails/(?P<pk>[0-9]+)/$', views.studentDetails, name='studentDetails'),

    # Teachers List
    url(r'^teachers/$', views.teachers, name='teachers'),

    # Teachers Details
    url(r'^teacherDetails/(?P<pk>[0-9]+)/$', views.teacherDetails, name='teacherDetails'),

    # Registrations
    url(r'^ogrencikaydi/$', views.ogrencikaydi, name='ogrencikaydi'),
    url(r'^ogretmenkaydi/$', views.ogretmenkaydi, name='ogretmenkaydi'),
    url(r'^derskaydi/$', views.derskaydi, name='derskaydi'),
    url(r'^donemkaydi/$', views.donemkaydi, name='donemkaydi'),
    url(r'^sinifkaydi/$', views.sinifkaydi, name='sinifkaydi'),

]
