import pandas as pd
import numpy as np
import pandas_datareader.data as pdr

temp_df = pdr.DataReader("^VIX","yahoo", '2016-01-01', '2020-03-17')
