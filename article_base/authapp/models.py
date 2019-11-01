from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Scientist(AbstractUser):
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.first_name + ', ' + self.position

    position = models.CharField(verbose_name="Должность", max_length=100, blank=True, unique=False)
