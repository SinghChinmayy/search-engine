class TxtLoader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load(self):
        file = open(self.file_path, encoding="utf-8")
        return file.read()
