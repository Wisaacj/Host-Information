import re

# Class to parse the data from the text file
class Parser():

    def __init__(self, filename):
        # Fields for the data file
        self.filename = filename
        self.fileContents = self.openFile()
        # Dictionary to hold the parsed data
        self.parsedData = {}
        # Setting the pattern for finding IP addresses
        self.pattern =  re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    def openFile(self):
        with open(self.filename, "r") as f:
            contents = f.readlines()
        return contents

    def printData(self):
        for line in self.fileContents:
            print(line)

    def parseData(self):
        no_routes = 0

        for count, line in enumerate(self.fileContents):
            if ("traceroute" in line):
                self.parsedData["{}".format(no_routes)] = self.parseBlock(count+1)
                no_routes += 1

    def parseBlock(self, startIndex):
        block_data = []

        for line in self.fileContents[startIndex:]:
            if ("traceroute" in line):
                print("Looking for next traceroute")
                break

            try:
                ips = self.pattern.search(line)[0]
            except:
                pass

            if (ips != None):
                block_data.append(ips)

        print(block_data)
        return block_data