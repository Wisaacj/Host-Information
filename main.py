from simpleParser import Parser
from ipDetails import IPDetails
import json

if __name__ == "__main__":
    # Parsing the data from the text file for IP addresses
    p = Parser("rawData.txt")
    parsedData = p.parseData()
    # Getting the information about the hosts
    ip = IPDetails(parsedData)
    host_data = ip.getHostInfo()
    # Instantiating a json object with the host_data dictionary
    host_data_json = json.dumps(host_data, indent = 4)
    # Exporting the host_data_json to a .json file
    with open("data.json", "w") as outfile:
        outfile.write(host_data_json)