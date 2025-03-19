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

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінку не знайдено 😕</h1>")

def about(request):
    data = {
        'title': 'Про Нас',
        'nav_buttons': nav_buttons,
        'food_buttons': food_buttons
    }
    return render(request, 'about/index.html', context=data)

def main_page(request):
    data = {
        'title':'Головна сторінка',
        'nav_buttons': nav_buttons,
        'food_buttons':food_buttons
    }
    return render(request, "main_page/index.html", context=data)

def login(request):
    data = {
        'title': 'Логін',
        'nav_buttons': nav_buttons,
        'food_buttons': food_buttons
    }
    return render(request, 'login/index.html', context=data)

def normal_food(request):
    data = {
        'title': 'Звичайні страви',
        'nav_buttons': nav_buttons,
        'food_buttons': food_buttons
    }
    return render(request, 'normal_food/index.html', context=data)

def sea_food(request):
    data = {
        'title': "Морські страви",
        'nav_buttons': nav_buttons,
        'food_buttons': food_buttons
    }
    return render(request, 'sea_food/index.html', context=data)


def meat_food(request):
    data = {
        'title': "М'ясні страви",
        'nav_buttons': nav_buttons,
        'food_buttons': food_buttons,
    }
    return render(request, 'meat_food/index.html', context=data)

