# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 18:25:16 2022

@author: shano
"""
import panda as pd
df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  
with pd.ExcelWriter("E:\E\hydrogen like atom.xlsx") as writer:
    df.to_excel(writer)