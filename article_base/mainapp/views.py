from django.shortcuts import render
import json

# added open from json file links in menu

with open('static/json/links.json', 'r', encoding="UTF-8") as read_file:
    links = json.load(read_file)['links']
# Create your views here.


def index(request):
    title = 'Главная'
    content = {'title': title,
               'links': links,
               }
    return render(request, "mainapp/index.html", content)


def library(request):
    pass


def bookshelf(request):
    pass


def profile(request):
    pass
