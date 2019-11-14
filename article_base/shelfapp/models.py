from django.db import models
from libraryapp.models import Article
from authapp.models import Scientist

# Create your models here.


class Bookshelf(models.Model):
    user = models.ForeignKey(Scientist, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    add_datetime = models.DateTimeField(verbose_name="время", auto_now_add=True)

    class Meta:
        verbose_name = "Полка"
        verbose_name_plural = "Полки"
        unique_together = (('user', 'article'),)
