import ghlca
from pathlib import Path
import re
import sys
import json
import subprocess
import random
import string

def fgen():
    return '/tmp/ghlca-popreposfiles-' + ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

#flistfile = "/tmp/ghlca-file-list.txt"
#infofile = "/tmp/ghlca-lang-info.txt"
flistfile = fgen()
infofile = fgen()

def popfilenames(repocoll, filescoll, fdir):
    repos = list(repocoll.find())
    random.shuffle(repos)
    for repo in repos:
        if "repository_full_name" not in repo:
            continue
        reponame = repo["repository_full_name"]
        if "repository_files_populated" in repo and repo["repository_files_populated"]:
            continue
        print(reponame)
        if "repository_file_list" in repo:
            print("repository_file_list found, deleting")
            del repo["repository_file_list"]
        repofilelist = getrepofileinfos(reponame, fdir)
        for f in repofilelist:
            f["_id"] = f["filename"]
            f["reponame"] = reponame
            filescoll.save(f)
        repo["repository_files_populated"] = True
        repocoll.save(repo)

def getrepofileinfos(reponame, fdir):
    globber = reponame + "/**/*"
    paths = Path(fdir + "/").glob(globber)
    pathstrs = [str(i) for i in paths if i.is_file()]
    with open(flistfile, 'w+') as outfile:
        json.dump(pathstrs, outfile)
    subprocess.call('ruby ruby/langinfo.rb "' + flistfile + '" "' + infofile + '"', shell=True)
    finfos = []
    with open(infofile) as infile:
        finfos = json.load(infile)
    return finfos

#print(getrepofileinfos("apache/cassandra", ghlca.wfilesdir))
popfilenames(ghlca.wcoll, ghlca.wfcoll, ghlca.wfilesdir)

