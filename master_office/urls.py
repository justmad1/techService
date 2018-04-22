from django.conf.urls import include, url
from . import views

from django.views.generic import ListView, DetailView
from master_office.views import OrderList, OrderDetailView

urlpatterns = [
    url(r'^orders$', OrderList.as_view(), name="master_orders"),
    url(r'^orders/(?P<pk>\d+)/$', OrderDetailView.as_view(), name="master_orders-detail"),

    # url(r'^areas/$', AreaList.as_view(), name="areas"),
    # url(r'^areas/(?P<pk>\d+)$', AreaDetailView.as_view(), name="areas-detail"),
    # url(r'^areas/service/(?P<pk>\d+)/$', ServiceDetailView.as_view(), name="service-detail"),
    # url(r'^order/', views.make_order, name="order"),

    # url(r'^area/create/$', views.AreaCreate.as_view(), name='area-create'),
    # url(r'^area/(?P<pk>\d+)/update/$', views.AreaUpdate.as_view(), name='area-update'),
    # url(r'^area/(?P<pk>\d+)/delete/$', views.AreaDelete.as_view(), name='area-delete'),
]