import sys
import math
import numpy as np
import pandas as pd


df = pd.read_csv('/Users/jstrothe/Desktop/PycharmProjects/stockdatapractice/aapl.us.csv')

# Create a list of the close prices
close_price = df['Close'].tolist()

# Create a list of the daily returns % change, then round it
aapl_daily_returns = df['Close'].pct_change()
print("Average daily returns of Apple stock: ", round(aapl_daily_returns.mean(), 6), "%")

# Making the % daily returns into a list
returns_list = df['Close'].pct_change().tolist()
print(returns_list[1:5])

# Retrospectively apply the % change to the price to make sure it matches the data
hypothetical_list = [close_price[i-1] * 1+returns_list[i] for i in range(len(close_price))]
print(hypothetical_list[1:10])
