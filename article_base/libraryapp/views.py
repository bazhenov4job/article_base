from django.shortcuts import render
from libraryapp.models import Sources, Themes, Article
from django.shortcuts import get_object_or_404
import json
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
