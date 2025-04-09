from dishes.models import Categories
from restaurant.models import My_profile_Buttons

food_buttons = Categories.objects.all()
my_profile_buttons = My_profile_Buttons.objects.all()


nav_buttons = [{'title': 'Головна сторінка', 'ref':'main_page'},
               {'title': 'Про нас', 'ref':'about'},
<<<<<<< HEAD
               {'title':'Меню', 'other_buttons':food_buttons},
               {'title':'Мій профіль', 'other_buttons':my_profile_buttons},
               {'title': 'Увійти', 'ref':'login'},]
=======
               {'title': 'Зареєструватися', 'ref':'login'},
               {'title':'Меню', 'other_buttons':food_buttons},
               {'title':'Мій профіль', 'other_buttons':my_profile_buttons},]
>>>>>>> 2bcde29b6c4e3882e13e228b684f1ed14d675d38


# food_buttons = [{'title': 'Звичайні страви', 'ref':'food_menu'},
#                {'title': "М'ясні страви", 'ref':'meat_food'},
#                {'title': 'Морепродукти', 'ref':'sea_food'}]

# my_profile_buttons =  [{'title':'Корзина', 'ref':'main_page'},
#                        {'title':'Особистий кабінет', 'ref':'main_page'},
#                        {'title':'Адмін панель', 'ref':'admin:index'},
#                        {'title':'Вийти', 'ref':'main_page'},]