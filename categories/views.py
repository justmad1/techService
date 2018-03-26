from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from categories.models import Categories

class CategoriesList(ListView):
    model = Categories

class CategoriesDetailView(DetailView):
    model = Categories

def book_detail_view(request,pk):
    try:
        book_id=Categories.objects.get(pk=pk)
    except Categories.DoesNotExist:
        raise Http404("Categories does not exist")

    #book_id=get_object_or_404(Categories, pk=pk)

    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )