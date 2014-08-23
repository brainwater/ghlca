import ghlca
import os
import subprocess



def getlasthash(repo):
    fullname = repo["repository_full_name"]
    pth = ghlca.datadir + '/' + fullname + '.git'
    confpath = pth + '/config'
    if os.path.isfile(confpath):
        subprocess.call('cd ' + pth + ' && git log | head -n 1 | sed -e "s/commit //" > ' + ghlca.tmpfilename, shell=True)
        commit = open(ghlca.tmpfilename, "r").read().strip()
        subprocess.call('cd ' + pth + ' && git branch | grep -E "^\*" | sed -e "s/\* //" > ' + ghlca.tmpfilename, shell=True)
        branch = open(ghlca.tmpfilename, "r").read().strip()
        subprocess.call('rm ' + ghlca.tmpfilename, shell=True)
        print(fullname + " " + commit + " " + branch)
        
    
        #print("Repo " + fullname + " exists")
#    else:
#        print("Repository " + fullname + " does not exist.")

for i in ghlca.wcoll.find():
    getlasthash(i)
