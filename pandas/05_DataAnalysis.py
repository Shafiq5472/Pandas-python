# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:13:28 2022

@author: SHA NU
"""

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))
print(df.tail())
print("_________________________________________")
#information
print(df.info()) 
