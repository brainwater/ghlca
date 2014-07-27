import subprocess as sp
import string
import random
from os import path
from pathlib import Path

datadir = "~/data/ghlca-repos"
#tmppath = '/tmp/ghlca-' + ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
repospathstr=path.expanduser('~/data/ghlca-repos')
reposp = Path(repospathstr)
repoabspaths =list(reposp.glob('**/*.git'))
relamap = lambda x: x.relative_to(reposp)
strmap = lambda x: str(relamap(x))

#repopaths = list(map(lambda x: x.relative_to(reposp), repoabspaths))
repos = [{"repo": strmap(i), "abspath": i, "relapath": relamap(i)} for i in repoabspaths]

print(repos)


