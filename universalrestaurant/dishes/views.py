from django.shortcuts import render

from nav_buttons.navigate_buttons import nav_buttons

from dishes.utils import json_format


def render_food_page(request, title, template_name, **kwargs):
    data = {
        'title': title,
        'nav_buttons': nav_buttons,
        **kwargs
    }
    return render(request, template_name, context=data)

def normal_food(request):
    return render_food_page(request, 'Звичайні страви', 'normal_food/index.html', food=json_format.n_dishes)

def sea_food(request):
    return render_food_page(request, 'Морські страви', 'sea_food/index.html')

def meat_food(request):
    return render_food_page(request, "М'ясні страви", 'meat_food/index.html')
