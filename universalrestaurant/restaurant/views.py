from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render


nav_buttons = [{'title': 'Головна сторінка', 'ref':'main_page'},
               {'title': 'Про нас', 'ref':'about'},
               {'title': 'Увійти', 'ref':'login'}]

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінку не знайдено 😕</h1>")

def about(request):
    data = {
        'title': 'Про Нас',
        'nav_buttons': nav_buttons
    }
    return render(request, 'about/index.html', context=data)

def main_page(request):
    data = {
        'title':'Головна сторінка',
        'nav_buttons': nav_buttons
    }
    return render(request, "main_page/index.html", context=data)

def login(request):
    data = {
        'title': 'Логін',
        'nav_buttons': nav_buttons
    }
    return render(request, 'login/index.html', context=data)

