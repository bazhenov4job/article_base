import json


with open('sources.txt', 'r', encoding='UTF-8') as sources_file:
    sources = {"sources": sources_file.read().split('\n')}

print(sources)

with open('static/json/sources.json', 'w', encoding='cp1251') as jsources:
    json.dump(sources, jsources, ensure_ascii=False, indent=4)
