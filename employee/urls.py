from django.conf.urls import url, include
from . import views

urlpatterns = [  # url(r'^$', views.index, name='index'),
                 url(r'^create/$', views.CreateEmployee.as_view(), name='create'),
                 # url(r'^list/$', views.listing, name='list'),
                 # url(r'^home/$', views.home, name='home'),
                 url(r'^$', views.ListView.as_view(), name='index'),
                 url(r'^(?P<pk>[0-9]+)/$', views.UpdateView.as_view(), name='update'),
                 url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='delete')]

