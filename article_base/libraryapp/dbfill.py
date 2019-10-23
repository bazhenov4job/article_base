from .models import Article, Authors, References, Sources, Themes
import json

with open('static/json/sources.json', 'r', encoding='cp1251') as json_source:
    sources = json.load(json_source)['sources']

for source in sources:
    new_source = Sources(source=source)
    new_source.save()
