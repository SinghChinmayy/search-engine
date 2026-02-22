import unicodedata

class TextNormalization:
    def __init__(self, text):
        self.text = text

    def normalize(self):
        # normalizing the text in NFKC format for higher compatability of search  
        text = unicodedata.normalize("NFKC", self.text)

        # Normalize Line Endings: 
        # Windows → \r\n 
        # Linux/macOS → \n

        text = text.replace("\r\n", "\n").replace("\r","\n")

        # case normalization 

        text = text.lower()

        # Punctualtion handling

        # ---will build it later ---

        # Strip the text 

        text = text.strip()
        return text