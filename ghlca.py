
import subprocess as sp
import string
import random

from os import path

from pathlib import Path

print("Hello, world!")

datadir = "~/data/ghlca-repos"

tmppath = '/tmp/ghlca-' + ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
#tmpfile = open(tmppath, 'w')

repospathstr=path.expanduser('~/data/ghlca-repos')

reposp = Path(repospathstr)

repopaths =list(reposp.glob('**/*.git'))

print(dir(repopaths[0]))



#repopath='~/data/ghlca-repos/angular/angular.js.git'

#sp.call('git "--git-dir=' + path.expanduser(repopath) + '" branch -a > "' + tmppath + '"', shell=True)

#tmpfile.close()
#tmpfile = open(tmppath, 'r')
#print(tmpfile.read())
#tmpfile.close()
#sp.call('git --version')
