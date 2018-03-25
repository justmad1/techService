from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from categories.models import Categories

urlpatterns = [
    url(r'^$',
        ListView.as_view(queryset=Categories.objects.all()[:20],template_name='categories/categories.html')),
    url(r'^(?P<pk>\d+)$', 'categories.views.basic_one'),
    # url(r'^(?P<pk>\d+)$',
        # DetailView.as_view(model=Categories, template_name='categories/category.html'))
]


# urlpatterns = patterns('',
#                        # Examples:
#                        # url(r'^$', 'firstapp.views.home', name='home'),
#                        # url(r'^blog/', include('blog.urls')),

#                        url(r'^1/', 'article.views.basic_one'),
#                        url(r'^2/', 'article.views.template_two'),
#                        url(r'^3/', 'article.views.template_three_simple'),
#                        url(r'^articles/all/$', 'article.views.articles'),
#                        url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
#                        url(r'^articles/addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
#                        url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
#                        url(r'^page/(\d+)/$', 'article.views.articles'),
#                        url(r'^', 'article.views.articles'),

#                        )