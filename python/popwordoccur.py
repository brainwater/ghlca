import ghlca

totalprefix = "wordcounts_wtch_7_total_"
totchar = totalprefix + "char"
totword = totalprefix + "word"
totwhite = totalprefix + "white"

tchar = ghlca.db[totchar]
tword = ghlca.db[totword]
twhite = ghlca.db[totwhite]

langs = ghlca.db["languages"]

alllang = langs.find_one({"_id": "All Languages"})

tcchar = alllang["charcount"]
tcword = alllang["wordcount"]
tcwhite = alllang["whitecount"]
tcfile = alllang["filecount"]
tcsloc = alllang["sloc"]
tcloc = alllang["loc"]

def poplangratio():
    for lang in langs.find():
        if lang["_id"] == "All Languages":
            continue
        language = lang["language"]
        lcchar = lang["charcount"]
        lcword = lang["wordcount"]
        lcwhite = lang["whitecount"]
        lcfile = lang["filecount"]
        lcsloc = lang["sloc"]
        lcloc = lang["loc"]

        lrchar = float(lcchar) / float(tcchar)
        lrword = float(lcword) / float(tcword)
        lrwhite = float(lcwhite) / float(tcwhite)
        lrfile = float(lcfile) / float(tcfile)
        lrsloc = float(lcsloc) / float(tcsloc)
        lrloc = float(lcloc) / float(tcloc)

        lang["char_ratio"] = lrchar
        lang["word_ratio"] = lrword
        lang["white_ratio"] = lrwhite
        lang["file_ratio"] = lrfile
        lang["sloc_ratio"] = lrsloc
        lang["loc_ratio"] = lrloc

        langs.save(lang)

# Populates the word ratios under "r" in the entries of wordcoll, by comparing them against the entries in totcoll
def popwordratio(wordcoll, totcoll):
    print(wordcoll.name)
    for word in wordcoll.find():
        wc = word["c"]
        tw = totcoll.find_one({ "_id": word["w"]})
        if tw == None:
            print("Unable to find word " + word["w"])


for coll in ghlca.langschars:
    popwordratio(coll, tchar)
    break
#for coll in ghlca.langswords:
#    popwordratio(coll, tword)
#for coll in ghlca.langswhites:
#    popwordratio(coll, twhite)

