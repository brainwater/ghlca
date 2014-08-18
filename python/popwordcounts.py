import ghlca
from utilwordcounter import WordCounter


def getwordcounts(fcoll):
    wctot = WordCounter()
    wc = {}
    cntr = 0
    for f in fcoll.find():
        if "language" not in f:
            continue
        if "vendored" in f and f["vendored"]:
            continue
        if "generated" in f and f["generated"]:
            continue
        if f["language"] not in wc:
            wc[f["language"]] = WordCounter()
        with open(f["filename"], "r") as thefile:
            try:
                text = thefile.read()
                wctot.update(text)
                wc[f["language"]].update(text)
            except:
                print("Error on file " + f["filename"])
        if cntr % 1000 == 0:
            print(cntr)
        cntr += 1
    return wctot, wc

wtot, w = getwordcounts(ghlca.wfcoll)

totals = { "wordcounts": wtot }
ghlca.wwccol.save(totals)

for i, j in w:
    ghlca.wwcol.save({ "language": i, "wordcounts": j })
#tot = dict(wtot)
#ghlca.wwccoll.save(tot)
#for i, j in w:
    
#ghlca.wwccoll

#print(type(w))

print(wtot.wordcountwhitespace.most_common())
print(wtot.wordcountwordchars.most_common())
print(wtot.charcount.most_common())

for i, j in w.items():
    print(i)
    print(j.wordcountwhitespace.most_common())
    print(j.wordcountwordchars.most_common())
    print(j.charcount.most_common())
