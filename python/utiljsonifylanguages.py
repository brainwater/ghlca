import json

langsfile = open("data/language-list.txt", "r")
langs = []
for lang in langsfile:
    langs.append(lang.rstrip("\n"))
langsjson = open("data/language-list.json", "w+")
json.dump(langs, langsjson)

