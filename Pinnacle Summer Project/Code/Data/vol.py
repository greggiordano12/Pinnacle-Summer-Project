import pandas as pd
import numpy as np
import pandas_datareader.data as pdr

temp_df = pdr.DataReader("^VIX","yahoo", '2010-01-01', '2020-03-17')


print(temp_df.head())


# We first can separate the vix data into the 3 regimes: low vol, med vol high vol
# Below 20 is low vol
# 20 - 30 is med vol
# Above 30 is high vol

dates = temp_df.index

# Assigning the dates to a regime
low_vol = []
med_vol = []
high_vol = []
for i in range(len(temp_df)):
    if(temp_df.Close[i] < 20):
        low_vol.append(dates[i])
    if(temp_df.Close[i] > 30):
        high_vol.append(dates[i])
    else:
        med_vol.append(dates[i])

print(len(low_vol))
print(len(med_vol))
print(len(high_vol))
