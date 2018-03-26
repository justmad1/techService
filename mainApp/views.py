from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from categories.models import Categories
from news.models import Articles

def index(request):
    num_categories=Categories.objects.all().count()
    num_articles=Articles.objects.all().count()
    num_instances_available=Articles.objects.filter(author__exact='kate').count()
    return render(
        request,
        'mainApp/home.html',
        context={'num_categories':num_categories,'num_articles':num_articles,'num_instances_available':num_instances_available},
    )

@login_required
def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['blablabla', '3578548']})
