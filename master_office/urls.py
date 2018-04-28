from django.conf.urls import include, url
from . import views

from django.views.generic import ListView, DetailView
from master_office.views import OrderList, OrderDetailView

urlpatterns = [
    url(r'^orders/$', OrderList.as_view(), name="orders"),
    url(r'^my_orders/$', 'master_office.views.masters_orders', name="masters_orders"),
    url(r'^my_closed_orders/$', 'master_office.views.masters_closed_orders', name="masters_closed_orders"),
    url(r'^orders/take_order/(?P<pk>\d+)/$', 'master_office.views.take_order', name="take_order"),
    url(r'^orders/close_order/(?P<pk>\d+)/$', 'master_office.views.take_order', name="close_order"),

    # url(r'^orders/(?P<pk>\d+)/$', OrderDetailView.as_view(), name="master_orders-detail"),
    # url(r'^add_comment/$', views.add_comment),

    url(r'^orders/all_services/$', 'master_office.views.show_orderlines', name="orderlines"),
    url(r'^orders/(?P<pk>\d+)/$', 'master_office.views.order', name="master_orders-detail"),
    url(r'^orders/(?P<pk>\d+)/addcomment/$', 'master_office.views.addcomment', name="addcomment"),
    # url(r'^orders/comment/(?P<article_id>[0-9]+)/$', views.add_comment, name='add_comment'),
]