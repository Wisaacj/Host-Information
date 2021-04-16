import ipinfo

class IPDetails():

    def __init__(self, parsedData):
        # Setting up the handler for the ipinfo API
        self.access_token = "292aba28c3f144"
        self.handler = ipinfo.getHandler(self.access_token)
        # Assigning the parsed data to its own field
        self.parsedData = parsedData
        # Declaring a dictionary to hold the host data
        self.host_data = {}
        self.setupHostDataDic()

    def setupHostDataDic(self):
        for block in self.parsedData.keys():
            self.host_data[block] = {}

    def getHostInfo(self, debugging=False):
        for block in self.parsedData.keys():
            for ip in self.parsedData[block]:
                if (debugging):
                    print((self.handler.getDetails(ip)).details)
                self.host_data[block]["{}".format(ip)] = (self.handler.getDetails(ip)).details

        return self.host_data