# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 23:24:31 2021

@author: Himanshu
"""


import pandas as pd

messages = pd.read_csv('spam.csv', sep='\t',names=["label", "message"],encoding="ISO-8859-1")


