from django.shortcuts import render

from utils.navigate_buttons import nav_buttons


def return_page(request, title, template_name, **kwargs):
    data = {
        'title': title,
        'nav_buttons': nav_buttons,
        **kwargs
    }
    return render(request, template_name, context=data)

def login(request):
    return return_page(request, 'Логін','login.html')

def profile(request):
    return return_page(request, 'Профіль користувача','profile.html')

def registration(request):
    return return_page(request, 'Регістрація','registration.html')

def logout(request):
    return  return_page(request, 'Вихід з профілю', 'logout.html')