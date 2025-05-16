from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from utils.navigate_buttons import nav_buttons
from utils.filter_buttons import filter_buttons
from dishes.models import Dishes, Categories
from utils.search_func import q_serarch


def render_food_page(request, title, template_name, **kwargs):
    data = {
        'title': title,
        'nav_buttons': nav_buttons,
        **kwargs
    }
    return render(request, template_name, context=data)

def food_by_category(request, category_slug=None):
    order_by = request.GET.get('order_by',None)
    on_sale = request.GET.get('on_sale', None)
    page = request.GET.get('page', 1)
    query = request.GET.get('q', None)
    if query:
        food_data = q_serarch(query)
        page_name = 'Результати пошуку'
    elif category_slug:
        category = get_object_or_404(Categories, slug=category_slug)
        food_data = Dishes.objects.filter(category=category)
        page_name = category.name
    else:
        food_data = Dishes.objects.all()
        page_name = 'Усі страви'
    if on_sale:
        food_data = food_data.filter(discount__gt=0)
    if order_by:
        food_data = food_data.order_by(order_by)


    paginator = Paginator(food_data, 6)
    current_page = paginator.page(page)
    return render_food_page(request, page_name, 'food_menu/index.html', food = current_page,
                            slug = category_slug, filter_buttons=filter_buttons)

def dish_information(request, dish_slug, category_slug):
    dish = get_object_or_404(Dishes, slug=dish_slug)
    return render_food_page(request, dish.name, 'information/index.html', dish=dish)
