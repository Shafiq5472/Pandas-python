# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:52:36 2022

@author: SHA NU
"""

import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)