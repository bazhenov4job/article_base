from django.contrib import admin
from .models import Themes, Sources, Authors, References, Article
# Register your models here.
admin.site.register(Themes)
admin.site.register(Sources)
admin.site.register(Authors)
admin.site.register(References)
admin.site.register(Article)
