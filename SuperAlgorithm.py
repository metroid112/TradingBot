from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import pandas as pd
import csv

key = 'BHZ0R0KGWA6BWPON'

ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)

data = pd.read_csv('daily_goog.csv')
sma = pd.read_csv('sma_goog.csv')
# data, meta_data = ts.get_daily(symbol='GOOG')
# sma, meta_sma = ti.get_sma(symbol='GOOG')

#data.to_csv('daily_goog.csv')
#with open('sma_goog.csv', 'w') as f:
#	w = csv.DictWriter(f, sma.keys())
#	w.writeheader()
#	w.writerow(sma)

print(data['4. close'][0])
print(sma)

figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
data['4. close'].plot()
plt.tight_layout()
plt.grid()
# plt.show()