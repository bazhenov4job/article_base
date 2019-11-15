from django.shortcuts import render
from libraryapp import views
from .models import Bookshelf
from libraryapp.models import Sources, Article, Themes
from django.shortcuts import get_object_or_404

# Create your views here.


def bookshelf(request):
    title = 'Книжная полка'
    links = views.load_links()
    themes = views.load_themes()
    sources = Sources.objects.all()
    articles_id = []
    user_articles = Bookshelf.objects.filter(user=request.user)
    for user_article in user_articles:
        articles_id.append(user_article.article.id)
    articles = Article.objects.filter(id__in=articles_id)
    if request.method == "POST":
        articles = views.filter_articles(articles, request)
    content = {'title': title,
               'themes': themes,
               'sources': sources,
               'links': links,
               'articles': articles,
               }

    return render(request, "shelfapp/library.html", content)


def article(request, pk=None):
    article_pk = get_object_or_404(Article, pk=pk)
    links = views.load_links()
    content = {'links': links,
               'article': article_pk,
               }

    return render(request, "shelfapp/article.html", content)
