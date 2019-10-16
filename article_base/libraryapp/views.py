from django.shortcuts import render

# Create your views here.


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
               }
    return render(request, "libraryapp/library.html", content)
