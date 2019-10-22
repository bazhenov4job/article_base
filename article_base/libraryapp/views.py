from django.shortcuts import render
import json
# Create your views here.

with open('static/json/links.json', 'r', encoding="UTF-8") as read_file:
    links = json.load(read_file)['links']


def load_themes():
    with open('static/json/themes.json', 'r', encoding='cp1251') as themes_json:
        themes = json.load(themes_json)['themes']
        return themes


def library(request):
    title = 'Библиотека'
    themes = load_themes()
    sources = ['iepc',
               'phys of plasmas',
               'prop and power',
               ]
    content = {'title': title,
               'themes': themes,
               'sources': sources,
               'links': links,
               }
    return render(request, "libraryapp/library.html", content)
