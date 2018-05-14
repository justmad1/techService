from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from client_office.forms import FeedbackForm
from master_office.forms import CommentForm
from master_office.models import Order, Comment


def client_page(request):
    args = {}
    args['user'] = request.user
    return render(request, 'client_office/client_page.html', args)


def current_orders(request):
    user = request.user
    args = {}
    args['user'] = user
    args['orders'] = Order.objects.filter(client_id=user.pk).filter(status=0)
    args['title'] = "Текущие заказы"
    return render(request, 'client_office/current_orders.html', args)


def order(request, pk=1):
    comment_form = CommentForm()
    args = {}
    # args.update(csrf(request))
    order = Order.objects.get(id=pk)
    args['order'] = order
    args['comments'] = Comment.objects.filter(order=args['order'])
    args['username'] = request.user
    if order.status == 1:
        fb_form = FeedbackForm()
        args['fb_form'] = fb_form
    else:
        args['form'] = comment_form

    return render(request, 'client_office/order_detail.html', args)


def closed_orders(request):
    user = request.user
    args = {}
    args['user'] = user
    args['orders'] = Order.objects.filter(client_id=user.pk).filter(status=1)
    args['title'] = "Закрытые заказы"

    return render(request, 'client_office/current_orders.html', args)


def add_feedback(request, pk):
    args = {}
    comment_form = CommentForm()
    args = {}
    # args.update(csrf(request))
    args['order'] = Order.objects.get(id=pk)
    args['comments'] = Comment.objects.filter(order=args['order'])
    args['form'] = comment_form
    args['username'] = request.user

    fb_form = FeedbackForm()
    args['fb_form'] = fb_form

    if request.POST:
        args['fb_form'] = fb_form
        if fb_form.is_valid():
            form_res = fb_form.save(False)
            order = Order.objects.get(id=pk)
            order.feedback = form_res.feedback
            order.rating = form_res.rating
            order.save()
            args['ready'] = 'Спасибо за вашу оценку! Вы помогаете нам стать лучше!'
            return render(request, 'client_office/order_detail.html', args)
#            return redirect('client_orders-detail', pk=pk)
            # return HttpResponseRedirect('/')

    return render(request, 'client_office/order_detail.html', args)

