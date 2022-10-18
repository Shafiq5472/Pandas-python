# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:39:57 2022

@author: SHA NU
"""

import pandas as pd

df = pd.read_csv('dirtydata.csv')

df.fillna(130, inplace = True)

print(df.to_string())

#Notice in the result: empty cells got the value 130 (in row 18, 22 and 28).

#%%
#Replace NULL values in the "Calories" columns with the number 130:

import pandas as pd

df = pd.read_csv('dirtydata.csv')

df["Calories"].fillna(130, inplace = True)
print(df)