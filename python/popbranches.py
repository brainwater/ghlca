import ghlca
import sys
import github3 as gh3
import subprocess
import os.path

# This will put the number of branches and the list of brances into each repository document in the database


def insbranches(coll):
    for repo in coll.find():
        owner = repo["repository_owner"]
        reponame = repo["repository_name"]
        repokeys = list(repo.keys())
        #if ('num_branches' not in repokeys):
        confpath = os.path.expanduser(ghlca.datadir + '/' + str(owner) + '/' + str(reponame) + '.git/config')
        #print(os.path.isfile(confpath))
        if os.path.isfile(confpath):
            print(str(owner) + "/" + str(reponame))
            #print(ghlca.tmpfilename)
            pth = ghlca.datadir + '/' + str(owner) + '/' + str(reponame) + '.git'
            subprocess.call('cd ' + pth + ' && git branch -a | sed -e "s/^.* //" > ' + ghlca.tmpfilename, shell=True)
            tmpfile = open(ghlca.tmpfilename)
            branchesstring = tmpfile.read()
            branchesstring = branchesstring.rstrip()
            #print(branchesstring)
            tmpfile.close()
            branches = branchesstring.split('\n')
            print(len(branches))
            subprocess.call('rm ' + ghlca.tmpfilename, shell=True)
            repo["branches"] = branches
            repo["num_branches"] = len(branches)
            coll.save(repo)
            #break
            #ghrepo = None
            """try:
                ghrepo = ghlca.gh.repository(owner, reponame)
            except gh3.models.GitHubError:
                print("Github error " + str(sys.exc_info()[0]))
            if ghrepo:
                #print(ghrepo)
                branches = ghrepo.iter_branches()
                branch_list = list(map(lambda x: x.name, branches))
                #print(list(branches))
                repo["branches"] = branch_list
                repo["num_branches"] = len(branch_list)
                coll.save(repo)
            else:
                print("No repo found")"""
            

#print(ghlca.gh.ratelimit_remaining)
insbranches(ghlca.wcoll)
#print(ghlca.gh.ratelimit_remaining)
