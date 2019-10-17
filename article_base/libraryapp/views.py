from django.shortcuts import render
import json
# Create your views here.

with open('static/json/links.json', 'r', encoding="UTF-8") as read_file:
    links = json.load(read_file)['links']


def library(request):
    title = 'Библиотека'
    themes = ['ХД',
              'ИД',
              'МПД',
              'ELF',
              'VASIMR',
              ]
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
