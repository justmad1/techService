from django.shortcuts import render

def basic_one(request):
    view = "basic_one"
    t = get_template('categories/category.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)
