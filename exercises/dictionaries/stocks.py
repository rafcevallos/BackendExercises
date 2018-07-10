# NOTES:
# DEFINITION: A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. Each value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.

# an unordered set of key: value pairs, with the requirement that the keys are unique (within one dictionary)

# ITERATING OVER DICTIONARIES:
# Dictionaries can be iterated over, just like a list. However, a dictionary, unlike a list, DOES NOT keep the order of the values stored in it. To iterate over key value pairs, use the following syntax:
# phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
# for name, number in phonebook.items():
# print("Phone number of %s is %d" % (name, number))

# REMOVING A VALUE:
# del phonebook["John"] or phonebook.pop("John")

# Dictionary of Stocks
stockDict = {
    'GM': 'General Motors',
    'CAT': 'Caterpillar',
    'EK': "Eastman Kodak",
    'PP': "Poopy Poo"
}

# List of tuples
purchases = [
    ('GM', 100, '10-sep-2001', 48),
    ('CAT', 100, '1-apr-1999', 24),
    ('EK', 200, '1-jul-1998', 56),
    ('GM', 150, '27-jan-2018', 100),
    ('PP', 500, '3-may-2017', 500)
]

# Purchase History Report
for stock in purchases:
    purchased_stocks = str(stock[1]) + " stocks of " + stockDict[stock[0]] + " cost us " + "$"+str((stock[1])*(stock[3]))
    print("Stock info: ", purchased_stocks)


# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

# total_investment is an empty dictionary that will hold the key: value pairs in stockDict
total_investment = {}
total_investment = dict((ticker, 0) for ticker in stockDict.keys())
print(total_investment)
# loop through purchases
for stock in purchases:
    total_investment[stock[0]] += stock[1]*stock[3] # match the keys in total_investment and stock and multiply the values
print(total_investment)
