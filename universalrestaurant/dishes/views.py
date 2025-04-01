from django.shortcuts import render
from utils.navigate_buttons import nav_buttons
# from dishes.utils import json_format
from dishes.models import Dishes


def render_food_page(request, title, template_name, **kwargs):
    data = {
        'title': title,
        'nav_buttons': nav_buttons,
        **kwargs
    }
    return render(request, template_name, context=data)

def normal_food(request):
    food_data = Dishes.objects.filter(category=1)
    return render_food_page(request, 'Звичайні страви', 'food_menu/index.html', food=food_data)

def sea_food(request):
    food_data = Dishes.objects.filter(category=3)
    return render_food_page(request, 'Морські страви', 'food_menu/index.html', food=food_data)

def meat_food(request):
    food_data = Dishes.objects.filter(category=2)
    return render_food_page(request, "М'ясні страви", 'food_menu/index.html', food=food_data)

def dish_information(request, dish_slug):
    dish = Dishes.objects.get(slug=dish_slug)
    return render_food_page(request, dish.name, 'information/index.html', dish=dish)
