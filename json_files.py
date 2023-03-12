#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:09:46 2023

@author: agnieszka
"""
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#json_file = open('loan_data_json.json')
#data = json.load(json_file)

with open('loan_data_json.json') as json_file:
   data = json.load(json_file)
   print(data)
    
loandata = pd.DataFrame(data)

loandata['purpose'].unique()

loandata.describe()

loandata['int.rate'].describe()
loandata['fico'].describe()

income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#fico >= 300 and < 400: 'Very Poor'
#fico >= 400 and ficoscore < 600: 'Poor'
#fico >= 601 and ficoscore < 660: 'Fair'
#fico >= 660 and ficoscore < 780: 'Good'
#fico >=780: 'Excellent'

fico = 700

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >=400 and fico <600:
    ficocat = 'Poor'
elif fico >=601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 780:
    ficocat = 'Good'
elif fico >=780:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'

print(ficocat)

lista =[]
length = len(loandata)

for x in range(1,length):
    category = loandata['fico'][x]
    try:
        if category >= 300 and category < 400:
            ficocat = 'Very Poor'
        elif category >=400 and category <600:
            ficocat = 'Poor'
        elif category >=601 and category < 660:
            ficocat = 'Fair'
        elif category >= 660 and category < 780:
            ficocat = 'Good'
        elif fico >=780:
            ficocat = 'Excellent'
        else:
            ficocat = 'Unknown'
    except:
        ficocat = 'Unknown'
    lista.append(ficocat)

print(lista)    

ficocat2 = pd.Series(lista)
loandata['fico.category'] = ficocat2

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'

loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='green', width=0.4)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='green', width=0.4)
plt.show()

#scatter plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint,ypoint)
plt.show()

loandata.to_csv('loan_cleaned.csv', index=True)



