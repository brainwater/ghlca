import ghlca
import statistics

def getavgbranches(coll):
    #totalbranches=0
    #repocount=0
    branches=[]
    for repo in coll.find():
        if 'num_branches' in repo:
            branches.append(int(repo['num_branches']))
            #repocount += 1
            #totalbranches += int(repo['num_branches'])
    #print("Total branches: " + str(totalbranches))
    #print("Number of repos: " + str(repocount))
    print("Median: " + str(statistics.median(branches)))
    return statistics.mean(branches)
    #return float(totalbranches) / float(repocount)


print("Average number of branches: " + str(getavgbranches(ghlca.wcoll)))


            
