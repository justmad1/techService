from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from news.models import Articles
from .models import Comment, Master, OrderLine
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from news.models import Articles
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from mainApp.forms import UserRegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from mainApp.forms import UserRegisterForm
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.views.decorators.http import require_http_methods
import django.contrib.auth
from mainApp.models import Area, Service
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from master_office.models import Order, OrderLine
from django.shortcuts import get_object_or_404

from django.forms.formsets import formset_factory


@login_required
def orders(request):
    pass

class OrderList(ListView):
    model = Order

class OrderDetailView(DetailView):
    model = Order


def order(request, pk=1):
    comment_form = CommentForm()
    args = {}
    # args.update(csrf(request))
    args['order'] = Order.objects.get(id=pk)
    args['comments'] = Comment.objects.filter(order=args['order'])
    args['form'] = comment_form
    args['username'] = request.user
    return render(request, 'master_office/order_detail.html', args)

def show_orderlines(request):
    args = {}
    # args.update(csrf(request))

    master = Master.objects.get(user_id = request.user.id)
    args['serveces'] = Service.objects.filter(area__in=master.areas.all)
    args['orderlines'] = OrderLine.objects.filter(service__in=args['serveces'].all).exclude(master__isnull=False)
    args['page'] = 'all_orderlines'
    return render(request, 'master_office/orderline_list.html', args)
# module.workflow_set.filter(trigger_roles__in=[self.role], allowed=True)
# eventgroups__in=u.groups.all())
def masters_orders(request):
    args = {}
    # args.update(csrf(request))
    # args['master'] = Master.objects.get(user=request.user)
    master = Master.objects.get(user_id = request.user.id)
    args['orderlines'] = OrderLine.objects.filter(master=master).filter(status=0) #  Order.objects.get(master.id = request.user.id)
    args['page'] = 'masters_orderlines'
    return render(request, 'master_office/orderline_list.html', args)


def masters_closed_orders(request):
    args = {}
    # args.update(csrf(request))
    # args['master'] = Master.objects.get(user=request.user)
    master = Master.objects.get(user_id = request.user.id)
    args['orderlines'] = OrderLine.objects.filter(master=master).filter(status=1) #  Order.objects.get(master.id = request.user.id)
    args['page'] = 'closed'
    return render(request, 'master_office/orderline_list.html', args)

def take_order(request, pk):
    args = {}
    # args.update(csrf(request))
    # args['master'] = Master.objects.get(user=request.user)

    master = Master.objects.get(user_id = request.user.id)
    line = OrderLine.objects.get(id = pk)
    area = Area.objects.get(id = line.service.area.id)
    line.master = master
    line.save()
    return masters_orders(request)
    # return render(request, 'master_office/orderline_list.html', args)

def close_order(request, pk):
    args = {}
    # args.update(csrf(request))
    # args['master'] = Master.objects.get(user=request.user)

    master = Master.objects.get(user_id = request.user.id)
    line = OrderLine.objects.get(id = pk)
    line.status = 1

    # area = Area.objects.get(id = line.service.area.id)
    # line.master = master
    line.save()
    return masters_orders(request)
    # return render(request, 'master_office/orderline_list.html', args)


def addcomment(request, pk):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.rating = 0
            comment.author = request.user
            comment.order = Order.objects.get(id=pk)
            form.save()
            return redirect('master_orders-detail', pk=pk)
            # return HttpResponseRedirect('/')
    else:
        form = CommentForm()
    return render(request, 'registration/register.html', {'form': form})




# >>> for form in formset:
# ...     print(form.as_table())
#         form = OrderForm(request.POST)
#         if form.is_valid():



# >>>
# >>> ArticleFormSet = formset_factory(ArticleForm)

#     order = models.ForeignKey('Order', on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     master = models.ForeignKey('Master', on_delete=models.CASCADE, blank=True)
#     brand_name = models.CharField(max_length = 20)
#     device_name = models.CharField(max_length = 20)
#     serial_id = models.CharField(max_length = 20)
#     feedback = models.TextField(blank=True)
#     trouble_description = models.TextField()
#     status = models.IntegerField(default = 0)



# comment.author = request.user
#     author = Author.objects.get(pk=author_id)
#     BookInlineFormSet = inlineformset_factory(Author, Book, fields=('title',))
#     if request.method == "POST":
#         formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
#         if formset.is_valid():
#             formset.save()
#             # Do something. Should generally end with a redirect. For example:
#             return HttpResponseRedirect(author.get_absolute_url())
#     else:
#         formset = BookInlineFormSet(instance=author)
#     return render_to_response("manage_books.html", {
#         "formset": formset,
#     })






    # return redirect('master_orders-detail', pk=pk, {'form': form})

# class Comment(models.Model):
#     content = models.TextField(verbose_name="Текст комментария")
#     rating = models.IntegerField(default = 0)
#     author = models.ForeignKey(User)
#     order = models.ForeignKey(Order)
#     date = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.content
    # if request.method == 'POST':
    #     form = UserRegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/')
    # else:
    #     form = UserRegisterForm()

    # return render(request, 'registration/register.html', {'form': form})


# def add_comment_to_order(request, pk):
#     order = get_object_or_404(Order, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.order = order
#             comment.author = auth.get_user(request)
#             comment.save()
#             return redirect('master_orders-detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'master_office/order_detail.html', {'form': form})


# def add_comment(request):
#     OrderDetailView.as_view()
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = CommentForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = CommentForm()

    # return render(request, 'order_detail.html', {'form': form})


# @login_required
# @require_http_methods(["POST"])
# def add_comment(request, order_id):

#     form = CommentForm(request.POST)
#     order = get_object_or_404(Order, id=article_id)

#     if form.is_valid():
#         comment = Comment()
#         comment.order = order
#         comment.author = auth.get_user(request)
#         comment.content = form.cleaned_data['comment_area']
#         comment.save()

#     return redirect(article.get_absolute_url())

# class ServiceDetailView(DetailView):
#     model = Service

# class AreaDetailView(DetailView):
#     model = Area

# def book_detail_view(request,pk):
#     try:
#         book_id=Area.objects.get(pk=pk)
#     except Area.DoesNotExist:
#         raise Http404("Area does not exist")

#     #book_id=get_object_or_404(Area, pk=pk)

#     return render(
#         request,
#         'catalog/book_detail.html',
#         context={'book':book_id,}
#     )

# def  make_order():
#     pass


# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy
# from .models import Area

# class AreaCreate(CreateView):
#     model = Area
#     fields = '__all__'
#     # initial={'date_of_death':'12/10/2016',}

# class AreaUpdate(UpdateView):
#     model = Area
#     fields = '__all__'
#     # ['first_name','last_name','date_of_birth','date_of_death']

# class AreaDelete(DeleteView):
#     model = Area
#     success_url = reverse_lazy('areas')


# def index(request):
#     num_categories=Area.objects.all().count()
#     num_articles=Articles.objects.all().count()
#     num_instances_available=Articles.objects.filter(author__exact='kate').count()
#     return render(
#         request,
#         'mainApp/home.html',
#         context={'num_categories':num_categories,'num_articles':num_articles,'num_instances_available':num_instances_available},
#     )