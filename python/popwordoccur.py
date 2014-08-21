import ghlca

totalprefix = "wordcounts_wtch_5_total_"
totchar = totalprefix + "char"
totword = totalprefix + "word"
totwhite = totalprefix + "whitte"

tchar = ghlca.db[totchar]
tword = ghlca.db[totword]
twhite = ghlca.db[totwhite]

langs = ghlca.db["languages"]

alllang = langs.find({"_id": "All Languages"})

tcchar = alllang["charcount"]
tcword = alllang["wordcount"]
tcwhite = alllang["whitecount"]
tcfile = alllang["filecount"]

for lang in langs.find():
    if lang["_id"] == "All Languages":
        continue
    language = lang["language"]
    lcchar = lang["charcount"]
    lcword = lang["wordcount"]
    lcwhite = lang["whitecount"]
    lcfile = lang["filecount"]

    lrchar = ((float) lcchar / (float) tcchar)
    lrword = ((float) lcword / (float) tcword)
    lrwhite = ((float) lcwhite / (float) tcwhite)
    lrfile = ((float) lcfile / (float) tcfile)
    
