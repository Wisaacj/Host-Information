# Host-Information
Python application to find information about each of the hosts on a tracert request.

## Classes

There are two 'homemade' classes:

1. Parser()
2. IPDetails()

## Parser()

The Parser() class splits each tracert into 'blocks' and within each block,
the parser looks for IP addresses and appends them to a sub-dictionary (defined by the block)
of a parsedData dictionary.

## IPDetails()

The IPDetails() class takes a parsedData dictionary as an input and outputs
a host_data dictionary containing all the publically availabel information
about each of the hosts in the dictionary.
