import ghlca

# This will link the data about the relative paths of the repos into the mongo database

def updaterepos(coll):
    for repo in coll.find():
        rurl = repo["repository_url"]
        rfname = rurl[19:]
        print(rfname)
        # Remove repositories with invalid urls, these are likely errors in the data on BigQuery
        if rfname.startswith("/"):
            print("Removing repo " + rfname)
            coll.remove(repo["_id"])
        else:
            subpayload = {}
            for k in repo.keys():
                if k.startswith("payload"):
                    subpayload[k] = repo[k]
                    #del repo[k]
            for k in subpayload.keys():
                del repo[k]
            if "subpayload" in repo:
                subpayload = dict(list(repo["subpayload"].items()) + list(subpayload.items()))
            repo["subpayload"] = subpayload
            repo["repository_full_name"] = rfname
            coll.save(repo)



updaterepos(ghlca.wcoll)

print("Done adding full name to repositories in wcoll")

updaterepos(ghlca.fcoll)

print("Done adding full name to repositories in fcoll")

