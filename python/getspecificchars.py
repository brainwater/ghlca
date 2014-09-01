import ghlca

# Gets a list of the characters most specific to the language

def getspecificchars(lang):
    chars = [char for char in ghlca.getlangwords(lang).find() if "tr" in char]
    schars = list(sorted(chars, key=lambda char: char["tr"], reverse=True))
    print(schars[:10])


getspecificchars("Java")
