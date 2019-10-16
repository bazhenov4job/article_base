from django.shortcuts import render

# Create your views here.


def index(request):
    title = 'Главная'
    content = {'title': title,
               }
    return render(request, "mainapp/index.html", content)


def library(request):
    pass


def bookshelf(request):
    pass


def profile(request):
    pass
