import ghlca
import os.path
import subprocess
from collections import Counter

def getbranchnames(coll):
    branches = {}
    repobranches = map(lambda x: x.get("branches", []), coll.find())
    lst = [branch for branch_list in repobranches for branch in branch_list]
    counter = Counter(lst)
    #print('master: ' + str(branches.get('master', 0)))
    #print('develop: ' + str(branches.get('develop', 0)))
    print(counter.most_common(30))

getbranchnames(ghlca.wcoll)
