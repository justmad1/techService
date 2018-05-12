from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from news.models import Articles
from mainApp.forms import UserRegisterForm, OrderLineForm
from django.http import HttpResponseRedirect
from master_office.models import Order, OrderLine, Master
from django.forms.formsets import formset_factory

def index(request):
    num_categories=Area.objects.all().count()
    num_articles=Articles.objects.all().count()
    num_instances_available=Articles.objects.filter(author__exact='kate').count()
    return render(
        request,
        'mainApp/home.html',
        context={'num_categories':num_categories,'num_articles':num_articles,'num_instances_available':num_instances_available},
    )

def contact(request):
    return render(request, 'mainApp/basic.html')


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        #     group = Group.objects.get(name='ServiceClient')
        #     user.groups.add(group)
        #     # form.save()
        #     # user.groups.add(group)
        #     # user.groups.add(1) # add by id
        # # /group.user_set.add(user)
        #     user.save()
            return HttpResponseRedirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form': form})


# g = Group.objects.get(name='My Group Name')
# users = User.objects.all()
# for u in users:
#     g.user_set.add(u)


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from mainApp.models import Area, Service

class AreaList(ListView):
    model = Area

class ServiceDetailView(DetailView):
    model = Service

class AreaDetailView(DetailView):
    model = Area

class MasterList(ListView):
    model = Master

class MasterDetailView(DetailView):
    model = Master



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

@login_required
def make_order(request):
    OrderLineFormSet = formset_factory(OrderLineForm, extra=1)
    if request.method == 'POST':
        formset = OrderLineFormSet(request.POST)
        if formset.is_valid():
            print('valid')
            order = Order()
            order.client = request.user
            order.price = 0
            order.save()
            for form in formset:

                if form.is_valid():
                    order_line = form.save(commit=False)
                    order_line.order = order
                    order_line.feedback = "123"
                    order_line.price = order_line.service.price
                    form.save()

            all_lines_in_order = OrderLine.objects.filter(order=order)
            total_price = 0
            for one_line in all_lines_in_order:
                total_price = total_price + one_line.service.price
            order.price = total_price
            order.save()
            # lines = formset.save(commit=False)
            # for line in lines:
            #     line.order = order
            #     line.save()
            # line = form.save(False)
            # line.order = order
            # line.feedback = ""
            # form.save()
            return render(request, 'mainApp/temp.html', {'formset': formset})
    else:
        formset = OrderLineFormSet()

    return render(request, 'mainApp/temp.html', {'formset': formset})

    # OrderLineFormSet = formset_factory(OrderLineForm)
    # formset = OrderLineFormSet()
    # if request.POST:
    #     if formset.is_valid():
    #         print("valid")
    #         order = Order()
    #         order.client = request.user
    #         order.price = 0
    #         order.save()
    #         # if formset.is_valid():
    #         for form in formset:

    #             if form.is_valid():
    #                 order_line = form.save(commit=False)
    #                 order_line.order = order
    #                 form.save()

    #     # orderLines = formset.save(commit=False)
    #     # else: formset.errors
    # else:
    #     print("novalid")
    #     print(formset.errors)
    #     messages.success(request, "Payments saved successfully")
    # return render(request, "mainApp/temp.html", {"formset": formset})

#     args['order'] = Order.objects.get(id=pk)
#     args['comments'] = Comment.objects.filter(order=args['order'])
#     args['form'] = comment_form
#     args['username'] = request.user
# class Order(models.Model):
#     client = models.ForeignKey(User, on_delete=models.CASCADE)
#     status = models.IntegerField(default = 0)
#     price = models.FloatField()
#     begin_date = models.DateTimeField(auto_now=True)
#     end_date = models.DateTimeField(blank=True)
#     expected_date = models.DateTimeField(blank=True)
#     rating = models.IntegerField(default = 0, blank=True)
#     feedback = models.TextField(blank=True)

# class OrderLine(models.Model):
#     order = models.ForeignKey('Order', on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     master = models.ForeignKey('Master', on_delete=models.CASCADE, blank=True)
#     brand_name = models.CharField(max_length = 20)
#     device_name = models.CharField(max_length = 20)
#     serial_id = models.CharField(max_length = 20)
#     feedback = models.TextField(blank=True)
#     trouble_description = models.TextField()
#     status = models.IntegerField(default = 0)


@login_required
def add_comment(request):
    OrderDetailView.as_view()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')





from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Area



class OrderLineCreate(CreateView):
    model = OrderLine
    fields = '__all__'



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

def do(self, **kwargs):
    print("1")
    return "1"