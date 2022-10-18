# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:53:50 2022

@author: SHA NU
"""

'''
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.'''

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(myvar[0])

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

print(myvar["y"])
