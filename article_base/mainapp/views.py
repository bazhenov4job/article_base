from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "mainapp/index.html")


def library(request):
    pass


def bookshelf(request):
    pass


def profile(request):
    pass
