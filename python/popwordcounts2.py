import ghlca
from utilwordcounter import WordCounter
import pymongo
import sys
import json
import gc

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
            sys.stdout.flush()
    return wc, cntr, failcntr, sloccnt, loccnt



def popwordcounts(fcoll):
    langfile = open("data/language-list.json", "r")
    print("Starting on total")
    wc, fcount, failcount, sloc, loc = wcforlang(fcoll)
    print("Garbage collecting")
    sys.stdout.flush()
    gc.collect()
    print("Done garbage collecting")
    sys.stdout.flush()
    print("Saving total counts")
    sys.stdout.flush()
    lang = "All Languages 2"
    prefix = "wordcounts_wtch_10_total_"
    collchar = pymongo.collection.Collection(ghlca.db, prefix + "char")
    collword = pymongo.collection.Collection(ghlca.db, prefix + "word")
    collwhite = pymongo.collection.Collection(ghlca.db, prefix + "white")
    totchars = sum(wc.charcount.values())
    totwords = sum(wc.wordcountwordchars.values())
    totwhites = sum(wc.wordcountwhitespace.values())
    ghlca.langcoll.save({"_id": lang, "language": lang, "filecount": fcount, "charcount": totchars, "wordcount": totwords, "whitecount": totwhites, "sloc": sloc, "loc": loc, "failcount": failcount})
    print("Garbage collecting")
    sys.stdout.flush()
    gc.collect()
    print("Done garbage collecting")
    sys.stdout.flush()
    print("Done with total counts, saving total chars")
    sys.stdout.flush()
    for word, count in wc.charcount.most_common(1000000):
        collchar.save({ "_id": word, "w": word, "c": count })
    print("Garbage collecting")
    sys.stdout.flush()
    gc.collect()
    print("Done garbage collecting")
    sys.stdout.flush()
    print("Saving total words")
    sys.stdout.flush()
    for word, count in wc.wordcountwordchars.most_common(2000000):
        collword.save({ "_id": word, "w": word, "c": count })
    print("Garbage collecting")
    sys.stdout.flush()
    gc.collect()
    print("Done garbage collecting")
    sys.stdout.flush()
    print("Saving total whites")
    sys.stdout.flush()
    for word, count in wc.wordcountwhitespace.most_common(2000000):
        collwhite.save({ "_id": word, "w": word, "c": count })
    print("Done with total whites")
    sys.stdout.flush()
    print("Done with total")
    sys.stdout.flush()


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
