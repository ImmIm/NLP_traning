import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
import numpy as np
import spacy
os.chdir('NLPScripts')

# Using sentiment dict for finance
sentiments = ['negative', 'positive', 'uncertainty', 'litigious','constraining']



def parse_sentiments():
    sentiment_df = pd.read_csv('data/Loughran-McDonald_MasterDictionary_1993-2021.csv')
    sentiment_df.columns = [column.lower() for column in sentiment_df.columns]
    sentiment_df = sentiment_df[sentiments + ['word']]
    sentiment_df[sentiments] = sentiment_df[sentiments].astype(bool)
    sentiment_df = sentiment_df[(sentiment_df[sentiments]).any(1)]
    
    return sentiment_df


df = parse_sentiments()
data = {'negative' : [],
     'positive': [],
     'uncertainty' : [],
     'litigious' : [], 
     'constraining' : [] 
    }

for line in df.iterrows():
    if line[1]['negative'] == True:
        data['negative'].append(line[1]['word'].lower())
        
    if line[1]['positive'] == True:
        data['positive'].append(line[1]['word'].lower())
        
    if line[1]['uncertainty'] == True:
        data['uncertainty'].append(line[1]['word'].lower())
        
    if line[1]['litigious'] == True:
        data['litigious'].append(line[1]['word'].lower())
        
    if line[1]['constraining'] == True:
        data['constraining'].append(line[1]['word'].lower())




def get_data_filters():
    df = parse_sentiments()
    data = {'negative' : [],
        'positive': [],
        'uncertainty' : [],
        'litigious' : [], 
        'constraining' : [] 
        }

    for line in df.iterrows():
        if line[1]['negative'] == True:
            data['negative'].append(line[1]['word'].lower())
            
        if line[1]['positive'] == True:
            data['positive'].append(line[1]['word'].lower())
            
        if line[1]['uncertainty'] == True:
            data['uncertainty'].append(line[1]['word'].lower())
            
        if line[1]['litigious'] == True:
            data['litigious'].append(line[1]['word'].lower())
            
        if line[1]['constraining'] == True:
            data['constraining'].append(line[1]['word'].lower())
            
            
    return data

