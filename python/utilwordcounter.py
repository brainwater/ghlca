from collections import Counter
import re

class WordCounter:
    wordcountwhitespace = Counter()
    wordcountwordchars = Counter()
    charcount = Counter()
    def update(self, text):
        self.charcount.update(text)
        self.wordcountwhitespace.update(text.split())
        self.wordcountwordchars.update(re.split("[\W]+", text))
    
