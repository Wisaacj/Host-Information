class hostNetworkDetails():

    def __init__(self, host_data, filename="data.json"):
        self.host_data = host_data
        self.fileName = filename
        self.asnsFound = False

    def parseASNs(self):
        # Function to parse the ASNs (for each ip) from the organisation field in the host_data dictionary
        for block in self.host_data:
            for ip in self.host_data[block]:
                self.findOrganisationNetwork(block, ip)

        print("Completed ASN parsing")
        # Setting the 'asnsFound' boolean to True so that there won't be errors when parsing the asn details from the website later
        self.asnsFound = True

        return self.host_data

    def findOrganisationNetwork(self, block, ip):
        try:
            if(not (self.host_data[block]["{}".format(ip)]["org"] == "University of Bath Intranet")):
                self.host_data[block]["{}".format(ip)]["asn"] = self.host_data[block]["{}".format(ip)]["org"].split(" ")[0]

                if (self.host_data[block]["{}".format(ip)]["org"].split(" ")[1:] == ["Jisc", "Services", "Limited"]):
                    self.host_data[block]["{}".format(ip)]["host"] = "JANET"
                else:
                    self.host_data[block]["{}".format(ip)]["host"] = self.host_data[block]["{}".format(ip)]["org"].split(" ")[1:]
            else:
                self.host_data[block]["{}".format(ip)]["asn"] = "Bath University ASN"
                self.host_data[block]["{}".format(ip)]["host"] = "Bath University"
        except:
            print("Organisation field not found. Continuing...")

    def dumpASNs(self):
        # Function to dump the asns to a file
        if (self.asnsFound):
            output = []
            for block in self.host_data:
                for ip in self.host_data[block]:
                    try:
                        output.append(self.host_data[block]["{}".format(ip)]["asn"])
                    except:
                        print("ASN field not found. Continuing...")

            with open("data/asns.txt", "w") as outfile:
                # This line coverts the list to a comma-separated string and then writes the string to txt file
                outfile.write(','.join(map(str, output)))

            print("ASNs successfully written to file")
        else:
            print("Error: You must first run the function 'parseASNs()'")