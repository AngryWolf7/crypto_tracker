# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 00:47:29 2022

@author: Filippo Fagnani
"""

# Import libraries\n"
import xlsxwriter
import requests
import time

# Making list for multiple crypto
currencies = ["BTCBUSD","ETHBUSD","BNBBUSD","LINKBUSD",
              "ADABUSD","DOGEBUSD","VETBUSD","XRPBUSD",
              "ALGOBUSD","XLMBUSD","HBARBUSD","QNTBUSD",
              "MATICBUSD"]

# Defining Binance API URL
key = "https://api.binance.com/api/v3/ticker/price?symbol="

# running loop to print all crypto prices
j = 0
n = len(currencies)
x = [0] * n
y = [0] * n

now = time.ctime()
parsed = time.strptime(now)
print ('\n' + time.strftime("%a %d %b %H:%M:%S %Y", parsed))

for i in currencies:
    # completing API for request
    url = key+currencies[j]
    data = requests.get(url)
    data = data.json()
    print('\n' + data['symbol'])
    print(data['price'])
    x[j] = float(data['price'])
    y[j] = str(data['symbol'])
    j = j+1

# Creating xlsx with pairs prices
workbook = xlsxwriter.Workbook('actual_price.xlsx')
worksheet = workbook.add_worksheet()
     
i = 0
worksheet.write('D1', time.strftime("%a %d %b %H:%M:%S %Y", parsed))
for i in range(len(currencies)):
    a = "A" + str(i+1)
    b = "B" + str(i+1)
    worksheet.write(a, y[i])
    worksheet.write(b, x[i])
    i = i + 1

workbook.close()