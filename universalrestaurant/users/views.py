from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from users.forms import UserLoginForm, UserRegistrationForm
from utils.navigate_buttons import nav_buttons
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

def return_page(request, title, template_name, **kwargs):
    data = {
        'title': title,
        'nav_buttons': nav_buttons,
        **kwargs
    }
    return render(request, template_name, context=data)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main_page'))
    else:
        form = UserLoginForm()


    return return_page(request, 'Логін','login.html', form=form)

def profile(request):
    return return_page(request, 'Профіль користувача','profile.html')

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main_page'))
    else:
        form = UserRegistrationForm()
    return return_page(request, 'Регістрація','registration.html' , form=form)

def logout(request):
    auth.logout(request)
    return  redirect(reverse('main_page'))