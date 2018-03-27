from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from news.models import Articles

from django.contrib.auth.forms import UserCreationForm
from mainApp.forms import UserRegisterForm
from django.http import HttpResponseRedirect

def index(request):
    num_categories=Area.objects.all().count()
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


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form': form})


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from mainApp.models import Area, Service

class AreaList(ListView):
    model = Area

class ServiceDetailView(DetailView):
    model = Service

class AreaDetailView(DetailView):
    model = Area

def book_detail_view(request,pk):
    try:
        book_id=Area.objects.get(pk=pk)
    except Area.DoesNotExist:
        raise Http404("Area does not exist")

    #book_id=get_object_or_404(Area, pk=pk)

    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )

def  make_order():
    pass


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Area

class AreaCreate(CreateView):
    model = Area
    fields = '__all__'
    # initial={'date_of_death':'12/10/2016',}

class AreaUpdate(UpdateView):
    model = Area
    fields = '__all__'
    # ['first_name','last_name','date_of_birth','date_of_death']

class AreaDelete(DeleteView):
    model = Area
    success_url = reverse_lazy('areas')