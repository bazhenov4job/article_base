from django.db import models
import json


# Create your models here.

def load_themes():
    with open('static/json/themes.json', 'r', encoding='cp1251') as themes_json:
        themes = json.load(themes_json)['themes']
        return themes


class Themes(models.Model):
    themes = load_themes()

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    def __str__(self):
        return ', '.join(self.get_list)

    @property
    def get_list(self):
        theme_list = []
        themes = load_themes()
        for key in self.__dict__.keys():
            if self.__dict__[key] and key in themes:
                theme_list.append(themes[key])
        return theme_list

    for theme in themes:
        locals()[theme] = models.BooleanField(verbose_name=themes[theme], default=False)


class Sources(models.Model):
    class Meta:
        verbose_name = "Источник"
        verbose_name_plural = "Источники"

    def __str__(self):
        return self.source

    source = models.CharField(verbose_name="Источники", max_length=64, unique=True)


class Authors(models.Model):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return ', '.join(self.get_list)

    @property
    def get_list(self):
        author_list = []
        for key in self.__dict__.keys():
            if 'author' in key and self.__dict__[key]:
                author_list.append(self.__dict__[key])
        return author_list

    for i in range(1, 11):
        author_x = "Автор " + str(i)
        locals()['author_{0:0=3}'.format(i)] = models.TextField(verbose_name=author_x, max_length=64, blank=True)


class References(models.Model):
    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"

    def __str__(self):
        return self.reference_001

    @property
    def get_list(self):
        ref_list = []
        for key in self.__dict__.keys():
            if 'reference' in key and self.__dict__[key]:
                ref_list.append(self.__dict__[key])
        return ref_list

    for i in range(1, 101):
        reference_x = "Ссылка " + str(i)
        locals()['reference_{0:0=3}'.format(i)] = models.TextField(verbose_name=reference_x, max_length=255, blank=True)


class Article(models.Model):
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title

    author = models.ForeignKey(Authors, verbose_name='Автор', on_delete=models.SET_NULL, null=True)
    title = models.CharField(verbose_name="Название статьи", max_length=255, unique=True)
    year = models.PositiveSmallIntegerField(verbose_name="Год написания")
    theme = models.ForeignKey(Themes, verbose_name='Тема', on_delete=models.SET_NULL, null=True)

    def generate_quote_link(self):
        pass
        # return quote_link

    doi = models.CharField(verbose_name='Идентификатор DOI', max_length=64, unique=True)
    source = models.ForeignKey(Sources, verbose_name='Источник', on_delete=models.SET_NULL, null=True)
    abstract = models.CharField(verbose_name="Выдержка (abstract)", max_length=255, blank=True, unique=True)
    reference = models.ForeignKey(References, verbose_name='Ссылки', on_delete=models.SET_NULL, blank=False, null=True)
    disk_space_link = models.FileField(upload_to='uploads/pdf', verbose_name="Ссылка на дисковое пространство", blank=False)
    ours = models.BooleanField(verbose_name="Публикация KeRC", blank=False)
    updated = models.DateField(verbose_name="Дата добавления", auto_now=True)
