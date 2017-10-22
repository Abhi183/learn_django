from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/$', views.add, name='index'),
    url(r'^multi/$', views.multi, name='index'),
]
