from django.template.defaultfilters import title

from dishes.models import Categories
from restaurant.models import My_profile_Buttons

food_buttons = Categories.objects.all()
my_profile_buttons = My_profile_Buttons.objects.all()


nav_buttons = {'main_but':{'title': 'Головна сторінка', 'ref':'main_page'},
               'about_but':{'title': 'Про нас', 'ref':'about'},
               'menu_but':{'title':'Меню', 'other_buttons':food_buttons},
               'profile_but':{'title':'Мій профіль', 'other_buttons':my_profile_buttons},
               'login_but':{'title': 'Увійти', 'ref':'login'},
               'my_orders_but':{'title': 'Мої замовлення', 'ref':'show_orders'},}


# food_buttons = [{'title': 'Звичайні страви', 'ref':'food_menu'},
#                {'title': "М'ясні страви", 'ref':'meat_food'},
#                {'title': 'Морепродукти', 'ref':'sea_food'}]

# my_profile_buttons =  [{'title':'Корзина', 'ref':'main_page'},
#                        {'title':'Особистий кабінет', 'ref':'main_page'},
#                        {'title':'Адмін панель', 'ref':'admin:index'},
#                        {'title':'Вийти', 'ref':'main_page'},]