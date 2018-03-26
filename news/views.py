from django.shortcuts imp
from django.views.generic import ListView
from news.models import Articles

class ArticlesList(ListView):
    model = Articles
