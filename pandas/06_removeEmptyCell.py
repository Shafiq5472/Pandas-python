# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:28:00 2022

@author: SHA NU
"""


#By default, the dropna() method returns a new DataFrame, and will not change the original.
import pandas as pd

df = pd.read_csv('dirtydata.csv')
print(df)
new_df = df.dropna()

print(new_df.to_string())

#%%
#Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame.
import pandas as pd

df = pd.read_csv('dirtydata.csv')

df.dropna(inplace = True)

print(df.to_string())
#Notice in the result that some rows have been removed (row 18, 22 and 28).

#These rows had cells with empty values.


