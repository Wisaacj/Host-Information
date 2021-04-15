import ipinfo
from parser import Parser

"""
access_token = "292aba28c3f144"
handler = ipinfo.getHandler(access_token)

ip_address = "138.38.108.254"

details = handler.getDetails(ip_address)

print(details.all)
"""

p = Parser("rawData.txt")
p.printData()