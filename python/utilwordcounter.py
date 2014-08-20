from collections import Counter
import re

class WordCounter:
    def __init__(self):
        self.wordcountwhitespace = Counter()
        self.wordcountwordchars = Counter()
        self.charcount = Counter()
        
    def update(self, text):
        self.charcount.update(text)
        self.wordcountwhitespace.update(text.split())
        self.wordcountwordchars.update(re.split("[\W]+", text))
    
