import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
import numpy as np
import spacy
os.chdir('NLPScripts')



text = '''
Sept 10 (Reuters) - Wall Street's main indexes were subdued on Friday as signs of higher inflation and a drop in Apple shares following an unfavorable court ruling offset expectations of an easing in U.S.-China tensions.

Data earlier in the day showed U.S. producer prices rose solidly in August, leading to the biggest annual gain in nearly 11 years and indicating that high inflation was likely to persist as the pandemic pressures supply chains. read more .

"Today's data on wholesale prices should be eye-opening for the Federal Reserve, as inflation pressures still don't appear to be easing and will likely continue to be felt by the consumer in the coming months," said Charlie Ripley, senior investment strategist for Allianz Investment Management.

Apple Inc (AAPL.O) fell 2.7% following a U.S. court ruling in "Fortnite" creator Epic Games' antitrust lawsuit that stroke down some of the iPhone maker's restrictions on how developers can collect payments in apps.


Sponsored by Advertising Partner
Sponsored Video
Watch to learn more
Report ad
Apple shares were set for their worst single-day fall since May this year, weighing on the Nasdaq (.FIXX) and the S&P 500 technology sub-index (.SPLRCT), which fell 0.1%.

Sentiment also took a hit from Cleveland Federal Reserve Bank President Loretta Mester's comments that she would still like the central bank to begin tapering asset purchases this year despite the weak August jobs report. read more

Investors have paid keen attention to the labor market and data hinting towards higher inflation recently for hints on a timeline for the Federal Reserve to begin tapering its massive bond-buying program.

The S&P 500 has risen around 19% so far this year on support from dovish central bank policies and re-opening optimism, but concerns over rising coronavirus infections and accelerating inflation have lately stalled its advance.


Report ad
The three main U.S. indexes got some support on Friday from news of a phone call between U.S. President Joe Biden and Chinese leader Xi Jinping that was taken as a positive sign which could bring a thaw in ties between the world's two most important trading partners.

At 1:01 p.m. ET, the Dow Jones Industrial Average (.DJI) was up 12.24 points, or 0.04%, at 34,891.62, the S&P 500 (.SPX) was up 2.83 points, or 0.06%, at 4,496.11, and the Nasdaq Composite (.IXIC) was up 12.85 points, or 0.08%, at 15,261.11.

Six of the eleven S&P 500 sub-indexes gained, with energy (.SPNY), materials (.SPLRCM) and consumer discretionary stocks (.SPLRCD) rising the most.

U.S.-listed Chinese e-commerce companies Alibaba and JD.com , music streaming company Tencent Music (TME.N) and electric car maker Nio Inc (NIO.N) all gained between 0.7% and 1.4%


Report ad
Grocer Kroger Co (KR.N) dropped 7.1% after it said global supply chain disruptions, freight costs, discounts and wastage would hit its profit margins.

Advancing issues outnumbered decliners by a 1.12-to-1 ratio on the NYSE and by a 1.02-to-1 ratio on the Nasdaq.

The S&P index recorded 14 new 52-week highs and three new lows, while the Nasdaq recorded 49 new highs and 38 new lows.
'''
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

