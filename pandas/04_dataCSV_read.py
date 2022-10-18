# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:07:30 2022

@author: SHA NU
"""

import pandas as pd

df = pd.read_csv('data.csv')

print(df) 

#%%
#use to_string() to print the entire DataFrame

import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 

print('maximum rows ',pd.options.display.max_rows)

'''In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

You can change the maximum rows number with the same statement.'''
pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df) 

