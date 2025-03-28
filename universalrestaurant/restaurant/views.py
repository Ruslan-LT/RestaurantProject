from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import title

from nav_buttons.navigate_buttons import nav_buttons


def return_page(request, title, template_name, **kwargs):
    data = {
        'title': title,
        'nav_buttons': nav_buttons,
        **kwargs
    }
    return render(request, template_name, context=data)

def about(request):
    content = 'Текст про те, наскільки цей ресторан є гарним та классним'
    return return_page(request,'Про нас', 'about/index.html', page_content=content)

def main_page(request):
    return return_page(request, 'Головна сторінка',"main_page/index.html")

def login(request):
    return return_page(request,'Логін', 'login/index.html')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінку не знайдено 😕</h1>")

