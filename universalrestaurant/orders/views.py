from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Prefetch
from django.shortcuts import render, redirect
from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from utils.navigate_buttons import nav_buttons

@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = request.user
                cart_items = Cart.objects.filter(user=user)

                if cart_items.exists():
                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data['phone_number'],
                        requires_delivery=form.cleaned_data['requires_delivery'],
                        delivery_address=form.cleaned_data['delivery_address'],
                        payment_on_get=form.cleaned_data['payment_on_get'],
                    )

                    for cart_item in cart_items:
                        OrderItem.objects.create(
                            order=order,
                            dish=cart_item.dish,
                            name=cart_item.dish.name,
                            price=cart_item.dish.sell_price(),
                            quantity=cart_item.quantity,
                        )

                    cart_items.delete()
                    return redirect('profile')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Оформлення замолення',
        'form': form,
        'nav_buttons': nav_buttons,
    }

    return render(request, 'orders/create_order.html', context=context)


def show_orders(request):
    orders = (
        Order.objects.filter(user=request.user)
            .prefetch_related(
            Prefetch(
                'orderitem_set',
                queryset=OrderItem.objects.select_related('dish')
            )
        )
        .order_by('-created_timestamp')
    )

    context = {
        'title': 'Мої замовлення',
        'nav_buttons': nav_buttons,
        'orders': orders,
    }
    return render(request, 'orders/show_user_orders.html', context=context)

