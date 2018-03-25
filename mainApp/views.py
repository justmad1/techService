from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'mainApp/home.html')

@login_required
def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['blablabla', '3578548']})
