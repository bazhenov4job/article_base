from django.shortcuts import render, HttpResponseRedirect
from django.conf import settings
from .models import Sources, Themes, Article, Authors
from shelfapp.models import Bookshelf
from django.shortcuts import get_object_or_404
from django.http import FileResponse, HttpResponse
import json
from django.urls import reverse
import os
# Create your views here.

with open('static/json/links.json', 'r', encoding="UTF-8") as read_file:
    links = json.load(read_file)['links']


def load_themes():
    with open('static/json/themes.json', 'r', encoding='cp1251') as themes_json:
        themes = json.load(themes_json)['themes']
        return themes


def load_sources():
    with open('static/json/sources.json', 'r', encoding='cp1251') as sources_json:
        sources = json.load(sources_json)['sources']
        return sources


def library(request):
    title = 'Библиотека'
    themes = load_themes()
    sources = Sources.objects.all()

    if request.method == 'POST':
        request_themes = {}
        request_sources = []
        request_dict = {}
        request_possible = ["title",
                            "doi",
                            "year__gte",
                            "year__lte",
                            "ours"
                            ]
        request_authors = []
        request_themes_id = []
        request_sources_id = []

        for key in request.POST:
            if key in themes:
                request_themes[key] = True
            elif key in request_possible and request.POST[key] != '':
                request_dict[key] = request.POST[key]
            for source in sources:
                if key in source.source:
                    request_sources.append(key)

        for theme in Themes.objects.filter(**request_themes):
            request_themes_id.append(theme.id)

        for author in Authors.objects.all():
            if request.POST['author'] in author.get_list:
                request_authors.append(author.id)

        for source in request_sources:
            request_sources_id.append(Sources.objects.filter(source=source)[0].id)

        print(request.POST, request_themes_id, request_sources_id)

        if len(request_authors) != 0:
            request_dict['author__id__in'] = request_authors
        if len(request_themes_id) != 0:
            request_dict['theme__id__in'] = request_themes_id
        if len(request_sources_id) != 0:
            request_dict['source__id__in'] = request_sources_id

        if len(request_authors) == 0 and len(request_themes_id) == 0 and \
           len(request_sources_id) == 0 and request.POST['title'] == ''and \
           request.POST['doi'] == '' and request.POST['year'] == '':
            articles = []
        else:
            articles = Article.objects.filter(**request_dict)
    else:
        articles = Article.objects.all()

    content = {'title': title,
               'themes': themes,
               'sources': sources,
               'links': links,
               'articles': articles,
               }
    return render(request, "libraryapp/library.html", content)


def article(request, pk=None):
    article_pk = get_object_or_404(Article, pk=pk)
    content = {'links': links,
               'article': article_pk,
               }

    return render(request, "libraryapp/article.html", content)


def add_shelf(request, pk=None):
    request_user = request.user
    request_article = Article.objects.get(pk=pk)
    new_shelf_article = Bookshelf(user=request_user, article=request_article)
    new_shelf_article.save()
    return HttpResponseRedirect(reverse('library:index'))


def open_pdf(request, pk=None):
    file_path = os.path.normpath(str(Article.objects.filter(pk=pk)[0].disk_space_link))
    file_path = os.path.join(settings.MEDIA_ROOT, file_path)
    with open(file_path, 'rb') as pdf:
        file_name = file_path[(file_path.rfind('\\') + 1): file_path.rfind('.')]
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        # response['Content-Disposition'] = 'file_name={}'.format(file_name)
        return response
