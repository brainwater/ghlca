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
print("a")
db = mongoclient.ghlca
print("b")
# Collection of repositories with the maximum number of watchers
wcoll = db["max-watchers-repos"]
print("c")
# Repositories with the maximum number of forks
fcoll = db["max-forks-repos"]
print("d")
datadir = "~/data/ghlca/repos/wtch"
print("e")
filesdir = path.expanduser('~/data/ghlca/files')
print("f")
wfilesdir = filesdir + '/wtch'
print("g")
ffilesdir = filesdir + '/fork'
print("h")
#repospathstr=path.expanduser('~/data/ghlca-repos')
#reposp = Path(repospathstr)
#repoabspaths =list(reposp.glob('**/*.git'))
#relamap = lambda x: x.relative_to(reposp)
#strmap = lambda x: str(relamap(x))
#repos = [{"repo": strmap(i), "abspath": i, "relapath": relamap(i)} for i in repoabspaths]
#tmpfilename='/tmp/ghlca-' + ''.join(random.choice(string.ascii_lowercase) for _ in range(16))

