# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:58:44 2022

@author: SHA NU
"""

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
#refer to the named index:
print(df.loc["day2"])