import ghlca.py
from pathlib import Path
from collections import Counter

def wcofrepo(reponame, fdir):
    paths = Path.glob(fdir + '/' + reponame + '.git/**')
    print(paths)
#    for path in paths:
#        f = open(path)

def totalwc(coll, fdir):
    return None
    #for repo in coll.find():
    #if 'repository_full_name' in repo:
    #        reponame = repo['repository_full_name']
    #        paths = Path.glob(fdir + '/**')
                
wcofrepo('adris9/jStorage', ghlca.wfilesdir)
