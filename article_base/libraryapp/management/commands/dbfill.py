from django.core.management.base import BaseCommand
from libraryapp.models import Sources
import json


with open('static/json/sources.json', 'r', encoding='cp1251') as json_source:
    sources = json.load(json_source)['sources']


class Command(BaseCommand):
    def handle(self, *args, **options):
        Sources.objects.all().delete()
        for source in sources:
            new_source = Sources(source=source)
            new_source.save()
