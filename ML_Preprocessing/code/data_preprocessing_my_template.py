# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
dataset = pd.read_csv("Data.csv")
''''Loading DataSet from Local Machine'''

# dataset.fillna(dataset.mean(),inplace=True)
X= dataset.iloc[:, :-1].values
'''Creating Independant features vector from Dataset'''
X= pd.DataFrame(X) 
'''Converting Data set to Pandas Data Format to apply fillna method'''

X.fillna(X.mean(), inplace=True) 
'''Filling missing values by mean of that column using fillna method'''
Y= dataset.iloc[:,3].values
'''Creating dependant features vector from Dataset'''


# from sklearn.impute import SimpleImputer 
# imputer = SimpleImputer (missing_values= 0,strategy='mean')
# imputer= imputer.fit(X[:,1:3])
# X[:,1:3]= imputer.transform(X[:,1:3])

# ------------
# dataset= dataset.fillna(-999,inplace=True)
# x= dataset.iloc[:, :-1].values
# # y= dataset.iloc[:,3].values

# # from sklearn.impute import SimpleImputer 
# # imputer = SimpleImputer (missing_values= '-999',strategy='mean')
# # imputer= imputer.fit(x[:,1:3])
# # x[:,1:3]= imputer.transform(x[:,1:3])
 