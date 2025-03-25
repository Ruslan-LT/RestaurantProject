from django.shortcuts import render


food_buttons = [{'title': 'Звичайні страви', 'ref':'normal_food'},
               {'title': "М'ясні страви", 'ref':'meat_food'},
               {'title': 'Морепродукти', 'ref':'sea_food'}]

nav_buttons = [{'title': 'Головна сторінка', 'ref':'main_page'},
               {'title': 'Про нас', 'ref':'about'},
               {'title': 'Зареєструватися', 'ref':'login'},
               {'title':'Каталог Страв', 'food_buttons':food_buttons}]

def render_food_page(request, title, template_name):
    data = {
        'title': title,
        'nav_buttons': nav_buttons,
        'food_buttons': food_buttons
    }
    return render(request, template_name, context=data)

def normal_food(request):
    return render_food_page(request, 'Звичайні страви', 'normal_food/index.html')

def sea_food(request):
    return render_food_page(request, 'Морські страви', 'sea_food/index.html')

def meat_food(request):
    return render_food_page(request, "М'ясні страви", 'meat_food/index.html')
