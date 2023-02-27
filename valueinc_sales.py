#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:36:06 2023

@author: agnieszka
"""

import pandas as pd

data = pd.read_csv('transaction.csv', sep=';')
data.info()

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6


ProfitPerItem = SellingPricePerItem - CostPerItem
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased 

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

day = data['Day'].astype(str)
year = data['Year'].astype(str)


my_date = day + '-' + data['Month'] + '-' + year
data['date'] = my_date

split_col = data['ClientKeywords'].str.split(',', expand=True)

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

data['ClientAge'] = data['ClientAge'].str.replace('[' , '') 
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '') 
data['ItemDescription'] = data['ItemDescription'].str.lower()

season = pd.read_csv('value_inc_seasons.csv',sep=';')

data = pd.merge(data, season, on = 'Month')

data = data.drop('ClientKeywords',axis=1)
data = data.drop('Year',axis=1)
data = data.drop('Day',axis=1)
data = data.drop('Month',axis=1)
