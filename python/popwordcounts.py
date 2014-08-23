import ghlca
from utilwordcounter import WordCounter
import pymongo
import sys
import json

def wcforlang(fcoll, lang=None):
    fnamefile = open("/tmp/ghlca-file-names-pop-wordcount.txt", "w+")
    cntr = 0
    failcntr = 0
    sloccnt = 0
    loccnt = 0
    wc = WordCounter()
    for f in fcoll.find():
        if "language" not in f:
            continue
        if "vendored" in f and f["vendored"]:
            continue
        if "generated" in f and f["generated"]:
            continue
        if (not (lang == None)) and (not (f["language"] == lang)):
            continue
        if "sloc" in f:
            sloccnt += f["sloc"]
        if "loc" in f:
            loccnt += f["loc"]
        fnamefile.write(f["filename"] + "\n")
        with open(f["filename"], "r") as thefile:
            try:
                wc.update(thefile.read())
                cntr += 1
            except UnicodeDecodeError:
                print("UnicodeDedcodeError on file " + f["filename"])
                failcntr += 1
        if cntr % 10000 == 0:
            print(cntr)
    return wc, cntr, failcntr, sloccnt, loccnt



def popwordcounts(fcoll):
    langfile = open("data/language-list.json", "r")
    languages = json.load(langfile)
    for lang in languages:
        print("Language " + lang)
        wclang, fcount, failcount, sloc, loc = wcforlang(fcoll, lang)
        prefix = "wordcounts_wtch_7_lang_"
        langcollchar = pymongo.collection.Collection(ghlca.db, prefix + "char_" + lang)
        langcollword = pymongo.collection.Collection(ghlca.db, prefix + "word_" + lang)
        langcollwhite = pymongo.collection.Collection(ghlca.db, prefix + "white_" + lang)
        for word, count in wclang.charcount.most_common(10000):
            langcollchar.save({ "w": word, "c": count })
        for word, count in wclang.wordcountwordchars.most_common(10000):
            langcollword.save({ "w": word, "c": count })
        for word, count in wclang.wordcountwhitespace.most_common(10000):
            langcollwhite.save({ "w": word, "c": count })
        totchars = sum(wclang.charcount.values())
        totwords = sum(wclang.wordcountwordchars.values())
        totwhites = sum(wclang.wordcountwhitespace.values())
        ghlca.langcoll.save({"_id": lang, "language": lang, "filecount": fcount, "charcount": totchars, "wordcount": totwords, "whitecount": totwhites, "sloc": sloc, "loc": loc, "failcount": failcount})
        print("Wrote language " + lang)
    print("Starting on total")
    wc, fcount, failcount, sloc, loc = wcforlang(fcoll)
    lang = "All Languages"
    prefix = "wordcounts_wtch_7_total_"
    collchar = pymongo.collection.Collection(ghlca.db, prefix + "char")
    collword = pymongo.collection.Collection(ghlca.db, prefix + "word")
    collwhite = pymongo.collection.Collection(ghlca.db, prefix + "white")
    for word, count in wc.charcount.most_common(10000000):
        collchar.save({ "w": word, "c": count })
    for word, count in wclang.wordcountwordchars.most_common(10000000):
        collword.save({ "w": word, "c": count })
    for word, count in wclang.wordcountwhitespace.most_common(10000000):
        collwhite.save({ "w": word, "c": count })
    totchars = sum(wc.charcount.values())
    totwords = sum(wc.wordcountwordchars.values())
    totwhites = sum(wc.wordcountwhitespace.values())
    ghlca.langcoll.save({"_id": lang, "language": lang, "filecount": fcount, "charcount": totchars, "wordcount": totwords, "whitecount": totwhites, "sloc": sloc, "loc": loc, "failcount": failcount})
    print("Done with total")


popwordcounts(ghlca.wfcoll)
#wtot, w = getwordcounts(ghlca.wfcoll)

#totals = { "wordcounts": wtot }
#ghlca.wwccoll.save(totals)

#for i, j in w:
#    ghlca.wwcoll.save({ "language": i, "wordcounts": j })
#tot = dict(wtot)
#ghlca.wwccoll.save(tot)
#for i, j in w:
    
#ghlca.wwccoll

#print(type(w))

#print(wtot.wordcountwhitespace.most_common())
#print(wtot.wordcountwordchars.most_common())
#print(wtot.charcount.most_common())

#for i, j in w.items():
#    print(i)
#    print(j.wordcountwhitespace.most_common())
#    print(j.wordcountwordchars.most_common())
#    print(j.charcount.most_common())
