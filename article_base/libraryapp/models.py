from django.db import models
from .views import load_themes

# Create your models here.


class Themes(models.Model):
    themes = load_themes()
    for theme in themes:
        locals()[theme] = models.BooleanField(verbose_name=themes[theme], default=False)


class Sources(models.Model):
    source = models.CharField(verbose_name="Источники", max_length=64, unique=True)


class Authors(models.Model):
    for i in range(1, 11):
        author_x = "Автор " + str(i)
        locals()['author_{0:0=3}'.format(i)] = models.TextField(verbose_name=author_x, max_length=64, blank=True)


class References(models.Model):
    for i in range(1, 101):
        reference_x = "Ссылка " + str(i)
        locals()['reference_{0:0=3}'.format(i)] = models.TextField(verbose_name=reference_x, max_length=255, blank=True)


class Article(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.SET_NULL, null=True)
    title = models.CharField(verbose_name="Название статьи", max_length=255, unique=True)
    year = models.PositiveSmallIntegerField(verbose_name="Год написания")
    theme = models.ForeignKey(Themes, on_delete=models.SET_NULL, null=True)

    def generate_quote_link(self):
        pass
        # return quote_link

    doi = models.CharField(max_length=64, unique=True)
    source = models.ForeignKey(Sources, on_delete=models.SET_NULL, null=True)
    abstract = models.CharField(verbose_name="Abstract", max_length=255, blank=True, unique=True)
    reference = models.ForeignKey(References, on_delete=models.SET_NULL, blank=False, null=True)
    disk_space_link = models.CharField(verbose_name="Ссылка на дисковое пространство", max_length=255, unique=True, blank=False)
    ours = models.BooleanField(verbose_name="Публикация KeRC", blank=False)
    updated = models.DateField(verbose_name="Дата добавления", auto_now=True)
