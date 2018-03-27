from django.conf.urls import include, url
from . import views
from mainApp.views import UserCreationForm

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^register/$', views.register_user),
]
