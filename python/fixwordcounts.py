import ghlca
# Changes the _id from a random to the word  in the wordcount collumns
def fixcoll(coll):
    print(coll.name)
    for word in coll.find():
        oldid = word["_id"]
        word["_id"] = word["w"]
        coll.save(word)
        coll.remove(oldid)

def fixwordcounts(colls):
    for coll in colls:
        fixcoll(coll)

fixwordcounts(ghlca.langschars)
fixwordcounts(ghlca.langswords)
fixwordcounts(ghlca.langswhites)
totalprefix = "wordcounts_wtch_7_total_"
totchar = totalprefix + "char"
totword = totalprefix + "word"
totwhite = totalprefix + "whitte"

tchar = ghlca.db[totchar]
tword = ghlca.db[totword]
twhite = ghlca.db[totwhite]


fixcoll(tchar)
fixcoll(tword)
fixcoll(twhite)
