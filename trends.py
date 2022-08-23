#The program uses Pytrends to find trends for search terms
#InterestByRegion output is saved to intr_byRegion.png
#RelatedQueries output is saved to ai.csv and facial_rec.csv
import pandas as pd
from pytrends.request import TrendReq
import matplotlib
import matplotlib.pyplot as plt
import requests

pytrends = TrendReq(hl='en-US', timeout=5) #connect to google

#keywords list
keyWords = ['Artificial Intelligence', 'Facial Recognition']
#Timeframe is from today to the last 3 months
pytrends.build_payload(kw_list=keyWords,timeframe='today 3-m', geo='US')

#InterestByRegion
regionIntr = pytrends.interest_by_region()

#Plot interest by region data
def plot_RegIntr(df):
    #pandas dataframe = df
    fig = plt.figure(figsize=(15,8))
    ax = fig.add_subplot(111) #grid parameter is 1x1
    df.plot(ax = ax)
    plt.ylabel('Search Frequency')
    plt.xlabel('State')
    plt.ylim((0,120))
    plt.legend(loc='lower left')
    return ax
plt.style.use('fivethirtyeight')
ax=plot_RegIntr(regionIntr)
plt.savefig('intr_byRegion.png') #save plot to png file

def query_relate():
    #Related Queries
    relatedQueries = pytrends.related_queries()
    rq_ai = relatedQueries.get('Artificial Intelligence').get('rising') #display rising terms
    rq_ai.to_csv('ai.csv') #save related queries to csv file

    rq_facialRec = relatedQueries.get('Facial Recognition').get('rising')
    rq_facialRec.to_csv('facial_rec.csv') 
query_relate()