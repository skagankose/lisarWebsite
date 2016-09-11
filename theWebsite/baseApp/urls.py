from django.conf.urls import include, url
from . import views

urlpatterns = [

    # Homepage
    url(r'^$', views.home, name='home'),
    url(r'^ogrencikaydi/$', views.ogrencikaydi, name='ogrencikaydi'),
    url(r'^ogretmenkaydi/$', views.ogretmenkaydi, name='ogretmenkaydi'),
    url(r'^derskaydi/$', views.derskaydi, name='derskaydi'),
    url(r'^donemkaydi/$', views.donemkaydi, name='donemkaydi'),
    url(r'^sinifkaydi/$', views.sinifkaydi, name='sinifkaydi'),

]
