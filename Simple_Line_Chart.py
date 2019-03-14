'''
Plotting stock price data for Infosys

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("data/INFY_test_data.csv")

# list(df.columns)
# del df['Turnover']
# del df['No. of Trades']
# del df['Symbol']  # You could keep it when dealing with multiple equities

# ensuring only equity series is considered
df = df.loc[df['Series'] == 'EQ']
## df.Series.count()  before and after

# Converting date to pandas datetime format
df['Date'] = pd.to_datetime(df['Date'])

#Plotting
plt.plot(df['Date'], df['Close Price'])

# Adding labels
plt.xlabel('Date')  
plt.ylabel('Close Price')  
plt.title('Simple time series plot for Infosys') 

plt.show()

# Saving image
plt.savefig('Simple Time Series Plot.png')
