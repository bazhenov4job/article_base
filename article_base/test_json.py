import json


with open('themes.txt', 'r', encoding='UTF-8') as themes_file:
    themes = {"themes": themes_file.read().split('\n')}

print(themes)

with open('static/json/themes.json', 'w', encoding='cp1251') as jthemes:
    json.dump(themes, jthemes, ensure_ascii=False, indent=4)
