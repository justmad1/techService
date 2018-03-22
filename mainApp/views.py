from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/home.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['blablabla', '3578548']})
