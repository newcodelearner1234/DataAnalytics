# -*- coding: utf-8 -*-
"""

@author: AVATANSH AWASTHI
"""
# Data-set Description.

"""

Abstract: The real estate valuation is a regression problem. The market historical data set of real estate valuation are collected from Sindian Dist., New Taipei City, Taiwan.

Data Set Characteristics: Multivariate

Number of Instances:414

Area: Business

Attribute Characteristics:Integer, Real

Number of Attributes:7

Date Donated: 2018-08-18

Associated Tasks: Regression

Missing Values? : N/A

Number of Web Hits: 95355

Source:

Original Owner and Donor Name: Prof. I-Cheng Yeh Institutions: Department of Civil Engineering, Tamkang University, Taiwan. Email: 140910 '@' mail.tku.edu.tw TEL: 886-2-26215656 ext. 3181

Date Donated: Aug. 18, 2018

Data Set Information:

The market historical data set of real estate valuation are collected from Sindian Dist., New Taipei City, Taiwan. The â€œreal estate valuationâ€ is a regression problem. The data set was randomly split into the training data set (2/3 samples) and the testing data set (1/3 samples).

Attribute Information:

The inputs are as follows X1=the transaction date (for example, 2013.250=2013 March, 2013.500=2013 June, etc.) X2=the house age (unit: year) X3=the distance to the nearest MRT station (unit: meter) X4=the number of convenience stores in the living circle on foot (integer) X5=the geographic coordinate, latitude. (unit: degree) X6=the geographic coordinate, longitude. (unit: degree)

The output is as follow Y= house price of unit area (10000 New Taiwan Dollar/Ping, where Ping is a local unit, 1 Ping = 3.3 meter squared)
"""

import pandas as pd
import statistics
import matplotlib.pyplot as plt

#Loading the data-set to the file

df = pd.read_csv("Real estate.csv") # reading csv file.
print("*********************************************************")
print("First 5 rows of the data-set :")
print("*********************************************************")
print(df.head()) # head() function gives the first 5 records

#Description of  the data-set
print("*********************************************************")
print("Statistical description of the data-set")
print("*********************************************************")
print(df.describe())  # describes the current data-set

#DATA PRE-Processing (removal of missing/ empty cells or unwanted columns/attributes)

#Finding missing values in each column
print("*********************************************************")
print("Number of missing values in each column")        
print("*********************************************************")
print(df.isnull().sum())  # finds number of empty cells in each column

#Replacing null values using median value
median1 = df['X2 house age'].median()      # finds median of the attribute and sets to a variable
median2 = df['X3 distance to the nearest MRT station'].median()
median3 = df['X4 number of convenience stores'].median()
median4 = df['X5 latitude'].median()
median5 = df['X6 longitude'].median()
median6 = df['Y house price of unit area'].median()

df['X2 house age'].fillna(median1, inplace=True)   # replaces null cell with median value 
df['X3 distance to the nearest MRT station'].fillna(median2, inplace=True)
df['X4 number of convenience stores'].fillna(median3, inplace=True)
df['X5 latitude'].fillna(median4, inplace=True)
df['X6 longitude'].fillna(median5, inplace=True)
df['Y house price of unit area'].fillna(median6, inplace=True)

print("*********************************************************")
print("Number of Null values after replace : " ,df.isnull().sum().sum())
print("*********************************************************")
print("BoxPlot for each attribute")
print("*********************************************************")

data = [df['X2 house age'],df['X3 distance to the nearest MRT station'],df['X4 number of convenience stores'],df['X5 latitude'],df['X6 longitude'],df['Y house price of unit area']]
fig,re = plt.subplots(figsize=(21,21)) # makes subplots
re.boxplot(data,labels=["X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude","Y house price of unit area"]) 
plt.show()

#Min Max normalization
def minmaxnormalization(col,ll,ul):
  arr1 = []                       # array  to store modified values
  mean = df[col].mean()           # mean of each column 
  sd = statistics.stdev(df[col])  # Std Deviation of each column
  max = df[col].max()
  min = df[col].min()
  
  for i in df[col]: 
    val = (i - min) / (max - min)
    val1 = val * (ul - ll)+ll
    arr1.append(val1)
   
  for  k in range(len(df)):
    df[col][k] = arr1[k-1]

columns = list(df)
print(columns)
for i in columns[5:]:
  minmaxnormalization(i,1,10)
#Printing status of dataset after min-max normalisation
print("*********************************************************")
print("After Min Max normalization")
print("*********************************************************")
print(df)

#Visualisation
print("*********************************************************")
print("Scatter Plots of different Columns vs X1")
print("*********************************************************")
for i in columns[3:]:
  plt.scatter(df['X1 transaction date'],df[i]) # makes scatter plot for selected columns. 
  plt.show()