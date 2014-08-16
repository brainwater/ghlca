import ghlca
from pathlib import Path
import re
import sys
import json
import subprocess


flistfile = "/tmp/ghlca-file-list.txt"
infofile = "/tmp/ghlca-lang-info.txt"

def popfilenames(coll, fdir):
    for repo in coll.find():
        if "repository_full_name" not in repo:
            continue
        reponame = repo["repository_full_name"]
        print(reponame)
        repo["repository_file_list"] = getrepofileinfos(reponame, fdir)
        coll.save(repo)

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
popfilenames(ghlca.wcoll, ghlca.wfilesdir)

