import sys
import pandas as pd
import pandas_profiling as pp
import matplotlib as mp
import numpy as np
import plotly as pt
import plotly.io as pio
import plotly.graph_objects as go
import plotly.express as px
import math
import datetime as dt
import statistics

pio.renderers.default = "browser"

# df = pd.read_csv('/Users/jstrothe/Downloads/data.csv')
df2 = pd.read_csv('/Users/jstrothe/Desktop/PycharmProjects/stockdatapractice/aapl.us.csv')


fig = px.scatter(df2, x='Date', y='Open')
fig.update_traces(marker_color="turquoise",
                  marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text="Dividend and Earnings")
# fig.show()

close_price = df2['Close'].tolist()
PDR_list = []

def PDR(a, b):
    return math.log(a/b)

for i in close_price:
    x = PDR(i+1, i)
    PDR_list.append(x)
#print(PDR_list)

def Average(PDR_list):
    return sum(PDR_list) / len(PDR_list)
def stdAverage(PDR_list):
    return statistics.stdev(PDR_list)

average = Average(PDR_list)
stdAvg = stdAverage(PDR_list)
print('Average Daily Return =', round(average, 4))
print('Std Dev of Average Daily Return =', round(stdAvg, 4))

pvar = statistics.pvariance(PDR_list)
print('P.Variance = ', round(pvar, 4))

drift = average - (pvar / 2)
print('Drift = ', round(drift, 4))

#randomValue = stdAvg * np.random.normal(0, 1, size=None)
#print(randomValue)

random_list = []
num = 1000
def valueRandom(random_list):
    for n in range(num):
        y = stdAvg * np.random.normal(0, 1, size=None)
        random_list.append(y)
    return sum(random_list) / len(random_list)
random_value = valueRandom(random_list)
print('Average of Random value = ', random_value)

nextdaypricepossibilities = []
def nextdayprice2(nextdaypricepossibilities):
    for n in range(num):
        z = 0.42388 * (2.718 ** (drift + random_value))
        nextdaypricepossibilities.append(z)
    return sum(nextdaypricepossibilities) / len(nextdaypricepossibilities)
# should use the list of random values and plug them into the next day price possibilities, and then take the median of
# those (should theoretically be a bell curve)

#nextdayprice = 0.42388 * (math.e ** (drift + random_value))
nextprice2 = nextdayprice2(nextdaypricepossibilities)
print('next day price = ', nextprice2)



'''
start = dt.datetime(1984, 9, 7)
end = dt.datetime(2017, 11, 10)

prices = (start, end)
print(prices)

def findsdev():
    sdev = df2['Close'].std()
    round(sdev, 6)
    print("Standard deviation of closing prices: " + str(round(sdev, 6)))
    return sdev
findsdev()


# df["Periodic Daily Return"] = df["Jan"] + df["Feb"] + df["Mar"]
# def findpdr():


def df_to_plotly(df2):
    return {'z': df2.values.tolist(),
            'x': df2.columns.tolist(),
            'y': df2.index.tolist()}


dfNew = df2.corr()
fig2 = go.Figure(data=go.Heatmap(df_to_plotly(dfNew)))
# fig2.show()

# fig3 = px.scatter(df2, x='Long Interest Rate', y='Earnings')
# fig.update_traces(marker_color="turquoise",
#                   marker_line_color='rgb(8,48,107)',
#                   marker_line_width=1.5)
# fig.update_layout(title_text='Long Interest Rate and Earnings')
# fig3.show()'''
