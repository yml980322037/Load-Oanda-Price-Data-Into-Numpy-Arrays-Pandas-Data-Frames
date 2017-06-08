import numpy as np
import pandas
import oandapy

## Load Data from Oanda
# Set Environment and Access Token for Oanda - Can Accept "live" or "practice" As Envioronment
oanda = oandapy.API(environment="live", access_token="Access Token Goes Here")
# Set Pair, Timeframe and Number of Bars to Grab from Oanda
pair = "EUR_USD"
granularity = "D"
count = 4700 #4700 MAX for Daily Candles

# Grab Data from Oanda
response = oanda.get_history(instrument=pair, granularity=granularity, count=count)
# Store Candles in a List
candles = response.get('candles')
# Create Arrays to Store Data
dateList = []
openList = []
highList = []
lowList = []
closeList = []
volumeList = []

# Create Structured Numpy Array to Be Converted to Pandas DataFrame
npdataset = np.zeros(count, dtype = [('Date', 'U27'),
                                         ('Open', 'f'),
                                         ('High', 'f'),
                                         ('Low', 'f'),
                                         ('Close', 'f'),
                                         ('Volume', 'f')]
                           )

# While Loop to Fill Up Arrays with List Data
i = 0
while i < count:
    # Add data to individual Lists
    closeList.append(candles[i].get('closeBid'))
    openList.append(candles[i].get('openBid'))
    highList.append(candles[i].get('highBid'))
    lowList.append(candles[i].get('lowBid'))
    dateList.append(candles[i].get('time'))
    volumeList.append(candles[i].get('volume'))

    #Add Data to Dataset Array
    npdataset[i] = (candles[i].get('time'), candles[i].get('openBid'), candles[i].get('highBid'), candles[i].get('lowBid'), candles[i].get('closeBid'), candles[i].get('volume'))
    i += 1

# Convert Data Lists to Arrays using Numpy
date = np.array(dateList)
open = np.array(openList)
high = np.array(highList)
low = np.array(lowList)
close = np.array(closeList)
volume = np.array(volumeList)

# Convert Numpy Dataset to Pandas Dataframe
dataset = pandas.DataFrame(npdataset)
btdataset = pandas.DataFrame(npdataset)
print dataset
