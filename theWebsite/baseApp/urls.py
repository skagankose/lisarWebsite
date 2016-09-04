from django.conf.urls import include, url
from . import views

urlpatterns = [

    # Homepage
    url(r'^$', views.home, name='home'),

]
