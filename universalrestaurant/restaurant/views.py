from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import title

food_buttons = [{'title': 'Звичайні страви', 'ref':'normal_food'},
               {'title': "М'ясні страви", 'ref':'meat_food'},
               {'title': 'Морепродукти', 'ref':'sea_food'}]

nav_buttons = [{'title': 'Головна сторінка', 'ref':'main_page'},
               {'title': 'Про нас', 'ref':'about'},
               {'title': 'Зареєструватися', 'ref':'login'},
               {'title':'Каталог Страв', 'food_buttons':food_buttons}]


def return_page(request, title, template_name, **kwargs):
    data = {
        'title': title,
        'nav_buttons': nav_buttons,
        'food_buttons': food_buttons,
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