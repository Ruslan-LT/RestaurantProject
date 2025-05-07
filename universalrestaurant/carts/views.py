from itertools import product

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from carts.models import Cart
from carts.utils import get_user_carts
from dishes.models import Dishes
from django.template.loader import render_to_string

from dishes.templatetags.dish_tags import register


@require_POST
def cart_add(request):

    dish_id = request.POST.get('dish_id')
    dish = Dishes.objects.get(id=dish_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, dish=dish)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, dish=dish, quantity=1)

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string('includes/include_cart.html', {'cart': user_cart}, request=request)
    return JsonResponse({'cartModal': cart_items_html})





@require_POST
def cart_change(request):
    cart_id = request.POST.get('cartID')
    quantity = request.POST.get('quantity')
    cart = Cart.objects.get(id=cart_id)
    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    cart = get_user_carts(request)
    cart_items_html = render_to_string('includes/include_cart.html', {'cart': cart}, request=request)

    response_data = {"html_context": cart_items_html,
                     "quantity": updated_quantity}

    return JsonResponse(response_data)


@require_POST
def cart_remove(request):


    cart_id = request.POST.get('cart_id')
    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string('includes/include_cart.html',{'cart': user_cart}, request=request)

    response_data = {"html_context": cart_items_html,
                     "quantity_deleted": quantity}


    return JsonResponse(response_data)