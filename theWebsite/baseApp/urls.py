from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),

    # Student List
    url(r'^students/$', views.students, name='students'),

    # Students Details
    url(r'^studentDetails/(?P<pk>[0-9]+)/$', views.studentDetails, name='studentDetails'),

    # Registrations
    url(r'^ogrencikaydi/$', views.ogrencikaydi, name='ogrencikaydi'),
    url(r'^ogretmenkaydi/$', views.ogretmenkaydi, name='ogretmenkaydi'),
    url(r'^derskaydi/$', views.derskaydi, name='derskaydi'),
    url(r'^donemkaydi/$', views.donemkaydi, name='donemkaydi'),
    url(r'^sinifkaydi/$', views.sinifkaydi, name='sinifkaydi'),

]
