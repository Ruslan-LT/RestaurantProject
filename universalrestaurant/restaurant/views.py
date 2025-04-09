from django.http import HttpResponseNotFound
from django.shortcuts import render

from utils.navigate_buttons import nav_buttons


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

<<<<<<< HEAD
=======
def login(request):
    return return_page(request,'Логін', 'login/index.html')

>>>>>>> 2bcde29b6c4e3882e13e228b684f1ed14d675d38

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінку не знайдено 😕</h1>")

