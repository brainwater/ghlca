import ghlca
from utilwordcounter import WordCounter
import pymongo
import sys
import json

def wcforlang(fcoll, lang=None):
    cntr = 0
    wc = WordCounter()
    for f in fcoll.find():
        if "language" not in f:
            continue
        if "vendored" in f and f["vendored"]:
            continue
        if "generated" in f and f["generated"]:
            continue
        if lang == None or not f["language"] == lang:
            continue
        fnamefile.write(f["filename"] + "\n")
        cntr += 1
        with open(f["filename"], "r") as thefile:
            try:
                wc.update(thefile.read())
            except UnicodeDecodeError:
                print("UnicodeDedcodeError on file " + f["filename"])
        if cntr % 10000 == 0:
            print(cntr)
    return wc, cntr



def getwordcounts(fcoll):
    #fnamefile = open("/tmp/ghlca-file-names-pop-wordcount.txt", "w+")
    langfile = open("data/language-list.json", "r")
    languages = json.load(langfile)
    for lang in languages:
        print("Language " + lang)
        wclang, fcount = wcforlang(fcoll, lang)
        prefix = "wordcounts_wtch_2_lang_"
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
        totwhites = sum(wclang.wordcountwordchars.values())
        ghlca.langcoll.save({"_id": lang, "language": lang, "filecount": fcount, "charcount": totchars, "wordcount": totwords, "whitecount": totwhites})
        print("Wrote language " + lang)
    print("Starting on total")
    wc, fcount = wcforlang(fcoll)
    prefix = "wordcounts_total_2_"
    collchar = pymongo.collection.Collection(ghlca.db, prefix + "char")
    collword = pymongo.collection.Collection(ghlca.db, prefix + "word")
    collwhite = pymongo.collection.Collection(ghlca.db, prefix + "white")
    for word, count in wclang.charcount.most_common(100000):
        collchar.save({ "w": word, "c": count })
    for word, count in wclang.wordcountwordchars.most_common(100000):
        collword.save({ "w": word, "c": count })
    for word, count in wclang.wordcountwhitespace.most_common(100000):
        collwhite.save({ "w": word, "c": count })
    print("Done with total")
    
    
            
            
            
    for f in fcoll.find():
        if "language" not in f:
            continue
        if "vendored" in f and f["vendored"]:
            continue
        if "generated" in f and f["generated"]:
            continue
        fnamefile.write(f["filename"] + "\n")
        if f["language"] not in wc:
            wc[f["language"]] = WordCounter()
        with open(f["filename"], "r") as thefile:
            try:
                text = thefile.read()
                wctot.update(text)
                wc[f["language"]].update(text)
            except UnicodeDecodeError:
                print("UnicodeDedcodeError on file " + f["filename"])
        if cntr % 1000 == 0:
            print(cntr)
            sys.stdout.flush()
        cntr += 1
    return wctot, wc

def popwordcounts(fcoll):
    wctotals, wordcounts = getwordcounts(fcoll)
    print("Done calculating, storing")
    for lang, wordcount in wordcounts.items():
        print("Storing language " + lang)
        
    totalcollchar = pymongo.collection.Collection(ghlca.db, "wordcounts_wtch_2_total_char")
    totalcollword = pymongo.collection.Collection(ghlca.db, "wordcounts_wtch_2_total_word")
    print("Storing whitespace delimited word counts")
    totalcollwhite = pymongo.collection.Collection(ghlca.db, "wordcounts_wtch_2_total_white")
    for word, count in wctotals.charcount.most_common(100000):
        totalcollchar.save({ "w": word, "c": count })
    print("Storing word character word counts")
    for word, count in wctotals.wordcountwordchars.most_common(100000):
        totalcollword.save({ "w": word, "c": count })
    print("Done with languages, storing chars")
    for word, count in wctotals.wordcountwhitespace.most_common(100000):
        totalcollwhite.save({ "w": word, "c": count })
    print("Done with everything")


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
