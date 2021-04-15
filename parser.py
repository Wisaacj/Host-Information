class Parser():

    def __init__(self, filename):
        self.filename = filename
        self.fileContents = self.openFile()

    def openFile(self):
        with open(self.filename) as f:
            contents = f.readlines()
        return contents

    def printData(self):
        for line in self.fileContents:
            print(line)

    def parseData(self):
        pass