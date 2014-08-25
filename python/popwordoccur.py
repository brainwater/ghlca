import ghlca

#totalprefix = "wordcounts_wtch_7_total_"
#totchar = totalprefix + "char"
#totword = totalprefix + "word"
#totwhite = totalprefix + "white"

#tchar = ghlca.db[totchar]
#tword = ghlca.db[totword]
#twhite = ghlca.db[totwhite]

langs = ghlca.db["languages"]

#alllang = langs.find_one({"_id": "All Languages 2"})
alllang = ghlca.totalinfo

tcchar = alllang["charcount"]
tcword = alllang["wordcount"]
tcwhite = alllang["whitecount"]
tcfile = alllang["filecount"]
tcsloc = alllang["sloc"]
tcloc = alllang["loc"]

def poplangratio():
    for lang in ghlca.langsinfo:
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

# Populates the word ratios under "r" in the entries of wordcoll, by comparing them against the lang info
def popwordratio(wordcoll, count):
    print(wordcoll.name)
    for word in wordcoll.find():
        wc = word["c"]
        if len(word["_id"]) > 1024 or len(word["w"]) > 1024:
            print("Skipping superlong key")
            continue
        wr = float(wc) / float(count)
        word["r"] = wr
        wordcoll.save(word)

# Needs the "r" to be populated already
def popwordratiototal(wordcoll, totcoll):
    print(wordcoll.name)
    for word in wordcoll.find():
        if len(word["_id"]) > 1024 or len(word["w"]) > 1024:
            print("Skipping superlong key")
            continue
        if "r" not in word:
            print("No ratio found")
            continue
        wr = word["r"]
        totword = totcoll.find_one({ "_id": word["w"] })
        if None == totword:
            continue
        if "r" not in totword:
            print("No ratio found in total")
            continue
        totalratio = totword["r"]
        tr = float(wr) / float(totalratio)
        word["tr"] = tr
        wordcoll.save(word)
        


# "r" is the ratio of the occurrence to the total number for that language
# "tr" is the ratio of the "r" of that to the "r" of all of the languages for that word
def popratios():
    #popwordratio(ghlca.totalchars, ghlca.totalinfo["charcount"])
    #popwordratio(ghlca.totalwords, ghlca.totalinfo["wordcount"])
    #popwordratio(ghlca.totalwhites, ghlca.totalinfo["whitecount"])
    for langinfo in ghlca.langsinfo:
        lang = langinfo["language"]
        print(lang)
        lchars = ghlca.getlangchars(lang)
        lwords = ghlca.getlangwords(lang)
        lwhites = ghlca.getlangwhites(lang)
        popwordratio(lchars, langinfo["charcount"])
        popwordratio(lwords, langinfo["wordcount"])
        popwordratio(lwhites, langinfo["whitecount"])
        popwordratiototal(lchars, ghlca.totalchars)
        popwordratiototal(lwords, ghlca.totalwords)
        popwordratiototal(lwhites, ghlca.totalwhites)

poplangratio()
popratios()


#for coll in ghlca.langschars:
#    popwordratio(coll, ghlca.totalchars)
#for coll in ghlca.langswords:
#    popwordratio(coll, tword)
#for coll in ghlca.langswhites:
#    popwordratio(coll, twhite)

