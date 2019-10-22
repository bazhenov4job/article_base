from django.db import models
from libraryapp.views import load_themes

# Create your models here.


class Themes(models.Model):
    themes = load_themes()
    for theme in themes:
        locals()[theme] = models.BooleanField(verbose_name=themes[theme], default=False)


class Sources(models.Model):
    source = models.CharField(verbose_name="Источники", max_length=64, unique=True)
