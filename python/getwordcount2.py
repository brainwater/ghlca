import ghlca
from collections import Counter

def getwordcountforcoll(coll):
    return Counter({item["w"]: item["c"] for item in coll.find()})

#print(ghlca.db.collection_names())
#for i in ghlca.db:
#    print(i)
wctotchar = getwordcountforcoll(ghlca.db.wordcounts_wtch_4_lang_char_Haskell)
print(wctotchar.most_common(100))
wctotchar = getwordcountforcoll(ghlca.db["wordcounts_wtch_4_total_char"])
print(wctotchar.most_common(100))
#wctotword = getwordcountforcoll(ghlca.db.wordcounts_wtch_total_word)
#print(wctotword.most_common(100))
#wctotwhite = getwordcountforcoll(ghlca.db.wordcounts_wtch_total_white)
#print(wctotwhite.most_common(100))


