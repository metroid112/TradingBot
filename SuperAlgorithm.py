from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

key = 'BHZ0R0KGWA6BWPON'

ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)

data, meta_data = ts.get_daily(symbol='GOOG')
sma, meta_sma = ti.get_sma(symbol='GOOG')

print(data['4. close'][0])
print(sma[1])

figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
data['4. close'].plot()
plt.tight_layout()
plt.grid()
# plt.show()