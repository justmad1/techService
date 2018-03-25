from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from categories.models import Categories

urlpatterns = [
    url(r'^$',
        ListView.as_view(queryset=Categories.objects.all()[:20],template_name='categories/categories.html')),
    url(r'^(?P<pk>\d+)$',
        DetailView.as_view(model=Categories, template_name='categories/category.html'))
]