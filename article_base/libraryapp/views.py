from django.shortcuts import render, HttpResponseRedirect
from django.conf import settings
from .models import Sources, Themes, Article, Authors, References
from .forms import ArticleCreationForm, AuthorCreationForm, ThemeCreationForm, SourceCreationForm, ReferenceCreationForm
from shelfapp.models import Bookshelf
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json
from django.urls import reverse
from django.core.paginator import Paginator
import os
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.


def load_links():
    with open('static/json/links.json', 'r', encoding="UTF-8") as read_file:
        links = json.load(read_file)['links']
        return links


def load_themes():
    with open('static/json/themes.json', 'r', encoding='cp1251') as themes_json:
        themes = json.load(themes_json)['themes']
        return themes


def load_sources():
    with open('static/json/sources.json', 'r', encoding='cp1251') as sources_json:
        sources = json.load(sources_json)['sources']
        return sources


themes = load_themes()
sources = Sources.objects.all()
links = load_links()


def filter_articles(articles, request):

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

        print(request, request.POST, request_themes_id, request_sources_id)

        if len(request_authors) != 0:
            request_dict['author__id__in'] = request_authors
        if len(request_themes_id) != 0:
            request_dict['theme__id__in'] = request_themes_id
        if len(request_sources_id) != 0:
            request_dict['source__id__in'] = request_sources_id

        if len(request_authors) == 0 and len(request_themes_id) == 0 and \
           len(request_sources_id) == 0 and request.POST['title'] == ''and \
           request.POST['doi'] == '' and request.POST['year'] == '':
            return []
        else:
            return Article.objects.filter(**request_dict)
    else:
        return Article.objects.all()


def library(request, page=1):
    title = 'Библиотека'
    articles = Article.objects.all()

    articles = filter_articles(articles, request)

    paginator = Paginator(articles, 4)
    try:
        page_articles = paginator.page(page)
    except PageNotAnInteger:
        page_articles = paginator.page(1)
    except EmptyPage:
        page_articles = paginator.page(paginator.num_pages)

    content = {'title': title,
               'themes': themes,
               'sources': sources,
               'links': links,
               'articles': page_articles,
               }
    return render(request, "libraryapp/library.html", content)


class ArticleView(ListView):
    model = Article
    template_name = 'libraryapp/list_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['stuff'] = 'some_stuff'
        return context


class CreateArticle(CreateView):
    model = Article
    template_name = 'libraryapp/create_article.html'
    success_url = reverse_lazy('libraryapp:index')
    form_class = ArticleCreationForm

    def __init__(self):
        self.author_id = 0
        self.theme_id = 0
        self.ref_id = 0

    def get(self, request, *args, **kwargs):
        self.author_id = self.kwargs['author_id']
        self.theme_id = self.kwargs['theme_id']
        self.ref_id = self.kwargs['ref_id']
        self.initial['author'] = Authors.objects.get(pk=self.author_id)
        self.initial['theme'] = Themes.objects.get(pk=self.theme_id)
        self.initial['reference'] = References.objects.get(pk=self.ref_id)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateArticle, self).get_context_data(**kwargs)
        context["action_url"] = 'libraryapp:create_article'
        context["author_id"] = self.author_id
        context["theme_id"] = self.theme_id
        context["ref_id"] = self.ref_id
        return context


class CreateAuthor(CreateView):
    model = Authors
    template_name = 'libraryapp/create_author.html'
    success_url = reverse_lazy('libraryapp:index')
    form_class = AuthorCreationForm

    def get_context_data(self, **kwargs):
        context = super(CreateAuthor, self).get_context_data(**kwargs)
        context["action_url"] = 'libraryapp:create_author'
        return context

    def form_valid(self, form):
        instance = form.save()
        author_id = instance.id
        print(author_id)
        return HttpResponseRedirect(reverse('libraryapp:create_theme', kwargs={'author_id': author_id}))


class CreateTheme(CreateView):
    model = Themes
    template_name = 'libraryapp/create_theme.html'
    form_class = ThemeCreationForm
    author_id = 0

    def get(self, request, *args, **kwargs):
        self.author_id = self.kwargs['author_id']
        print(str(self.author_id) + "Метод гет")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.author_id = self.kwargs['author_id']
        return super().post(request, *args, *kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_url'] = 'libraryapp:create_theme'
        context['author_id'] = self.author_id
        return context

    def form_valid(self, form):
        instance = form.save()
        print(instance.id)
        print(str(self.author_id) + "метод форм валид")
        kwargs = {'author_id': self.author_id,
                  'theme_id': instance.id}
        return HttpResponseRedirect(reverse('libraryapp:create_ref', kwargs=kwargs))


class CreateRef(CreateView):
    model = References
    template_name = 'libraryapp/create_ref.html'
    form_class = ReferenceCreationForm

    def __init__(self, *args, **kwargs):
        super(CreateRef, self).__init__(*args, **kwargs)
        self.author_id = ''
        self.theme_id = ''

    def get(self, request, *args, **kwargs):
        self.author_id = self.kwargs['author_id']
        self.theme_id = self.kwargs['theme_id']
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.author_id = self.kwargs['author_id']
        self.theme_id = self.kwargs['theme_id']
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_url'] = 'libraryapp:create_ref'
        context['author_id'] = self.author_id
        context['theme_id'] = self.theme_id
        return context

    def form_valid(self, form):
        instance = form.save()
        print(instance.id)
        kwargs = {'author_id': self.author_id,
                  'theme_id': self.theme_id,
                  'ref_id': instance.id}
        return HttpResponseRedirect(reverse('libraryapp:create_article', kwargs=kwargs))



def article(request, pk=None):
    article_pk = get_object_or_404(Article, pk=pk)
    links = load_links()
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

