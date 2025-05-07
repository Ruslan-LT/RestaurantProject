from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from utils.navigate_buttons import nav_buttons
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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
                messages.success(request, f' {username}, Ви успішно увійшли в аккаунт')

                if request.POST.get('next', False):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main_page'))
    else:
        form = UserLoginForm()


    return return_page(request, 'Логін','login.html', form=form)



@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Профайл успішно оновлений')
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = ProfileForm(instance=request.user)
    return return_page(request, 'Профіль','profile.html' , form=form)



def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f' {user.username}, Ви успішно зареєстровані та увійшли в аккаунт')
            return HttpResponseRedirect(reverse('main_page'))
    else:
        form = UserRegistrationForm()
    return return_page(request, 'Регістрація','registration.html' , form=form)


@login_required
def logout(request):
    messages.success(request, f' {request.user.username}, Ви вийшли з аккаунта')
    auth.logout(request)
    return  redirect(reverse('main_page'))


def users_cart(request):
    return return_page(request, 'Корзина', 'users_cart.html')