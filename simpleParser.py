import re

# Class to parse the IPs from the text file
class Parser():

    def __init__(self, filename):
        # Fields for the data file
        self.filename = filename
        self.fileContents = self.openFile()
        # Dictionary to hold the parsed data
        self.parsedData = {}
        # Dictionary to hold the average route time for each traceroute
        self.avgRouteTimes = {}
        # Setting the pattern for finding IP addresses
        self.pattern =  re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    def openFile(self):
        with open(self.filename, "r") as f:
            contents = f.readlines()
        return contents

    def printData(self):
        for line in self.fileContents:
            print(line)

    def parseData(self, debugging=False):
        no_routes = 0

        for count, line in enumerate(self.fileContents):
            if ("traceroute" in line):
                self.parsedData["{}".format(no_routes)], self.avgRouteTimes["{}".format(no_routes)] = self.parseBlock(count+1, debugging)
                no_routes += 1

        return self.parsedData, self.avgRouteTimes

    def parseBlock(self, startIndex, debugging=False):
        block_data = []
        block_route_time = 0

        for line in self.fileContents[startIndex:]:
            if ("traceroute" in line):
                if (debugging):
                    print("Looking for next traceroute")
                break

            try:
                ips = self.pattern.search(line)[0]

                if (ips != None):
                    block_data.append(ips)

                splittedLine = line.split(" ")

                avg_time = 0
                timeCount = 0

                for i, split in enumerate(splittedLine):
                    if (split == "ms" or split == "ms\n"):
                        avg_time += float(splittedLine[i-1])
                        timeCount += 1

                avg_time /= timeCount
                block_route_time += avg_time

            except:
                pass

        # Print the block's data if debugging mode is enabled
        if (debugging):
            print(block_data)

        return block_data, block_route_time