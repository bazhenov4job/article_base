from django.shortcuts import render, HttpResponseRedirect
from .forms import ScientistLoginForm
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


def registration(request):
    pass
    """title = 'Регистрация пользователя'
    registration_form = ScientistRegistrationForm
    if request.method == 'POST' and registration_form.is_valid():
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        position = request.POST['position']
        username = request.POST['username']
        password = request.POST['password']"""


