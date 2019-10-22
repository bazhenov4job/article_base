from django.db import models
from libraryapp.views import load_themes

# Create your models here.


class Themes(models.Model):
    themes = load_themes()
    for theme in themes:
        locals()[theme] = models.BooleanField(verbose_name=themes[theme], default=False)


class Sources(models.Model):
    source = models.CharField(verbose_name="Источники", max_length=64, unique=True)


class Authors(models.Model):
    for i in range(1, 11):
        author_x = "Автор " + "i"
        locals()['author_' + 'i'] = models.CharField(verbose_name=author_x, max_length=64, blank=True)


class References(models.Model):
    for i in range(1, 201):
        reference_x = "Ссылка " + 'i'
        locals()['reference_' + 'i'] = models.CharField(verbose_name=reference_x, max_length=256, blank=True)


class Article(models.Model):
    author_id = models.ForeignKey(Authors, on_delete=models.SET_NULL)
    title = models.CharField(verbose_name="Название статьи", max_length=256, unique=True)
    year = models.PositiveSmallIntegerField(verbose_name="Год написания")
    theme_id = models.ForeignKey(Themes, on_delete=models.SET_NULL)

    def generate_quote_link(self):
        pass
        # return quote_link

    doi = models.CharField(max_length=64, unique=True)
    source_id = models.ForeignKey(Sources)
    abstract = models.CharField(verbose_name="Abstract", max_length=1024, blank=True, unique=True)
    reference_id = models.ForeignKey(References, on_delete=models.SET_NULL, blank=False)
    disk_space_link = models.CharField(verbose_name="Ссылка на дисковое пространство", unique=True, blank=False)
    ours = models.BooleanField(verbose_name="Публикация KeRC", blank=False)
    updated = models.DateField(verbose_name="Дата добавления", auto_now=True)
