import ghlca
from pathlib import Path
import re


def popfilenames(coll):
    return None
#    for repo in coll.find():

def poprepofilenames(reponame, fdir):
    globber = reponame + "/**/*"
    paths = Path(fdir + "/").glob(globber)
    for path in paths:
        if path.is_file():
            print(path)

poprepofilenames("apache/cassandra", ghlca.wfilesdir)

