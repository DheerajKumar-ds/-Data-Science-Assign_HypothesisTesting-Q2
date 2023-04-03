# -*- coding: utf-8 -*-
"""

@author: user
"""

import numpy as np
import pandas as pd

df = pd.read_csv("LabTAT.csv")

#Applying Descriptive Statistics
df.describe()

#Checking for Null Values
df.isnull().sum()

#Checking for Duplicate Values
df[df.duplicated()].shape

#Checking the data type
df.info()

#Calculating P value

import scipy.stats as stats
Fcalc, Pval = stats.f_oneway(df["Laboratory 1"],df["Laboratory 2"], df["Laboratory 3"], df["Laboratory 4"])
print('p_value =',Pval.round(3))

alpha = 0.05
print('Significnace=%.3f, p=%.3f' % (alpha, Pval))
if Pval < alpha:
    print('Ho is rejected & H1 is accepted')
else:
    print('Ho is accepted & H1 is rejected')