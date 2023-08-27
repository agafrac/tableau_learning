#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:30:37 2023

@author: agnieszka
"""

import pandas as pd

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data = pd.read_excel('articles.xlsx')

data.describe()

data.info()

data.groupby(['source_id'])['article_id'].count()

data.groupby(['source_id'])['engagement_reaction_count'].sum()

data = data.drop(['engagement_comment_plugin_count'], axis=1)

keyword = 'crash'
# leng = len(data)

#keyword_flag = []

#for x in range(0,10):
#    heading = data['title'][x]
#    if keyword in heading:
#        flag = 1
#    else:
#        flag = 0
#    keyword_flag.append(flag)
    
#print(keyword_flag)
# print(flag)

def keywordflag(keyword):
    keyword_flag = []
    leng = len(data)
    for x in range(0,leng):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
        
keywordflag = keywordflag('murder')
print(keywordflag)

data['keyword_flag'] = pd.Series(keywordflag)

data.to_excel('blogme_clean.xlsx', sheet_name='blogme_data', index=False)