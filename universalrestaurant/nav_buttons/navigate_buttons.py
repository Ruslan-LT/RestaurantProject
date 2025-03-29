food_buttons = [{'title': 'Звичайні страви', 'ref':'normal_food'},
               {'title': "М'ясні страви", 'ref':'meat_food'},
               {'title': 'Морепродукти', 'ref':'sea_food'}]

my_profile_buttons =  [{'title':'Корзина', 'ref':'main_page'},
                       {'title':'Особистий кабінет', 'ref':'main_page'},
                       {'title':'Адмін панель', 'ref':'admin:index'},
                       {'title':'Вийти', 'ref':'main_page'},]

nav_buttons = [{'title': 'Головна сторінка', 'ref':'main_page'},
               {'title': 'Про нас', 'ref':'about'},
               {'title': 'Зареєструватися', 'ref':'login'},
               {'title':'Каталог Страв', 'other_buttons':food_buttons},
               {'title':'Мій профіль', 'other_buttons':my_profile_buttons},]