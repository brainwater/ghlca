import subprocess as sp
import string
import random
from os import path
from pathlib import Path
#import settings
#import github3 as gh3
import pymongo as pm
import random

#gh = gh3.login(token=settings.github_api_token)

mongoclient = pm.MongoClient('localhost', 27017)
db = mongoclient.ghlca
# List of files collection
wfcoll = pm.collection.Collection(db, "files-wtch")
langcoll = pm.collection.Collection(db, "languages")
#wwccoll = pm.collection.Collection(db, "wtchwordcounts")
wwccoll = pm.collection.Collection(db, "wtchwordcountsnogenven")
# Collection of repositories with the maximum number of watchers
wcoll = db["max-watchers-repos"]
# Repositories with the maximum number of forks
fcoll = db["max-forks-repos"]
datadir = path.expanduser("~/data/ghlca/repos/wtch")
filesdir = path.expanduser('~/data/ghlca/files')
wfilesdir = filesdir + '/wtch'
ffilesdir = filesdir + '/fork'

# Language specific collections
langcoll = db.languages

langprefix = "wordcounts_wtch_7_lang_"
langcharprefix = langprefix + "char_"
langwordprefix = langprefix + "word_"
langwhiteprefix = langprefix + "white_"

def testifall(lang):
    return (not (lang == "All Languages")) and (not (lang == "All Languages 2"))

langschars = [db[langcharprefix + lang["language"]] for lang in langcoll.find() if testifall(lang["language"])]
langswords = [db[langwordprefix + lang["language"]] for lang in langcoll.find() if testifall(lang["language"])]
langswhites = [db[langwhiteprefix + lang["language"]] for lang in langcoll.find() if testifall(lang["language"])]

# Total words collections
totprefix = "wordcounts_wtch_9_total_"
totalchars = pm.collection.Collection(db, totprefix + "char")
totalwords = pm.collection.Collection(db, totprefix + "word")
totalwhites = pm.collection.Collection(db, totprefix + "white")


#repospathstr=path.expanduser('~/data/ghlca-repos')
#reposp = Path(repospathstr)
#repoabspaths =list(reposp.glob('**/*.git'))
#relamap = lambda x: x.relative_to(reposp)
#strmap = lambda x: str(relamap(x))
#repos = [{"repo": strmap(i), "abspath": i, "relapath": relamap(i)} for i in repoabspaths]
tmpfilename='/tmp/ghlca-' + ''.join(random.choice(string.ascii_lowercase) for _ in range(16))

