import re 

class Parser():
    def __init__(self, pText):
        self.text = pText
        self.position = 0
        self.programm = []

    def parse(self):
        for string in self.text:
            if re.search(r"print(.)", string):
                pass