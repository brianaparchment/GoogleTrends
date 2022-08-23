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