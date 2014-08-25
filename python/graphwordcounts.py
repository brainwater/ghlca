import ghlca

def graphlangchars(lang):
    lchars = ghlca.getlangchars(lang)
    for i in lchars.find().sort({ "c": -1 }):
        print(i)

graphlangchars("Java")

