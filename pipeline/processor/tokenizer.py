import re

class TextTokenize:
    def __init__(self, text):
        self.text = text

    def tokenize(self):
        tokens = re.findall(r"\b\w+(?:[-']\w+)*\b", self.text)
        return tokens