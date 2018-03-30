from django.conf.urls import include, url
from . import views
from mainApp.views import UserCreationForm

from django.views.generic import ListView, DetailView
from mainApp.models import Area
from mainApp.views import AreaList, AreaDetailView, ServiceDetailView

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^register/$', views.register_user, name="register"),

    url(r'^areas/$', AreaList.as_view(), name="areas"),
    url(r'^areas/(?P<pk>\d+)$', AreaDetailView.as_view(), name="areas-detail"),
    url(r'^areas/service/(?P<pk>\d+)/$', ServiceDetailView.as_view(), name="service-detail"),
    url(r'^order/', views.make_order, name="order"),

    url(r'^area/create/$', views.AreaCreate.as_view(), name='area-create'),
    url(r'^area/(?P<pk>\d+)/update/$', views.AreaUpdate.as_view(), name='area-update'),
    url(r'^area/(?P<pk>\d+)/delete/$', views.AreaDelete.as_view(), name='area-delete'),
]