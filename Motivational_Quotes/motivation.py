# -*- coding: utf-8 -*-
"""
Motivation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jFLsm_mNhyVmrRCf3xCp9cjBgPmd7DRy
"""

import pandas as pd
import random

#Reads in a database of quotes
df = pd.read_json("Quotes\quotes.json")

#dropping the popularity axis 
df.drop('Popularity', axis=1, inplace=True)

#getting a list of categories
cat = df['Category'].unique()
print(cat)

# #Depreciated old way thats inefficient :(
# filtered = pd.DataFrame()
# for item in cat:
#     if(item == 'inspiration'):
#         filtered = pd.concat([df[df['Category']=='inspiration'],filtered])
#     elif(item == 'motivation'):
#         filtered = pd.concat([df[df['Category']=='motivation'],filtered])
#     elif(item == 'positive'):
#         filtered = pd.concat([df[df['Category']=='positive'],filtered])
# print(len(filtered))

#filtering on necessary categories
filtered = df.loc[df['Category'].isin(['motivation','inspiration','positive'])]
print(len(filtered))

#removing the quotes that fell under multiple categories
filtered = filtered.loc[filtered.astype(str).drop_duplicates().index]
print(len(filtered))

#stroing the quotes in a new JSON
result = filtered.to_json(r"Quotes\filtered.json")


