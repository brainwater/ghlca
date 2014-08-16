import ghlca
from pathlib import Path
from collections import Counter
import hashlib
import re

wcounter = Counter()
scount = Counter()
ccount = Counter()
filehashes = []

def wcofrepo(reponame, fdir):
    print(reponame)
    globber = reponame + "/**/*.java"
    #print(globber)
    paths = Path(fdir + "/").glob(globber)
    #Path(fdir + "/").glob(reponame + '/**')
    #print(list(paths))
    #print(list(paths))

    try:
        for path in paths:
            #print(path)
            if not str(path).endswith(".java"):
                continue
            f = open(str(path), encoding="utf-8")
            fstr = f.read()
            hs = hashlib.md5(fstr.encode(encoding="utf-8")).hexdigest()
            #print(path)
            filehashes.append(hs)
            ccount.update(fstr)
            wcounter.update(re.split("[\W]+", fstr))
            scount.update(fstr.split())
            #print(wcounter.most_common(100))

            f.close()
    except:
        print("Exception")
    #    for path in paths:
    #        f = open(path)

def totalwc(coll, fdir):
    for repo in coll.find():
        if 'repository_full_name' in repo:
            reponame = repo['repository_full_name']
            wcofrepo(reponame, fdir)
                
totalwc(ghlca.wcoll, ghlca.wfilesdir)
#wcofrepo("apache/cassandra", ghlca.wfilesdir)

print(wcounter.most_common(100))
print(scount.most_common(100))
print(Counter(filehashes).most_common(50))
mc = ccount.most_common(100)
for i in mc:
    try:
        print(i)
    except:
        pass

# wcofrepo(, ghlca.wfilesdir)
