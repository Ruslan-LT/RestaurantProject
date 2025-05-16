from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from utils.navigate_buttons import nav_buttons



def return_page(request, title, template_name, **kwargs):
    return render(request, template_name, context={
        'title': title,
        'nav_buttons': nav_buttons,
        'request': request,
        **kwargs
    })


@login_required
def create_order(request):
    return return_page(request, 'Оформити замовлення', 'orders/create_order.html')