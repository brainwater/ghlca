import ghlca

def getwordcountforcoll(coll):
    return Counter({item["w"]: item["c"] for item in coll.find()})

wctotchar = getwordcountforcoll(ghlca.db.wordcounts_wtch_total_char)
print(wctotchar.most_common())


