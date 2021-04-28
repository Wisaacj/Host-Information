from simpleParser import Parser
from ipDetails import IPDetails
from hostNetworkDetails import hostNetworkDetails
import json

if __name__ == "__main__":
    # Parsing the data from the text file for IP addresses
    p = Parser("data/rawData.txt")
    parsedData, avgRouteTimes = p.parseData()
    # Printing the average routes time
    print(avgRouteTimes)
    # Getting the information about the hosts
    ip = IPDetails(parsedData)
    host_data = ip.getHostInfo()
    # Parsing the ASNs from the host_data
    hnd = hostNetworkDetails(host_data)
    # Updating host_data to have an 'asn' field
    host_data = hnd.parseASNs()
    # Writing the ASNs to a file
    hnd.dumpASNs()
    # Instantiating a json object with the host_data dictionary
    host_data_json = json.dumps(host_data, indent = 4)
    # Exporting the host_data_json to a .json file
    with open("data/data.json", "w") as outfile:
        outfile.write(host_data_json)