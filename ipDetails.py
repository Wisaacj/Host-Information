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

                currDetails = (self.handler.getDetails(ip)).details

                # Checking to see if the ip details request failed
                if (currDetails["ip"] == "172.16.0.1"):
                    self.host_data[block]["{}".format(ip)] = currDetails
                    self.host_data[block]["{}".format(ip)]["city"] = "Bath"
                    self.host_data[block]["{}".format(ip)]["region"] = "England"
                    self.host_data[block]["{}".format(ip)]["country_name"] = "United Kingdom"
                    self.host_data[block]["{}".format(ip)]["org"] = "University of Bath Intranet"
                else:
                    self.host_data[block]["{}".format(ip)] = currDetails

        return self.host_data