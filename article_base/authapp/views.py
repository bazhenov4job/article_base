from django.shortcuts import render, HttpResponseRedirect
from .forms import ScientistLoginForm, ScientistRegistrationForm
from django.contrib import auth
from django.urls import reverse

# Create your views here.


def login(request):
    title = 'Вход'
    login_form = ScientistLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    content = {
        'title': title,
        'login_form': login_form
    }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'Регистрация пользователя'

    if request.method == 'POST':
        register_form = ScientistRegistrationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))

    else:
        register_form = ScientistRegistrationForm()

    content = {
        'title': title,
        'register_form': register_form,
    }
    return render(request, 'authapp/register.html', content)


def edit(request):
    return HttpResponseRedirect(reverse('main'))


